from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1130_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1130_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_BB7",          # 01, 1
        "Function_2_CBD",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31B")

    ChrTalk(    #0
        0x101,
        (
            "#1002F那卡片里的地方……\x02\x03",

            "……莫非是指这里？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_176")

    ChrTalk(    #1
        0x103,
        (
            "#022F嗯，虽然有这可能性……\x02\x03",

            "稍后再进行那个事件的调查吧。\x01",
            "现在要赶紧前往拉文努村哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_317")

    label("loc_176")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_204")

    ChrTalk(    #3
        0x108,
        (
            "#072F嗯，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在应该赶紧前往拉文努村。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_317")

    label("loc_204")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292")

    ChrTalk(    #5
        0x104,
        (
            "#030F唔，是有这可能……\x02\x03",

            "不过那个事件的调查稍后再进行吧。\x01",
            "现在先赶紧前往拉文努村吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002F啊，嗯……明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_317")

    label("loc_292")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_317")

    ChrTalk(    #7
        0x105,
        (
            "#042F嗯，说不定就是……\x02\x03",

            "不过这里迟些再调查吧。\x01",
            "现在得赶紧前往拉文努村啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1002F啊，嗯……说得对。\x02",
    )

    CloseMessageWindow()

    label("loc_317")

    TalkEnd(0xFF)
    Return()

    label("loc_31B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 15500, 4000, 43010, 90)
    SetChrPos(0xF7, 15490, 4000, 44530, 180)
    SetChrPos(0xF8, 14760, 4000, 45010, 180)
    SetChrPos(0xF9, 15520, 4000, 45770, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383")
    SetChrPos(0x4, 14740, 4000, 46100, 180)

    label("loc_383")

    OP_6D(15000, 4500, 43060, 0)
    OP_67(0, 4940, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(47000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #9
        0x101,
        (
            "#1002F这个，是七耀教会的圣典吧。\x02\x03",

            "『女神的话语』\x01",
            "莫非就是说这个？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_462")

    ChrTalk(    #10
        0x103,
        (
            "#026F圣典被认为是女神\x01",
            "赐予的美好教诲之书。\x02\x03",

            "#020F大概是不会错的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E")

    label("loc_462")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AF")

    ChrTalk(    #11
        0x108,
        (
            "#070F圣典是女神\x01",
            "赐予的美好教诲之书。\x02\x03",

            "恐怕不会有错吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E")

    label("loc_4AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50B")

    ChrTalk(    #12
        0x104,
        (
            "#035F圣典被认为是女神\x01",
            "赐予的美好教诲之书。\x02\x03",

            "#030F我想恐怕不会有错吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E")

    label("loc_50B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55E")

    ChrTalk(    #13
        0x106,
        (
            "#053F圣典好像是女神\x01",
            "赐予的美好教诲之书。\x02\x03",

            "#050F大概不会有错吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #14
        0x101,
        (
            "#1015F啊，这么说来在主日学校\x01",
            "好像也听说过这个似的……\x02\x03",

            "#1000F……那好。\x01",
            "先调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05调查圣典\x01",
            "发现其中夹着铁制的勋章。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #16
        "\x07\x00得到了\x07\x02#16I宝剑天马大勋章\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #17
        0x101,
        (
            "#1001F嘿嘿，找到啦！\x02\x03",

            "#1016F不，不过\x01",
            "好夸张的勋章啊～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FA")

    ChrTalk(    #18
        0x104,
        (
            "#031F哈哈，厚重夸张\x01",
            "正是埃雷波尼亚的国风嘛。\x02\x03",

            "和利贝尔王国的那种俭朴悠闲的\x01",
            "国风正好相反。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF")

    label("loc_6FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75A")

    ChrTalk(    #19
        0x105,
        (
            "#045F嗯，因为厚重夸张\x01",
            "是那边的国风嘛。\x02\x03",

            "但这种国风竟然还\x01",
            "反映在勋章上了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF")

    label("loc_75A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #20
        0x108,
        (
            "#070F唔，是帝国国风吧。\x02\x03",

            "一般说来帝国\x01",
            "很喜欢厚重夸张的风气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF")

    label("loc_7AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FF")

    ChrTalk(    #21
        0x103,
        (
            "#021F呵呵，这是帝国国风嘛。\x02\x03",

            "帝国有喜好厚重夸张\x01",
            "事物的倾向哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF")


    ChrTalk(    #22
        0x101,
        (
            "#1011F唔……原来如此。\x01",
            "这就是所谓国民性的差异吧。\x02\x03",

            "#1016F嗯，不过想想也对，\x01",
            "这种程度的震撼力大概还是有必要的。\x02\x03",

            "因为这个可是\x01",
            "达维尔大使的勋章呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E3")

    ChrTalk(    #23
        0x106,
        (
            "#051F哈哈，说得好。\x02\x03",

            "那大叔的脸\x01",
            "和这勋章也不相上下嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1")

    label("loc_8E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_92E")

    ChrTalk(    #24
        0x107,
        (
            "#067F嘿嘿，大概吧。\x02\x03",

            "那个大叔的脸\x01",
            "也是蛮有震撼力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1")

    label("loc_92E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_983")

    ChrTalk(    #25
        0x103,
        (
            "#020F呵呵，说得好。\x02\x03",

            "那个达维尔大使的脸\x01",
            "也是相当有震撼力的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D1")

    label("loc_983")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D1")

    ChrTalk(    #26
        0x108,
        (
            "#071F哈哈，说得好。\x02\x03",

            "那位大人的面孔\x01",
            "也是相当的厚重夸张啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A41")

    ChrTalk(    #27
        0x108,
        (
            "#070F唔，现在看起来\x01",
            "大概更加这么觉得了。\x02\x03",

            "但也可能由于这次勋章被偷，\x01",
            "他心情变得非常地差。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B58")

    label("loc_A41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #28
        0x105,
        (
            "#040F嗯，现在\x01",
            "更加觉得他的脸夸张了。\x02\x03",

            "可能因为勋章被盗\x01",
            "令他更加焦虑导致的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B58")

    label("loc_AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFB")

    ChrTalk(    #29
        0x103,
        (
            "#020F现在说不定\x01",
            "还更严重了呢。\x02\x03",

            "由于这件事\x01",
            "皱纹都多出好几条了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B58")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #30
        0x104,
        (
            "#030F唔，现在说不定\x01",
            "他的脸变得更夸张了。\x02\x03",

            "勋章被偷的事\x01",
            "好像让他相当焦虑。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B58")


    ChrTalk(    #31
        0x101,
        (
            "#1015F哎呀，这么说还真是呢。\x02\x03",

            "#1001F那么就马上\x01",
            "把勋章送还吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1132   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_BB7(): pass

    label("Function_1_BB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC4")
    Return()

    label("loc_BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD6")
    Return()

    label("loc_BD6")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_C11")
    Call(1, 2)
    Jump("loc_CB6")

    label("loc_C11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_C20")
    Call(1, 2)
    Jump("loc_CB6")

    label("loc_C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_C78")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_CB6")

    label("loc_C78")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_CB6")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_1_BB7 end

    def Function_2_CBD(): pass

    label("Function_2_CBD")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D2A")

    ChrTalk(    #34
        0x8,
        (
            "我也为你们祈祷，\x01",
            "一定能找到照片上的少女的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "不到最后不要放弃希望，\x01",
            "请一定要完成使命。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCB")

    label("loc_D2A")


    ChrTalk(    #36
        0x8,
        (
            "嗬，在追寻\x01",
            "照片中少女的脚步吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "实在遗憾，\x01",
            "我没有印象……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "如果有女神的指引，\x01",
            "就一定能遇见的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "不到最后不要放弃希望，\x01",
            "请一定要完成使命。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DCB")

    TalkEnd(0x8)
    Return()

    # Function_2_CBD end

    SaveToFile()

Try(main)
