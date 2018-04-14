from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132_2 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
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
        Unknown_30              = 35,
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
        "Function_1_16D",          # 01, 1
        "Function_2_2B2",          # 02, 2
        "Function_3_62F",          # 03, 3
        "Function_4_1427",         # 04, 4
        "Function_5_15E4",         # 05, 5
        "Function_6_190D",         # 06, 6
        "Function_7_1AD1",         # 07, 7
        "Function_8_1B8A",         # 08, 8
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_108")
    TalkBegin(0x10)
    TurnDirection(0x10, 0x0, 0)

    ChrTalk(    #0
        0x10,
        (
            "刚才开始\x01",
            "外边就吵闹得很厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        "……有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    TalkEnd(0x10)
    Jump("loc_16C")

    label("loc_108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_128")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 6)
    Jump("loc_16C")

    label("loc_128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_145")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 5)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_16C")

    label("loc_145")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_162")
    EventBegin(0x0)
    OP_4A(0x10, 255)
    Call(2, 2)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Jump("loc_16C")

    label("loc_162")

    TalkBegin(0x10)
    Call(2, 1)
    TalkEnd(0x10)

    label("loc_16C")

    Return()

    # Function_0_AA end

    def Function_1_16D(): pass

    label("Function_1_16D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1AC")

    ChrTalk(    #2
        0x10,
        (
            "我在等人\x01",
            "但怎么也不来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "呼，就不能快点吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1")

    label("loc_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_208")

    ChrTalk(    #4
        0x10,
        "据说近来危险的魔兽很多呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "自己１个人\x01",
            "去调查实在是不行的啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259")

    label("loc_208")

    OP_A2(0x7)

    ChrTalk(    #6
        0x10,
        (
            "听协会的消息\x01",
            "据说近来危险的魔兽很多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "最好避免\x01",
            "一个人走在大道上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259")

    Jump("loc_2B1")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2B1")
    OP_8C(0x10, 346, 0)

    ChrTalk(    #8
        0x10,
        (
            "嗯～照相机准备了\x01",
            "备用感光结晶回路也买了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "……好，准备ＯＫ。\x02",
    )

    CloseMessageWindow()

    label("loc_2B1")

    Return()

    # Function_1_16D end

    def Function_2_2B2(): pass

    label("Function_2_2B2")

    Call(2, 7)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2FC")

    ChrTalk(    #10
        0x10,
        "咦，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "难道\x01",
            "其它的事已经完成了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E")

    label("loc_2FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_334")

    ChrTalk(    #12
        0x10,
        "啊，是游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        "已经有空闲了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_42E")

    label("loc_334")


    ChrTalk(    #14
        0x101,
        "#1011F对了，打扰一下行吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 400)
    Sleep(400)

    ChrTalk(    #15
        0x10,
        "好的，有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F我们看了公告板来的，\x01",
            "您是森特先生吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        "啊，是游击士们吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "呀～等候多时了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "我想马上拜托你们点事，\x01",
            "现在有时间吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_28(0x66, 0x1, 0x1)
    OP_28(0x66, 0x1, 0x2)
    OP_28(0x66, 0x4, 0x4)
    OP_28(0x66, 0x4, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_4A5")
    Call(2, 4)
    Jump("loc_4A9")

    label("loc_4A5")

    Call(2, 3)

    label("loc_4A9")

    Jump("loc_62A")

    label("loc_4AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_539")

    ChrTalk(    #20
        0x101,
        (
            "#1007F嗯～抱歉。\x01",
            "还不行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "哎呀呀，是吗？\x01",
            "唉，没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "如果有空闲了\x01",
            "请再来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1000F嗯，我们会再来的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(    #24
        0x101,
        "#1015F嗯～还不行呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "哎呀呀，还不行吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "有空的话\x01",
            "再拜托你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1007F嗯，抱歉哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A")

    label("loc_5AE")

    OP_28(0x66, 0x1, 0x8000)

    ChrTalk(    #28
        0x101,
        (
            "#1007F啊，抱歉。\x01",
            "现在不太方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "哎呀呀，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "那么，如果有空闲了\x01",
            "再拜托你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1006F嗯，好吧。\x02",
    )

    CloseMessageWindow()

    label("loc_62A")

    Call(2, 8)
    Return()

    # Function_2_2B2 end

    def Function_3_62F(): pass

    label("Function_3_62F")


    ChrTalk(    #32
        0x101,
        (
            "#1006F嗯，没问题。\x02\x03",

            "那么，是怎样的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "嗯，想拜托你们去\x01",
            "拍摄『绀碧之塔』的照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "希望你们去塔顶，\x01",
            "把某样东西拍下来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_709")

    ChrTalk(    #35
        0x106,
        (
            "#050F说到『绀碧之塔』……\x02\x03",

            "是说在阿伊纳街道岔路上，\x01",
            "古代遗迹的塔吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_756")

    ChrTalk(    #36
        0x103,
        (
            "#020F绀碧之塔就是指……\x02\x03",

            "是说在阿伊纳街道岔路上的\x01",
            "古代遗迹塔吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756")


    ChrTalk(    #37
        0x10,
        (
            "没错。\x01",
            "知道得真清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1011F不过，为什么\x01",
            "需要塔的照片呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        "#1018F啊，难道是新办的杂志社吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        "不不，不是啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "我是王都历史资料馆\x01",
            "派遣来的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "所以，这次的调查\x01",
            "是学术上的调查。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_869")

    ChrTalk(    #43
        0x104,
        "#030F呼，学术调查啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_889")

    label("loc_869")


    ChrTalk(    #44
        0x101,
        "#1008F是吗，是学术调查啊。\x02",
    )

    CloseMessageWindow()

    label("loc_889")


    ChrTalk(    #45
        0x10,
        "对，是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "……不过，这次调查\x01",
            "稍微有点特别。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1011F……特别？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_928")

    ChrTalk(    #48
        0x106,
        (
            "#053F嗯，关于这个\x01",
            "以后再说吧。\x02\x03",

            "#050F总之现在\x01",
            "确认工作内容优先。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_977")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_977")

    ChrTalk(    #49
        0x103,
        (
            "#026F嗯，关于这个\x01",
            "以后再说吧。\x02\x03",

            "#020F总之现在\x01",
            "确认工作内容优先哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_977")

    SetChrName("森特")

    ChrTalk(    #50
        0x10,
        (
            "哦，对不起。\x01",
            "跑题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "嗯～说到哪里了？\x02",
    )

    CloseMessageWindow()

    def lambda_9B4():
        TurnDirection(0xF7, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9B4)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #52
        0x101,
        (
            "#1011F要爬上塔顶，\x01",
            "拍摄某样东西啦。\x02\x03",

            "#1015F……那个，『某样东西』是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        "是塔顶上的『谜之装置』。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "虽是古代文明的遗物，\x01",
            "用途却完全不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "因此没办法，我们研究者\x01",
            "仅仅称之为『装置』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1011F塔顶上的装置……\x02\x03",

            "就是那个台座一样的机械？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_BB2")

    ChrTalk(    #57
        0x10,
        "咦，你知道吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "对对，就是那个。\x01",
            "确实是像台座一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1002F嗯，其实我已经去看过了。\x02\x03",

            "总觉得那个『装置』，\x01",
            "放射着奇怪的光……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        "嗯嗯，我知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "资料馆里也收到了\x01",
            "可靠的报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5F")

    label("loc_BB2")


    ChrTalk(    #62
        0x10,
        "咦，你知道吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "对对，就是那个。\x01",
            "确实是像台座一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1001F啊，果然是说那个啊。\x02\x03",

            "虽然好像已经不能动了，\x01",
            "但的的确确是『装置』的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "不，那其实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        "好像也不是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1011F咦？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "那个『装置』……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        "……好像还在动。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x101,
        (
            "#1004F在、在动吗……！？\x02\x03",

            "那个奇怪的机械！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "是，我们也收到了\x01",
            "可靠的报告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        "误报的可能性很低。\x02",
    )

    CloseMessageWindow()

    label("loc_D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D9D")

    ChrTalk(    #74
        0x106,
        (
            "#053F原来如此啊……\x02\x03",

            "#050F所以才急忙来调查吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD1")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DD1")

    ChrTalk(    #75
        0x103,
        (
            "#027F原来如此……\x02\x03",

            "所以才突然来调查吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(    #76
        0x10,
        "是、是的，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "总而言之有必要\x01",
            "记录『装置』的现状。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1003F确实很诡异……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "虽然现在那个『装置』\x01",
            "好像还没有危险性……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "但要发生什么也不足为奇。\x01",
            "请多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1002F嗯，我们不会大意的。\x02\x03",

            "那么，拍下了『装置』\x01",
            "再回到这里就行了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1037")

    label("loc_EE1")


    ChrTalk(    #82
        0x10,
        "是、是的，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10,
        (
            "总而言之\x01",
            "有必要确认一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1002F确实很诡异……\x01",
            "不能放任不理。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F6C")

    ChrTalk(    #85
        0x106,
        "#050F『装置』没有危险吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_F92")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_F92")

    ChrTalk(    #86
        0x103,
        "#022F『装置』没有危险吗？\x02",
    )

    CloseMessageWindow()

    label("loc_F92")


    ChrTalk(    #87
        0x10,
        (
            "是，目前的状况来说\x01",
            "『装置』本身没有危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "当然，即使如此\x01",
            "也不能断言说很安全。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1002F嗯，我们会多加小心的。\x02\x03",

            "那么，摄影结束以后\x01",
            "再回到这里就行了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1037")


    ChrTalk(    #90
        0x10,
        "嗯嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "现在借给你们的照相机\x01",
            "也请在那时还给我。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 400)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 400)
    OP_92(0x10, 0x101, 0x2BC, 0x7D0, 0x0)
    Sleep(400)

    ChrTalk(    #92
        0x10,
        "那么，拜托你们了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x1F\x32\x02\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x232, 1)
    Sleep(400)
    OP_8F(0x10, 0xFFFF4B3B, 0x0, 0x1108, 0x3E8, 0x0)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #94
        0x101,
        "#1016F好、好大啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_120C")

    ChrTalk(    #95
        0x127,
        (
            "#150F嗯～因为是拍摄\x01",
            "记录照片的高级机型嘛～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 400)

    ChrTalk(    #96
        0x101,
        "#1011F咦，是很好的相机吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x127,
        (
            "#151F嘿嘿，真是\x01",
            "坦率的好孩子啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x101,
        "#1007F好、好孩子……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1231")

    label("loc_120C")


    ChrTalk(    #99
        0x10,
        (
            "那当然啦。\x01",
            "是机械部件的组合嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1231")


    ChrTalk(    #100
        0x10,
        (
            "啊，感光结晶回路\x01",
            "已经设置好了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        (
            "只要按下快门\x01",
            "就可以了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1000F嗯，了解。\x02\x03",

            "#1015F那，再确认一次\x01",
            "工作内容……\x02\x03",

            "到『绀碧之塔』的塔顶上去，\x01",
            "拍下那里的『装置』……\x02\x03",

            "然后再返回这里，\x01",
            "归还这个相机就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        "嗯嗯，就按这个程序走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        "啊，还有一点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "尽量避免设计的角度，\x01",
            "照片的构图麻烦简单一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "怎么说都是资料用的照片，\x01",
            "可以的话请从正面拍摄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1000F避免设计的角度\x01",
            "简单点就好？\x02\x03",

            "#1000F……原来如此，明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "等你们的好照片。\x01",
            "那么，请小心注意吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    Return()

    # Function_3_62F end

    def Function_4_1427(): pass

    label("Function_4_1427")


    ChrTalk(    #109
        0x10,
        (
            "嗯，大致的情况\x01",
            "已经说明了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1011F嗯，已经听过了。\x02\x03",

            "#1015F以防万一，还是\x01",
            "确认一下……\x02\x03",

            "到『绀碧之塔』的塔顶上去，\x01",
            "拍下那里的『装置』……\x02\x03",

            "然后再返回这里，\x01",
            "归还借的照相机就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        "嗯嗯，就按这个程序吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        "那么请拿好照相机。\x02",
    )

    CloseMessageWindow()
    OP_92(0x10, 0x101, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #113
        "\x1F\x32\x02\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x232, 1)
    Sleep(400)
    OP_8F(0x10, 0xFFFF4B3B, 0x0, 0x1108, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #114
        0x10,
        "那么，请小心注意吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        "期待你们的照片哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1006F嗯，我们走了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 346, 0)
    Return()

    # Function_4_1427 end

    def Function_5_15E4(): pass

    label("Function_5_15E4")

    Call(2, 7)

    ChrTalk(    #117
        0x10,
        "哎呀，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "【确认工作内容】\x01",      # 0
            "【取消委托】\x01",          # 1
            "【没什么】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1676"),
        (1, "loc_177E"),
        (SWITCH_DEFAULT, "loc_18DC"),
    )


    label("loc_1676")


    ChrTalk(    #118
        0x10,
        (
            "希望你们拍摄的，\x01",
            "是在『绀碧之塔』塔顶上\x01",
            "像台座一样形状的『装置』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        (
            "『绀碧之塔』在阿伊纳街道途中\x01",
            "向南拐弯的岔道前面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10,
        (
            "照片要避开设计的角度，\x01",
            "构图麻烦简单一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        "毕竟是资料用的东西嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10,
        (
            "如果顺利拍摄好了，\x01",
            "再请返回这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x10,
        "那么，请当心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_177E")

    OP_28(0x66, 0x3, 0x8)
    OP_28(0x66, 0x1, 0x4000)

    ChrTalk(    #124
        0x101,
        (
            "#1007F抱歉，稍微\x01",
            "有点事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        (
            "哎呀呀……\x01",
            "要取消委托吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x10,
        "嗯～真是遗憾。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1000F总之，\x01",
            "先归还照相机吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #128
        "\x1F\x32\x02\x07\x00归还了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x232, 1)
    Sleep(400)
    OP_8F(0x101, 0xFFFF4F84, 0x0, 0xE42, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #129
        0x10,
        (
            "事情办完了\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "但是，请赶快哟。\x01",
            "还有下一项调查计划呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_18DC")


    ChrTalk(    #132
        0x10,
        (
            "『装置』的原形还不明。\x01",
            "请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1908")

    label("loc_1908")

    Call(2, 8)
    Return()

    # Function_5_15E4 end

    def Function_6_190D(): pass

    label("Function_6_190D")

    Call(2, 7)

    ChrTalk(    #133
        0xFE,
        (
            "哦哦，诸位。\x01",
            "正等着你们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "照片拍好了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1001F嗯，顺利完成了。\x02\x03",

            "#1011F啊，对了。\x01",
            "首先得归还照相机。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0x10, 0x2BC, 0x7D0, 0x0)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #136
        "\x1F\x32\x02\x07\x00归还了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x232, 1)
    Sleep(400)
    OP_8F(0x101, 0xFFFF4F84, 0x0, 0xE42, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #137
        0xFE,
        "……嗯，确实。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "那么，走吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1004F咦……？\x02\x03",

            "要去哪里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "当然是\x01",
            "导力器工房啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "得去冲洗\x01",
            "感光结晶回路才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016F啊～是这么回事啊。\x02\x03",

            "#1006F嗯，那么\x01",
            "马上去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2120   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_190D end

    def Function_7_1AD1(): pass

    label("Function_7_1AD1")

    Fade(1000)
    OP_6D(-45110, 0, 4019, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x26)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B05")
    SetChrPos(0x127, -43820, 0, 3580, 307)

    label("loc_1B05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B23")
    SetChrPos(0x104, -43810, 0, 2360, 299)

    label("loc_1B23")

    SetChrPos(0x101, -45180, 0, 3650, 289)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B4F")
    SetChrPos(0x106, -44880, 0, 2770, 280)
    Jump("loc_1B67")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1B67")
    SetChrPos(0x103, -44880, 0, 2770, 280)

    label("loc_1B67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x8)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B88")
    TurnDirection(0x10, 0x101, 0)

    label("loc_1B88")

    OP_0D()
    Return()

    # Function_7_1AD1 end

    def Function_8_1B8A(): pass

    label("Function_8_1B8A")

    OP_30(0x0)
    OP_8C(0x10, 346, 0)
    Return()

    # Function_8_1B8A end

    SaveToFile()

Try(main)
