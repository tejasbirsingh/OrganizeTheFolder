import os 
from time import sleep
from tqdm import tqdm


def createFolder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def move(name , files):
	for file in files:
		os.replace(file ,"{}/{}".format(name, file))


if __name__ == "__main__":

	files = os.listdir()
	files.remove("main.py")

	print(*files,sep='\n')

	createFolder('Images')
	createFolder('Documents')
	createFolder('Media')
	createFolder('Others')

	imgExts = [".png",".jpg",".jpeg",".gif"]
	images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

	docExts = [".txt",".docx",".pdf",".doc"]
	docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts ]

	mediaExts = [".mp4",".mp3",".avi",".flv"]
	medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts ]
	 


	others = []
	for file in files:
		ext = os.path.splitext(file)[1].lower()
		if(ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
			others.append(file)

	
	for i in tqdm(range(80),desc='Moving'):

		sleep(0.01)

		
	print()
	move("Media",medias)
	move("Images",images)
	move("Documents",docs)
	move("Others" , others)
	
	newFiles = os.listdir()
	print(*newFiles,sep='\n')
	
