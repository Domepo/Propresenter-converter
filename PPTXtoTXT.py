from pptx import Presentation
import glob
import string
for eachfile in glob.glob("*.pptx"):
    filea = eachfile.replace(".pptx","")    
    file = open(filea+".txt","w") 
    prs = Presentation(eachfile)
    print(eachfile)
    print("----------------------")
    for slide in prs.slides:
        for shape in slide.shapes:         
            if hasattr(shape, "text"):
                if shape.text.isdigit() == True :
                    print("Fool")
                else:   
                    file.write(shape.text)
                    file.write("\n")
                    file.write("\n")
    file.close() 
