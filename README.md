# Instagram_Imposter_Detector
Find out who are the people whom you follow on Instagram but they don't follow you back

## How to use the program
Go to your instagram profile -> Followers . Now copy the whole thing and paste it in "Followers.txt". Just keep the Name, Username and "Username's profile picture" in the file and remove everything else from it. Do the same for the following as well in "Following.txt" using your following data. Now run the `run.bat` file. You will be asked whether you want to know your "Extra followers" (People who follow you but you don't follow them back) or "Imposters" (People whom you follow on Instagram but they don't follow you back). Press `1` or `2` based on your choice.

## Known bug
Every profile you copy should have the above listed 3 data. If any of the three is missing, you shall get weird and incorrect results. So have a look at the data in the txt files and add a `.` in appropriate locations to compensate the missing conditions. Remember, the program is supposed to print the *USERNAME* of the accounts.