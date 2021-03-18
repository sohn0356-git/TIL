package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.TextView
import kotlinx.android.synthetic.main.activity_frame_layout_exam.*

class FrameLayout_exam : AppCompatActivity(), View.OnClickListener {
    var idx = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_frame_layout_exam)

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