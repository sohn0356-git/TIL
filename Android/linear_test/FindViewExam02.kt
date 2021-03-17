package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_find_view_test.*
import kotlinx.android.synthetic.main.findview_exam.*
import java.util.*

class FindViewExam02 : AppCompatActivity(), View.OnClickListener  {
    var imageview:ImageView ?= null
    var btn_dream1: Button?= null
    var btn_dream2: Button?= null
    var btn_beach1: Button?= null
    var btn_ic: Button?= null
    var btn_beach2: Button?= null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_find_view_exam02)
        imageview = findViewById(R.id.imageview)
        btn_dream1 = findViewById(R.id.btn_dream1)
        btn_dream2 = findViewById(R.id.btn_dream2)
        btn_beach1 = findViewById(R.id.btn_beach1)
        btn_ic = findViewById(R.id.btn_ic)
        btn_beach2 = findViewById(R.id.btn_beach2)
        btn_dream1?.setOnClickListener(this)
        btn_dream2?.setOnClickListener {
            imageview?.setImageResource(R.drawable.dream02)
        }
        var mylistener1 = object : View.OnClickListener {
            override fun onClick(v: View?) {
                imageview?.setImageResource(R.drawable.beach)
            }
        }
        btn_beach1?.setOnClickListener(mylistener1)
        btn_ic?.setOnClickListener(object :View.OnClickListener {
            override fun onClick(v: View?) {
                    imageview?.setImageResource(R.drawable.ic_launcher_background)
            }
        })
            var mylistener2 = object : View.OnClickListener {
            override fun onClick(v: View?) {
                when (v?.id) {
                    btn_dream1?.id -> {
                        imageview?.setImageResource(R.drawable.dream01)
                    }
                    btn_dream2?.id -> {
                        imageview?.setImageResource(R.drawable.dream02)
                    }
                    btn_ic?.id -> {
                        imageview?.setImageResource(R.drawable.ic_launcher_background)
                    }
                    btn_beach1?.id, btn_beach2?.id -> {
                        imageview?.setImageResource(R.drawable.beach)
                    }
                }
            }
        }
        btn_beach2?.setOnClickListener(mylistener2)
    }

    override fun onClick(v: View?) {
        imageview?.setImageResource(R.drawable.dream01)
    }
}


