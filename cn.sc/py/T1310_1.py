from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1310_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1310_1 ._SN',
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
        "Function_1_1FC3",         # 01, 1
        "Function_2_1FDD",         # 02, 2
        "Function_3_1FF7",         # 03, 3
        "Function_4_200E",         # 04, 4
        "Function_5_2088",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 82350, 0, 53600, 180)
    SetChrPos(0x106, 83210, 0, 53720, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105")
    SetChrPos(0x105, 82610, 0, 54630, 180)
    SetChrPos(0xF9, 81580, 0, 54720, 180)
    Jump("loc_159")

    label("loc_105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137")
    SetChrPos(0x105, 82610, 0, 54630, 180)
    SetChrPos(0xF8, 81580, 0, 54720, 180)
    Jump("loc_159")

    label("loc_137")

    SetChrPos(0xF8, 82610, 0, 54630, 180)
    SetChrPos(0xF9, 81580, 0, 54720, 180)

    label("loc_159")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_175")
    SetChrPos(0xC, 82940, 0, 52010, 0)

    label("loc_175")

    OP_4A(0xC, 255)
    OP_6D(82800, 0, 53860, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(35000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    OP_28(0x7A, 0x1, 0x8)

    ChrTalk(    #0
        0xC,
        (
            "呼，总算\x01",
            "来到关所了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "就一直待在这里\x01",
            "绝对不能回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xC,
        (
            "如果\x01",
            "不安排人来迎接我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1004F#1P（啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_318")

    ChrTalk(    #4
        0x105,
        (
            "#042F#5P（那是……芙拉瑟小姐呢。）\x02\x03",

            "#045F（想、想不到她\x01",
            "　竟然会来到这里……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x106,
        (
            "#050F#2P（是王立学院的学生呢……）\x02\x03",

            "（她就是那个要\x01",
            "　逃避相亲的『大小姐』吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1002F#1P（嗯、嗯……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_393")

    label("loc_318")


    ChrTalk(    #7
        0x106,
        (
            "#050F#2P（看上去就像是\x01",
            "　王立学院的学生呢。\x02\x03",

            "（她就是那个要\x01",
            "　逃避相亲的『大小姐』吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002F#1P（嗯、嗯……）\x02",
    )

    CloseMessageWindow()

    label("loc_393")

    OP_8C(0xC, 0, 400)

    ChrTalk(    #9
        0xC,
        "#4P哎呀，你们是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_497")

    ChrTalk(    #10
        0x101,
        (
            "#1016F#1P那个，好久不见……\x02\x03",

            "……别来无恙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xC,
        "#4P嗯，我很好啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xC,
        (
            "#4P以前我们在王立\x01",
            "学院见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        "#040F#5P你好，芙拉瑟小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        (
            "#4P哎呀……\x01",
            "科洛丝也在！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        "#4P你们到底为什么会来到这里？\x02",
    )

    CloseMessageWindow()
    Jump("loc_51A")

    label("loc_497")


    ChrTalk(    #16
        0x101,
        (
            "#1000F#1P那个，好久不见……\x02\x03",

            "……别来无恙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "#4P嗯，以前我们在王立\x01",
            "学院见过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "#4P各位今天到底为什么\x01",
            "会来到这里？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A")

    Jump("loc_556")

    label("loc_51D")


    ChrTalk(    #19
        0xC,
        "#4P哎呀，各位……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xC,
        (
            "#4P你们又来了，\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_556")


    ChrTalk(    #21
        0x101,
        (
            "#1000F#1P嗯，的确有个紧急的\x01",
            "委托。\x02\x03",

            "#1015F其实我们是来\x01",
            "找芙拉瑟小姐帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xC,
        "#4P找……我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "#4P那我究竟要\x01",
            "做什么才好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F#1P很简单啊。\x02\x03",

            "#1002F希望你和我们一起……\x01",
            "返回柏斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_96(0xC, 0x144C4, 0x0, 0xC8F0, 0x1F4, 0x2710)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_678")

    ChrTalk(    #25
        0x105,
        "#044F芙拉瑟小姐！？\x02",
    )

    CloseMessageWindow()

    label("loc_678")


    ChrTalk(    #26
        0xC,
        "#4P你、你们──\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        (
            "#4P#3S应该……\x01",
            "是蕾娜的爪牙吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#1P爪、爪牙……\x02\x03",

            "请不要把我们说得像是\x01",
            "恶势力一样。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(    #29
        0x105,
        "#045F#5P真、真是的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_802")

    label("loc_72E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_758")

    ChrTalk(    #30
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_802")

    label("loc_758")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A7")

    ChrTalk(    #31
        0x104,
        (
            "#035F呼，太伤人心了。\x02\x03",

            "我明明一直都是\x01",
            "站在女士这一边的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_802")

    label("loc_7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_802")

    ChrTalk(    #32
        0x108,
        (
            "#070F呵呵，因为有两个\x01",
            "大男人在呢。\x02\x03",

            "在对方看来，\x01",
            "爪牙可能就是这样的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_802")


    ChrTalk(    #33
        0x106,
        (
            "#551F#2P喂喂，大小姐。\x01",
            "在学校没学过吗？\x02\x03",

            "我们游击士都是中立的。\x01",
            "既不是谁的爪牙也不是谁的手下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        (
            "#4P嗯、嗯……\x01",
            "我当然知道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "#4P但我不会被这种\x01",
            "冠冕堂皇的话所欺骗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xC,
        (
            "#4P嘴上这么说，最后还是要\x01",
            "用武力带我回去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        (
            "#057F#2P这就要看你的态度了。\x02\x03",

            "如果不想被那样对待，\x01",
            "就乖乖听我们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x144C4, 0x0, 0xD016, 0x7D0, 0x0)
    TurnDirection(0x106, 0xC, 0)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0xC, 0xB4, 0x64, 0x3E8, 0x0)

    ChrTalk(    #38
        0xC,
        "#4P别、别过来！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "#4P你再靠近我就\x01",
            "喊人了！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1002F#1P你、你冷静点。\x02\x03",

            "没事的，我们什么也不会做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x106,
        (
            "#552F#2P真是的……\x01",
            "好一个会大惊小怪的大小姐。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #42
        0x101,
        "#1007F#1P阿加特你也稍微等等。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Sleep(1000)
    OP_94(0x1, 0x101, 0x0, 0x15E, 0x3E8, 0x0)
    Sleep(1000)

    ChrTalk(    #43
        0x101,
        (
            "#1002F#1P那个，芙拉瑟小姐你听我说。\x02\x03",

            "我们是来\x01",
            "保护你的。\x02\x03",

            "#1003F我知道你无法\x01",
            "接受相亲的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xC,
        "#4P当然，不可原谅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        (
            "#4P但是，更让我感到\x01",
            "不可原谅的是蕾娜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1002F#1P……什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "#4P她……\x01",
            "居然背叛了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xC,
        (
            "#4P本来这次来柏斯的\x01",
            "目的应该是旅游的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        (
            "#4P虽然经常路过那座城市，\x01",
            "但是却没来旅行过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xC,
        (
            "#4P所以我很期待\x01",
            "这次的旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "#4P可是来了以后等着我的\x01",
            "却是相亲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "#4P蕾娜一开始就准备\x01",
            "欺骗我呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015F#1P原来如此，之前\x01",
            "就一直瞒着你啊。\x02\x03",

            "#1002F但这样一来岂不是\x01",
            "更应该返回城里了吗？\x02\x03",

            "你应该向蕾娜小姐\x01",
            "说出真实的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xC,
        (
            "#4P这、这个……\x01",
            "绝对不可能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xC,
        (
            "#4P我根本就不想\x01",
            "再见到蕾娜了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        (
            "#1019F#1P（呼，唔……\x01",
            "这样下去好像很麻烦呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x106, 270, 400)

    ChrTalk(    #57
        0x106,
        (
            "#552F#2P（喂…………）\x02\x03",

            "（你要跟她说这些\x01",
            "  说到什么时候啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1016F#1P（再、再稍微等等。）\x02\x03",

            "（我再劝劝她……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    TurnDirection(0x106, 0xC, 400)

    ChrTalk(    #59
        0x101,
        (
            "#1002F#1P我说，芙拉瑟小姐。\x02\x03",

            "你无～论如何\x01",
            "都不愿意返回城里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        "#4P嗯，我没那个打算。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xC,
        (
            "#4P只要还是和蕾娜一起参加相亲，\x01",
            "我就不准备返回柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1007F#1P是，是吗……\x02\x03",

            "唉，真是的…\x01",
            "我们说什么你都听不进去，不过……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【芙拉瑟小姐真是个顽固的人呢】\x01",      # 0
            "【芙拉瑟小姐真是个胆小鬼呢】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EF")

    ChrTalk(    #63
        0x101,
        "#1007F#1P……芙拉瑟小姐真是个顽固的人呢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #64
        0xC,
        (
            "#4P我说，你们才\x01",
            "是顽固的人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xC,
        (
            "#4P就算是游击士，\x01",
            "也不能不考虑别人的感受吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xC,
        (
            "#4P难道你们要把自己的\x01",
            "道理强加于人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#1013F#1P我、我们\x01",
            "可没这么想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xC,
        "#4P那就不要管我了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xC,
        (
            "#4P你们老缠着我不放的话\x01",
            "我可真的要喊人了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #70
        0x101,
        "#1008F#1P啊、啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x106,
        (
            "#053F#2P呼，说服失败。\x02\x03",

            "#057F真是太\x01",
            "浪费时间了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x144C4, 0x0, 0xCB48, 0x7D0, 0x0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #72
        0xC,
        "#4P呀！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xC,
        "#4P你、你们要干什么！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x106,
        (
            "#057F#2P根据规约第二项的但书，\x01",
            "对你进行强制保护。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F#1P规约的第二项……\x01",
            "我记得是『民间人士保护』吧。\x02\x03",

            "……可那个『但书』是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        (
            "#053F#2P嗯，那是条约中的\x01",
            "特例措施。\x02\x03",

            "它规定了非常时期\x01",
            "可以强制执行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1004F#1P还、还有这一条啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        "#4P太、太乱来了！\x02",
    )

    CloseMessageWindow()

    def lambda_1213():
        OP_8E(0xC, 0x144C4, 0x0, 0xC544, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1213)
    Sleep(200)
    OP_8E(0x106, 0x144C4, 0x0, 0xC79C, 0xBB8, 0x0)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xC, 0x32, 0x0, 0x1F4, 0x7D0)

    ChrTalk(    #79
        0xC,
        (
            "#4P#3S你、你要干什么！！\x01",
            "放开我！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#053F#2P这是合法的措施。\x01",
            "你再哭再闹也没用。\x02\x03",

            "好了，赶快走吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12E9():

        label("loc_12E9")

        TurnDirection(0x101, 0x106, 400)
        OP_48()
        Jump("loc_12E9")

    QueueWorkItem2(0x101, 1, lambda_12E9)

    def lambda_12FA():

        label("loc_12FA")

        TurnDirection(0xF8, 0x106, 400)
        OP_48()
        Jump("loc_12FA")

    QueueWorkItem2(0xF8, 1, lambda_12FA)

    def lambda_130B():

        label("loc_130B")

        TurnDirection(0xF9, 0x106, 400)
        OP_48()
        Jump("loc_130B")

    QueueWorkItem2(0xF9, 1, lambda_130B)
    OP_43(0x106, 0x0, 0x1, 0x4)
    OP_43(0xC, 0x0, 0x1, 0x5)
    OP_43(0x101, 0x0, 0x1, 0x1)
    OP_43(0xF9, 0x2, 0x1, 0x3)

    ChrTalk(    #81 op#A op#5
        0xC,
        "#18A有、有人吗！！\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82 op#A op#5
        0xC,
        "#22A救命啊～有人要绑架我～！！\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83 op#A op#5
        0x106,
        "#054F#23A喂，别说话，快走。\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0xC, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(80870, 0, 54440, 2500)

    ChrTalk(    #84
        0x101,
        (
            "#1016F嗯、嗯……\x01",
            "要和她一起返回山道吗？\x02\x03",

            "#1007F唉，感觉路上会有事发生…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xC,
        "#2P啊啊啊，放开我！！\x02",
    )

    CloseMessageWindow()
    OP_22(0x97, 0x0, 0x64)

    ChrTalk(    #86
        0x106,
        "#2P喂、喂喂，别捣乱！！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #87
        0xC,
        "士兵的声音",
        "#2P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0xC,
        "士兵的声音",
        "#2P莫、莫非是绑架！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C5")

    ChrTalk(    #89
        0x108,
        "#070F哈哈，真是个有活力的大小姐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_14C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FD")

    ChrTalk(    #90
        0x103,
        "#021F呵呵，真是个有活力的大小姐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_14FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1543")

    ChrTalk(    #91
        0x105,
        (
            "#045F不、不愧是芙拉瑟小姐……\x02\x03",

            "正在拼命抵抗呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158D")

    label("loc_1543")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158D")

    ChrTalk(    #92
        0x104,
        (
            "#031F哈哈哈。\x01",
            "不愧是帝国的大小姐。\x02\x03",

            "确实是只难驯之马。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158D")


    ChrTalk(    #93
        0x101,
        (
            "#1019F总、总之我们上去帮忙吧。\x02\x03",

            "放任不管的话\x01",
            "会有大麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15D4():
        OP_6D(80870, 10000, 54440, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_15D4)
    OP_28(0x7A, 0x1, 0x20)
    Jump("loc_1FA4")

    label("loc_15EF")


    ChrTalk(    #94
        0x101,
        "#1007F#1P……芙拉瑟小姐真是个胆小鬼呢。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #95
        0xC,
        "#4P胆、胆小鬼……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xC,
        (
            "#4P你、你刚才……\x01",
            "说我是胆小鬼？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1015F#1P嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xC,
        (
            "#4P我哪里\x01",
            "胆小了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xC,
        "#4P希望你解释一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1002F#1P因为，你刚才虽然\x01",
            "说了很多理由……\x02\x03",

            "可是到头来还是\x01",
            "在害怕相亲吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0xC,
        "#4P我、我没害怕！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1002F#1P那就赶紧回\x01",
            "柏斯不就好了。\x02\x03",

            "虽然你想把相亲的事\x01",
            "怪罪在蕾娜小姐头上……\x02\x03",

            "可是她也不是自己\x01",
            "愿意那么做的。\x02\x03",

            "如果你试着站在蕾娜小姐的立场上\x01",
            "考虑问题的话就能很容易地明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xC,
        "#4P这、这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1010F#1P可是你却以此为借口\x01",
            "来逃避相亲。\x02\x03",

            "人的一生中会遇到\x01",
            "很多不合理或者令人痛苦的事。\x02\x03",

            "#1002F因为讨厌而逃避就\x01",
            "永远也无法前进。\x02\x03",

            "就因为你是这样的胆小鬼，\x01",
            "所以蕾娜小姐才对你撒了谎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xC,
        (
            "#4P这、这个……\x01",
            "这些我都知道！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xC,
        (
            "#4P#3S嗯！！\x01",
            "你说得没错！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #107
        0xC,
        (
            "#4P#3S所以我才无法\x01",
            "原谅蕾娜！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1020F#1P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xC,
        (
            "#4P蕾娜虽然平时\x01",
            "总是夸我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xC,
        (
            "#4P#3S可是有这种大事的时候\x01",
            "她还是不相信我！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_19CC():

        label("loc_19CC")

        TurnDirection(0x106, 0xC, 400)
        OP_48()
        Jump("loc_19CC")

    QueueWorkItem2(0x106, 1, lambda_19CC)

    def lambda_19DD():
        OP_92(0xC, 0x101, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_19DD)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #111
        0xC,
        (
            "#4P真正的朋友应该\x01",
            "互相信任，对吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)

    def lambda_1A24():
        OP_92(0xC, 0x101, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A24)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #112
        0xC,
        (
            "#4P那个？艾丝蒂尔小姐。\x01",
            "朋友就应该是那样的吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1A89():
        OP_92(0xC, 0x101, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A89)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x3E8, 0x0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #113
        0xC,
        (
            "#4P#3S我有什么地方\x01",
            "说错了吗？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    WaitChrThread(0xC, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B21")

    ChrTalk(    #114
        0x105,
        "#043F#5P芙拉瑟小姐……\x02",
    )

    CloseMessageWindow()

    label("loc_1B21")


    ChrTalk(    #115
        0x101,
        (
            "#1008F#1P等、等等……\x02\x03",

            "别、别那么兴奋啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xC,
        "#4P呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x106,
        (
            "#053F#2P……嗯，原来如此。\x02\x03",

            "你也有很多的\x01",
            "疑问呢……\x02\x03",

            "#050F可是你是不是\x01",
            "把质问的对象搞错了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        "#4P……呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xC,
        "是啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        "#4P……也许你们是对的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xC,
        (
            "#4P这份怒气应该\x01",
            "保留给蕾娜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1011F#1P啊，那就是说……\x02\x03",

            "你愿意回去了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xC,
        "#4P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "#4P把胸中的怒气宣泄出来，\x01",
            "心情舒服多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xC,
        (
            "#4P总之……\x01",
            "先回城里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "#4P我必须要告诉蕾娜\x01",
            "她有多伤我的心。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D14")

    ChrTalk(    #127
        0x105,
        (
            "#542F#5P呼……\x02\x03",

            "太好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D44")

    ChrTalk(    #128
        0x103,
        "#020F呵呵，轻松一点了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1D44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA0")

    ChrTalk(    #129
        0x108,
        (
            "#070F哈哈，你看上去像是\x01",
            "除去了一块心病。\x02\x03",

            "怎么样？\x01",
            "平静下来一点了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD4")

    label("loc_1DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD4")

    ChrTalk(    #130
        0x104,
        (
            "#030F怎么样？\x01",
            "平静下来一点了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD4")


    ChrTalk(    #131
        0xC,
        "#4P嗯，多少有点……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xC,
        (
            "#4P总之，我有勇气\x01",
            "来面对相亲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1001F#1P嘿嘿，那就好⊙\x02\x03",

            "#1017F对不起，我说了很多\x01",
            "很不客气的话。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xC,
        "#4P不，我才是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xC,
        (
            "#4P好了，各位。\x01",
            "那么我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xC,
        (
            "#4P归途的护卫工作……\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(    #137
        0x108,
        "#070F嗯，你就放心吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_1EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1F")

    ChrTalk(    #138
        0x104,
        (
            "#031F呵呵，我非常乐意\x01",
            "保护你。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F47")

    ChrTalk(    #139
        0x103,
        "#525F嗯，请放心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F68")

    label("loc_1F47")


    ChrTalk(    #140
        0x101,
        "#1006F#1P嗯，就交给我们吧⊙\x02",
    )

    CloseMessageWindow()

    label("loc_1F68")


    ChrTalk(    #141
        0x106,
        "#051F#2P好了，那就走吧。\x02",
    )

    CloseMessageWindow()

    def lambda_1F8C():
        OP_6D(82800, 10000, 53860, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1F8C)
    OP_28(0x7A, 0x1, 0x10)

    label("loc_1FA4")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1131   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_1FC3(): pass

    label("Function_1_1FC3")

    Sleep(200)
    OP_8F(0x101, 0x144D8, 0x0, 0xD2BE, 0x7D0, 0x0)
    Return()

    # Function_1_1FC3 end

    def Function_2_1FDD(): pass

    label("Function_2_1FDD")

    Sleep(400)
    OP_8F(0xF8, 0x13470, 0x0, 0xD5D4, 0x7D0, 0x0)
    Return()

    # Function_2_1FDD end

    def Function_3_1FF7(): pass

    label("Function_3_1FF7")

    Sleep(1000)
    OP_6D(78140, 0, 53020, 3000)
    Return()

    # Function_3_1FF7 end

    def Function_4_200E(): pass

    label("Function_4_200E")

    OP_8E(0x106, 0x144C4, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_8E(0x106, 0x1426C, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_A6(0x6)
    OP_8E(0x106, 0x124F8, 0x0, 0xCE2C, 0x7D0, 0x0)

    def lambda_2053():
        OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2053)
    OP_8E(0x106, 0x11FE4, 0x0, 0xCE2C, 0x7D0, 0x0)
    OP_8E(0x106, 0x11BFC, 0x0, 0xCE2C, 0x7D0, 0x0)
    Return()

    # Function_4_200E end

    def Function_5_2088(): pass

    label("Function_5_2088")

    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xC, 0x40)
    OP_8F(0xC, 0x144C4, 0x0, 0xCB48, 0x7D0, 0x0)
    OP_8F(0xC, 0x144C4, 0x0, 0xCF08, 0x7D0, 0x0)
    OP_A2(0x6)
    OP_8C(0xC, 90, 0)
    OP_8F(0xC, 0x124F8, 0x0, 0xCE2C, 0x7D0, 0x0)

    def lambda_20EB():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20EB)
    OP_8F(0xC, 0x11FE4, 0x0, 0xCE2C, 0x7D0, 0x0)
    Return()

    # Function_5_2088 end

    SaveToFile()

Try(main)
