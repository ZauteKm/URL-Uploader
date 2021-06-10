class Translation(object):
    START_TEXT = """Hello,
This is a Telegram URL Upload Bot!

<b>Please send me any Direct download URL link, I can upload to telegram as File/Video</b>
Hits /help for more details..

➟ <b>Made by @ZauteKm</b>"""
    RENAME_403_ERR = "Sorry. You are not permitted to rename this file."
    ABS_TEXT = " Please don't be selfish."
    UPGRADE_TEXT = "<b>👉 Create own Clone Bot.. </b>  \n\n<a href='https://youtu.be/T6FYjPW1cBE'>Click here, Fork and Deploy!!</a>"
    FORMAT_SELECTION = "<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a> \n<b>If you want to set custom thumbnail,</b> send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """<b>If you want to download premium videos,</b> provide in the following format:
<b>URL | filename | username | password</b>"""
    NOYES_URL = "@robot URL detected. Please use https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
    DOWNLOAD_START = "<b>📥 Downloading...</b>"
    UPLOAD_START = "<b>Uploading now... 📤</b>"
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Please rate me if you find me useful. Join : @ZauteSupport"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n<b>Share & Support Me :</b> [👉 Share](https://t.me/share/url?url=Hi%20Friend%2C%0D%0AAm%20Introducing%20a%20Powerful%20%2A%2AURL%20Uploader%20@ZauTeKm%20Bot%2A%2A%20for%20Free.%0D%0A%2A%2ABot%20Link%2A%2A%20%3A%20%40uploadzKbot) \nUploaded in {} seconds."
    NOT_AUTH_USER_TEXT = "Please /upgrade your subscription."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Detected File Size: {}. Free Users can only upload: {}\nPlease /upgrade your subscription.\nIf you think this is a bug, please contact <a href='https://telegram.dog/MizoHelpDesK'>@MizoHelpDesK</a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "<b>✅ Custom thumbnail cleared succesfully.</b>"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "<b>✅ Media cleared succesfully.</b>"
    SAVED_RECVD_DOC_FILE = "<b>Document Downloaded Successfully.</b>"
    CUSTOM_CAPTION_UL_FILE = "<b>Share & Support Me:</b> [Share](https://t.me/share/url?url=Hi%20Friend%2C%0D%0AAm%20Introducing%20a%20Powerful%20%2A%2AURL%20Uploader%20@ZauTeKm%20Bot%2A%2A%20for%20Free.%0D%0A%2A%2ABot%20Link%2A%2A%20%3A%20%40uploadzKbot)"
    NO_CUSTOM_THUMB_NAIL_FOUND = "<b>No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently.</b>"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """<b>Current plan details</b>
--------
Telegram ID: <code>{}</code>
"""
    HELP_USER = """<b>Hi I'm URL Uploader Bot.</b>
    
1. Send url (Link|New Name with Extension).
2. Send Custom Thumbnail (Optional).
3. Select the button.
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
   
--------
Send /me to know current plan details

➟ <b>Made by @ZauteKm</b>
"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n© @ZauteKm"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "https://telegram.dog/ZauTeSupport"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://t.me/iZaute/5'>Support Group</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Uploaded {} files in {} seconds"
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
