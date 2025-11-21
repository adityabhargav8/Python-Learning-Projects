import json
def load_data ():
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)          #jason.load() converts jason data into list 
    except FileNotFoundError:
            return []

def save_data_helper (videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\nVideo list :")
    print('-'*100)
    for index , video in enumerate(videos, start =1):
        print(f" {index}. {video['name']} | Duration : {video['time']} min ")
    print('-'*100)

def delete_all (videos):
    choice = input("Do you want to delete all videos :  ")
    if choice == "yes" or choice == "Yes" or choice == "YES":
        print("Deleted all videos")
    else:
        print("not deleted ")

#thinking of a way to add this

def add_video (videos):
    print("\nAdd video :")
    print("-"*100)
    name = input("Enter video name: ")
    time = input("Enter video duration: ")
    if name == '' or time == '':
        print("Enter valid video name and duration")
    else:
        videos.append({'name': name, 'time': time})
        save_data_helper(videos)

def update_video (videos):
    print("\nUpdate video :")
    print("-"*100)
    while True:
        try:
            index = int(input("Enter the video number to update : "))
        except ValueError:
            print("Invalid index! \nPlease enter again\n")
            continue                    #ignore next lines in loop 
        if index >=1 and index <= len(videos):
            break                       # valid index continue
        else:
            print(f'Enter a valid index between 1 and {len(videos)}\n')

    name = input("Enter new video name: ")
    time = input("Enter new video duration: ")
    current_video = videos[index-1]
    if name.strip():
        current_video['name']= name
    if time.strip():
        current_video['time']= time
    save_data_helper(videos)
    print("\nUpdated sucessfully!\n\nUpdated list : ")
    list_all_videos(videos)
   
        


def delete_video (videos):
    print("\nDelete video :")
    print("-"*100)
    index = int(input("Enter the video number to delete : "))
    if index >=1 and index <= len(videos):
        print(f"Deleting vedio at index : {index}, video name : {videos[index-1]['name']} and  Duration: {videos[index-1]['time']}")
        del videos[index-1]
        save_data_helper(videos)
    else:
        print('Enter a valid index')


def main():             
    videos = load_data()
    while True :
        print("\nYouTube Manager")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update description")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice : ")
        match choice:
            case '1':
                list_all_videos(videos)
                delete_all(videos)
            case '2':
                add_video(videos)
            case '3':
                list_all_videos(videos)
                update_video(videos)
            case '4':
                list_all_videos(videos)
                delete_video(videos)
            case '5':
                print("\nまたね means Bye for now\n")
                break
            case _ :
                print("Invalid choice! Choose again")

# entry point of program
if __name__ == "__main__":
    main()