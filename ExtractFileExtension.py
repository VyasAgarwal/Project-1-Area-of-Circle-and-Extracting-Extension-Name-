x = input("Input the Filename: ")
ext = x.split(".")
d = {"py" : "python",
"mp3" : "MP3 Audio File",
"zip" : "Zip Compressed File",
"sql" : "SQL Database File",
"vcf" : "E-Mail Contact File",
"apk" : "Android Package File",
"jar" : "Java Archive File",
"jpeg" : "JPEG Image",
"psd" : "PSD Image",
"png" : "PNG Image",
"js" : "JavaScript File",
"xhtml" : "XHTML File",
"ppt" : "PowerPoint Presentation",
"pptx" : "PowerPoint Open XML Presentation",
"c" : "C and C++ Source Code File",
"xls" : "Microsoft Excel File",
"xlsx" : "Microsoft Excel Open XML Spreadsheet File",
"mp4" : "MPEG4 Video File",
"docx" : "Word File",
"doc" : "Microsoft Word File",
"pdf" : "PDF File",}
print ("The extension of the file is : " + d[(ext[-1])])