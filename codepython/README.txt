#bật môi trường ảo linux
source codepython/bin/activate
cd codepython

#cài các thư viện
chmod +rx installScript.sh
./installScript.sh 

#train model
python trainModel.py
#kiểm tra kết quả
python test.py

=======================================

#bật môi trường ảo window
codepython\Scripts\activate
cd codepython

#cài các thư viện: thực ra cái file bash này cho linux chứ win vẫn lỗi cái pyaudio :v
bash installScript.sh 


