import os
import shutil


def UploadFile(OriginalFilePath, Target):
    shutil.copy(OriginalFilePath, Target)


def AddProfileImg(UploaderName,Type,FilePath):
    try:
        Path = f"./Assets/Profiles/{Type}s/{UploaderName}"
        fileName = FilePath.split("/")[-1]
        filePath = (Path + "/" + fileName)
        if Type == "Teacher" and not os.path.isfile(filePath):
            os.mkdir(Path)
            UploadFile(FilePath, filePath)
        elif Type == "Student" and not os.path.isfile(filePath):
            os.mkdir(Path)
            UploadFile(FilePath, filePath)
        return filePath
    except:
        print("An Error Occurred During Adding Profile Img Probably File Source Is not Found")


def AddLectureFile(UploaderName,LectureName,FilePath):
    try:
        TeacherPath = f"./Assets/Lectures/{UploaderName}"
        if not os.path.isdir(TeacherPath):
            os.mkdir(TeacherPath)
        TotalPath = f"./Assets/Lectures/{UploaderName}/{LectureName}"
        if not os.path.isdir(TotalPath):
            os.mkdir(TotalPath)
        fileName = FilePath.split("/")[-1]
        filePath = (TotalPath + "/" + fileName)
        if not os.path.isfile(filePath):
            UploadFile(FilePath, filePath)
        else:
            print("File Is Already Exist")
        return filePath
    except:
        print("An Error Occurred During Adding Lecture File Probably File Source Is not Found")
