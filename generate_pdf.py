import json
import boto3
from datetime import datetime
from fpdf import FPDF

s3 = boto3.client('s3')

BUCKET_NAME = 'deleted-orders-backup-adi-2026'


def lambda_handler(event, context):
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='deleted-orders/')

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, text="Deleted Orders Summary Report", ln=True, align='C')
        pdf.cell(200, 10, text=f"Generated at: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.ln(10)

        count = 0
        if 'Contents' in response:
            for item in response['Contents']:
                key = item['Key']
                if key.endswith('/'):
                    continue

                file_obj = s3.get_object(Bucket=BUCKET_NAME, Key=key)
                content = file_obj['Body'].read().decode('utf-8')

                # Encoding handling to prevent font errors
                safe_text = f"{count + 1}. File: {key.split('/')[-1]} -> {content[:100]}"
                safe_text = safe_text.encode('latin-1', 'replace').decode('latin-1')

                pdf.cell(200, 10, text=safe_text, ln=True)
                count += 1

        if count == 0:
            pdf.cell(200, 10, text="No deleted orders found.", ln=True)

        pdf_file_path = '/tmp/summary_report.pdf'
        pdf.output(pdf_file_path)

        pdf_key = f"reports/summary_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.pdf"
        s3.upload_file(
            pdf_file_path,
            BUCKET_NAME,
            pdf_key,
            ExtraArgs={'ACL': 'public-read', 'ContentType': 'application/pdf'}
        )

        pdf_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{pdf_key}"

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'PDF generated successfully',
                'pdfUrl': pdf_url
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }