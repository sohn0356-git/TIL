package com.example.linear_test

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView

class FrameLayout_test : AppCompatActivity(), View.OnClickListener {
    var idx = 0
    var image:Array<ImageView>?=null
    var btn_image:Button?=null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_frame_layout_test)
        var imageview1:ImageView = findViewById(R.id.iv_1)
        var imageview2:ImageView = findViewById(R.id.iv_2)
        btn_image = findViewById(R.id.btn_login)
        btn_image?.setOnClickListener(this)
        image = arrayOf(imageview1,imageview2)
    }

    override fun onClick(v: View?) {
        imageChange()
    }

    fun imageChange(){
        image?.get(idx)?.visibility = View.GONE
        idx = (idx+1)% (image?.size ?: 1)
        image?.get(idx)?.visibility = View.VISIBLE

    }

}