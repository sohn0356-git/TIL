package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import java.util.*

class FindViewTestActivity : AppCompatActivity(), View.OnClickListener {
    var btnClick:Button?=null
    var btnCancel:Button?=null
    var tv_result:TextView?=null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_find_view_test)
        btnClick = findViewById(R.id.btn_dream1)
        btnCancel = findViewById(R.id.btn_dream2)
        tv_result = findViewById(R.id.tv_result)
        btnClick?.setOnClickListener(this)
        btnCancel?.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when(v?.id){
            btnClick?.id ->{
                btnClick?.setText(Date().toString())
            }
            btnCancel?.id -> {
                btnClick?.setText("버튼누르기")
            }
        }
    }
}