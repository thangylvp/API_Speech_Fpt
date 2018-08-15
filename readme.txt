File đầu vào input.json (3 key)
	- voice : là 1 trong 4 string "mienbac_nu" "mienbac_nam" "mientrung" "miennam" tương ứng với các giọng nói
	- msg : câu cần nói.
	- image : đường dẫn file ảnh
	- Định dạng file utf-8

Code api.py:
	- Cài đặt vlc media player
	- LIB: matplotlib json requests vlc time io mutagen urllib