package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.util.*


class FindViewExam : AppCompatActivity(), View.OnClickListener {
    var btn_Click:Button?=null
    var tv_data:TextView?=null
    var tv_result:TextView?=null
    var ed_data:EditText?=null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_find_view_exam)
        btn_Click = findViewById(R.id.btn_Click)
        tv_data = findViewById(R.id.tv_data)
        tv_result = findViewById(R.id.tv_exam_result)
        ed_data = findViewById(R.id.et_data)
        btn_Click?.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when(v?.id){
            btn_Click?.id ->{
                tv_result?.setText("결과 : "+ed_data?.text)
            }
        }
    }
}