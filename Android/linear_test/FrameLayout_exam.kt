package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView

class FrameLayout_exam : AppCompatActivity(), View.OnClickListener {
    var idx = 0
    var btn_login:Button?=null
    var btn_register:Button?=null
    var btn_detail:Button?=null
    var btn_insert:Button?=null
    var btn_insert2:Button?=null
    var ll_login:LinearLayout?=null
    var ll_register:LinearLayout?=null
    var ll_detail:LinearLayout?=null
    var ed_login1:EditText?=null
    var ed_login2:EditText?=null
    var ed_reg1:EditText?=null
    var ed_reg2:EditText?=null
    var ed_reg3:EditText?=null
    var tv_login:TextView?=null
    var tv_register:TextView?=null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_frame_layout_exam)
        ll_login = findViewById(R.id.ll_login)
        ll_register = findViewById(R.id.ll_register)
        ll_detail = findViewById(R.id.ll_detail)
        ed_login1 = findViewById(R.id.ed_login1)
        ed_login2 = findViewById(R.id.ed_login2)
        ed_login1 = findViewById(R.id.ed_login1)
        ed_reg1 = findViewById(R.id.ed_reg1)
        ed_reg2 = findViewById(R.id.ed_reg2)
        ed_reg3 = findViewById(R.id.ed_reg3)
        tv_login = findViewById(R.id.tv_login)
        tv_register = findViewById(R.id.tv_register)
        btn_login = findViewById(R.id.btn_login)
        btn_register = findViewById(R.id.btn_register)
        btn_detail = findViewById(R.id.btn_detail)
        btn_insert = findViewById(R.id.btn_insert)
        btn_insert2 = findViewById(R.id.btn_insert2)
        btn_login?.setOnClickListener(this)
        btn_register?.setOnClickListener(this)
        btn_detail?.setOnClickListener(this)
        btn_insert?.setOnClickListener(this)
        btn_insert2?.setOnClickListener(this)
    }

    override fun onClick(v: View?) {
        when(v?.id){
            R.id.btn_login->{
                ll_register?.visibility = View.GONE
                ll_detail?.visibility = View.GONE
                ll_login?.visibility = View.VISIBLE
            }
            R.id.btn_register->{
                ll_detail?.visibility = View.GONE
                ll_login?.visibility = View.GONE
                ll_register?.visibility = View.VISIBLE
            }
            R.id.btn_detail->{
                ll_register?.visibility = View.GONE
                ll_login?.visibility = View.GONE
                ll_detail?.visibility = View.VISIBLE
            }
            R.id.btn_insert->{
                var id = ed_login1?.text.toString()
                var pw = ed_login2?.text.toString()
                tv_login?.setText(id+"\n"+pw)
            }
            R.id.btn_insert2->{
                var id = ed_reg1?.text.toString()
                var name = ed_reg2?.text.toString()
                var pw = ed_reg3?.text.toString()
                tv_register?.setText(id+"\n"+name+"\n"+pw)
            }
        }
    }

}