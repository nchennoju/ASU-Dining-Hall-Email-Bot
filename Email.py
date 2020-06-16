import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DISLIKES = ["Pepperoni", "Ham", "Beef", "Pork"]
LIKES = ["Chicken", "Omlette", "Fried", "Teriyaki", "Noodles", "Curly fries", ]

class Email:

    mealType = ["BREAKFAST", "LUNCH", "DINNER"]

    def __init__(self, sender_email, password, receiver_email, data, date, mealNum):

        message = MIMEMultipart("alternative")

        #swap month and day
        dt = date.split("/")
        date = dt[1] + '/' + dt[0] + '/' + dt[2]

        message["Subject"] = str(date) + ": " + self.mealType[mealNum]
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        html = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
        <head>
        <!--[if gte mso 9]><xml><o:OfficeDocumentSettings><o:AllowPNG/><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml><![endif]-->
        <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
        <meta content="width=device-width" name="viewport"/>
        <!--[if !mso]><!-->
        <meta content="IE=edge" http-equiv="X-UA-Compatible"/>
        <!--<![endif]-->
        <title></title>
        <!--[if !mso]><!-->
        <!--<![endif]-->
        <style type="text/css">
                body {
                    margin: 0;
                    padding: 0;
                }
        
                table,
                td,
                tr {
                    vertical-align: top;
                    border-collapse: collapse;
                }
        
                * {
                    line-height: inherit;
                }
        
                a[x-apple-data-detectors=true] {
                    color: inherit !important;
                    text-decoration: none !important;
                }
            </style>
        <style id="media-query" type="text/css">
                @media (max-width: 610px) {
        
                    .block-grid,
                    .col {
                        min-width: 320px !important;
                        max-width: 100% !important;
                        display: block !important;
                    }
        
                    .block-grid {
                        width: 100% !important;
                    }
        
                    .col {
                        width: 100% !important;
                    }
        
                    .col>div {
                        margin: 0 auto;
                    }
        
                    img.fullwidth,
                    img.fullwidthOnMobile {
                        max-width: 100% !important;
                    }
        
                    .no-stack .col {
                        min-width: 0 !important;
                        display: table-cell !important;
                    }
        
                    .no-stack.two-up .col {
                        width: 50% !important;
                    }
        
                    .no-stack .col.num4 {
                        width: 33% !important;
                    }
        
                    .no-stack .col.num8 {
                        width: 66% !important;
                    }
        
                    .no-stack .col.num4 {
                        width: 33% !important;
                    }
        
                    .no-stack .col.num3 {
                        width: 25% !important;
                    }
        
                    .no-stack .col.num6 {
                        width: 50% !important;
                    }
        
                    .no-stack .col.num9 {
                        width: 75% !important;
                    }
        
                    .video-block {
                        max-width: none !important;
                    }
        
                    .mobile_hide {
                        min-height: 0px;
                        max-height: 0px;
                        max-width: 0px;
                        display: none;
                        overflow: hidden;
                        font-size: 0px;
                    }
        
                    .desktop_hide {
                        display: block !important;
                        max-height: none !important;
                    }
                }
            </style>
        </head>
        <body class="clean-body" style="margin: 0; padding: 0; -webkit-text-size-adjust: 100%; background-color: #179bc4;">
        <!--[if IE]><div class="ie-browser"><![endif]-->
        <table bgcolor="#179bc4" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="table-layout: fixed; vertical-align: top; min-width: 320px; Margin: 0 auto; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #179bc4; width: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td style="word-break: break-word; vertical-align: top;" valign="top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color:#179bc4"><![endif]-->
        <div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #179bc4;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#179bc4;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#179bc4"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#179bc4;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 10px; padding-right: 10px; padding-bottom: 10px; padding-left: 10px;" valign="top">
        <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td height="0" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>
        <div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #171717;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#171717;background-image:url('images/302a8575-f046-420b-96ef-41a9b0caf7f8.jpg');background-position:top center;background-repeat:repeat">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#171717"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#171717;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 20px; padding-left: 20px; padding-top:55px; padding-bottom:55px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:55px; padding-bottom:55px; padding-right: 20px; padding-left: 20px;">
        <!--<![endif]-->
        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 20px; padding-left: 20px; padding-top: 0px; padding-bottom: 0px; font-family: Tahoma, sans-serif"><![endif]-->
        <div style="color:#ffffff;font-family:Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;line-height:1.2;padding-top:0px;padding-right:20px;padding-bottom:0px;padding-left:20px;">
        <div style="font-size: 14px; line-height: 1.2; color: #ffffff; font-family: Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 17px;">
        <p style="font-size: 42px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 50px; margin: 0;"><span style="font-size: 42px;">"""

        #Add dining hall to eat at
        points = []
        for i in range(len(data)):
            #change to open when done testing
            if(data[i][1] == "Open"):
                pt = 1
                all_items = []
                for j in range(len(data[i][2])):
                    all_items += data[i][2][j]
                print(all_items)
                for j in range(len(all_items)):
                    tmp = self.content(all_items[j] + ": " + data[i][3][j])
                    pt += self.numContains(all_items[j], LIKES)
                points.append(pt)
            else:
                points.append(0)

        max_PT = 0
        for i in range(len(points)):
            if(points[i] > points[max_PT]):
                max_PT = i
        if(not (max_PT == 0)):
            html += "You should eat at " + data[max_PT][0].replace(' - Arizona State University', '')
        else:
            html += "All Dining Halls Closed :("






        html += """</span></p>
        </div>
        </div>
        <!--[if mso]></td></tr></table><![endif]-->
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>
        <div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #179bc4;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#179bc4;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#179bc4"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#179bc4;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:0px; padding-bottom:0px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:0px; padding-bottom:0px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 5px; padding-right: 10px; padding-bottom: 0px; padding-left: 10px;" valign="top">
        <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" height="0" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 0px solid transparent; height: 0px; width: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td height="0" style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>"""

        end_html = """
        <div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #179bc4;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#179bc4;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#179bc4"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#179bc4;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <table border="0" cellpadding="0" cellspacing="0" class="divider" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td class="divider_inner" style="word-break: break-word; vertical-align: top; min-width: 100%; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; padding-top: 0px; padding-right: 10px; padding-bottom: 5px; padding-left: 10px;" valign="top">
        <table align="center" border="0" cellpadding="0" cellspacing="0" class="divider_content" role="presentation" style="table-layout: fixed; vertical-align: top; border-spacing: 0; border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-top: 1px solid #2FA5CA; width: 100%;" valign="top" width="100%">
        <tbody>
        <tr style="vertical-align: top;" valign="top">
        <td style="word-break: break-word; vertical-align: top; -ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%;" valign="top"><span></span></td>
        </tr>
        </tbody>
        </table>
        </td>
        </tr>
        </tbody>
        </table>
        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, sans-serif"><![endif]-->
        <div style="color:#a7d1e3;font-family:Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
        <div style="font-size: 14px; line-height: 1.2; color: #a7d1e3; font-family: Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 17px;">
        <p style="font-size: 11px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 13px; margin: 0;"><span style="font-size: 11px;">This message was sent to you from Nitish's email bot because you subscribed for the service.</span></p>
        </div>
        </div>
        <!--[if mso]></td></tr></table><![endif]-->
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
        </tr>
        </tbody>
        </table>
        <!--[if (IE)]></div><![endif]-->
        </body>
        </html>"""



        for i in range(len(data)):
            #change to open when done testing
            if(data[i][1] == "Open"):
                html += self.openHeader(data[i][0] + " - ")
                all_items = []
                for j in range(len(data[i][2])):
                    all_items += data[i][2][j]
                print(all_items)
                for j in range(len(all_items)):
                    tmp = self.content(all_items[j] + ": " + data[i][3][j])
                    if(not self.contains(all_items[j], DISLIKES) and not self.contains(data[i][3][j], DISLIKES)):
                        html += tmp
            else:
                html += self.closeHeader(data[i][0] + " - ")

        # Turn these into plain/html MIMEText objects
        part = MIMEText(html+end_html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    def convStringToHtml(self, tag, str, style):
        return "<" + tag + " style=\"" + style + "\">" + str + "</" + tag + ">"

    def contains(self, str, user_ls):
        for i in range(len(user_ls)):
            if (user_ls[i].lower() in str.lower()):
                return True
        return False

    def numContains(self, str, user_ls):
        num = 0
        for i in range(len(user_ls)):
            if(user_ls[i].lower() in str.lower()):
                num+=1
        return num

    def openHeader(self, str):
        return """<div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #1fe163;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#1fe163;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#1fe163"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#1fe163;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, sans-serif"><![endif]-->
        <div style="color:#555555;font-family:Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
        <div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14px;">
        <p style="font-size: 20px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 24px; margin: 0;"><span style="color: #ffffff; font-size: 20px;">""" + str + """ OPEN</span></p>
        </div>
        </div>
        <!--[if mso]></td></tr></table><![endif]-->
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>"""

    def content(self, str):
        return """<div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #ffffff;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#ffffff;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#ffffff"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#ffffff;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, sans-serif"><![endif]-->
        <div style="color:#555555;font-family:Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
        <div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14px;">
        <p style="font-size: 14px; line-height: 1.2; word-break: break-word; text-align: left; mso-line-height-alt: 17px; margin: 0;">""" + str + """</p>
        </div>
        </div>
        <!--[if mso]></td></tr></table><![endif]-->
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>"""

    def closeHeader(self, str):
        return """<div style="background-color:transparent;">
        <div class="block-grid" style="Margin: 0 auto; min-width: 320px; max-width: 590px; overflow-wrap: break-word; word-wrap: break-word; word-break: break-word; background-color: #f2575a;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color:#f2575a;">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:transparent;"><tr><td align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:590px"><tr class="layout-full-width" style="background-color:#f2575a"><![endif]-->
        <!--[if (mso)|(IE)]><td align="center" width="590" style="background-color:#f2575a;width:590px; border-top: 0px solid transparent; border-left: 0px solid transparent; border-bottom: 0px solid transparent; border-right: 0px solid transparent;" valign="top"><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 0px; padding-left: 0px; padding-top:5px; padding-bottom:5px;"><![endif]-->
        <div class="col num12" style="min-width: 320px; max-width: 590px; display: table-cell; vertical-align: top; width: 590px;">
        <div style="width:100% !important;">
        <!--[if (!mso)&(!IE)]><!-->
        <div style="border-top:0px solid transparent; border-left:0px solid transparent; border-bottom:0px solid transparent; border-right:0px solid transparent; padding-top:5px; padding-bottom:5px; padding-right: 0px; padding-left: 0px;">
        <!--<![endif]-->
        <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding-right: 10px; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; font-family: Tahoma, sans-serif"><![endif]-->
        <div style="color:#555555;font-family:Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;line-height:1.2;padding-top:10px;padding-right:10px;padding-bottom:10px;padding-left:10px;">
        <div style="line-height: 1.2; font-size: 12px; color: #555555; font-family: Oxygen, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 14px;">
        <p style="font-size: 20px; line-height: 1.2; word-break: break-word; text-align: center; mso-line-height-alt: 24px; margin: 0;"><span style="font-size: 20px; color: #ffffff;">""" + str + """CLOSED</span></p>
        </div>
        </div>
        <!--[if mso]></td></tr></table><![endif]-->
        <!--[if (!mso)&(!IE)]><!-->
        </div>
        <!--<![endif]-->
        </div>
        </div>
        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        <!--[if (mso)|(IE)]></td></tr></table></td></tr></table><![endif]-->
        </div>
        </div>
        </div>"""