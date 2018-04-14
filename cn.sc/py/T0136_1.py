from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0136_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0136_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
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
        "Function_1_4A7",          # 01, 1
        "Function_2_67E",          # 02, 2
        "Function_3_E5F",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_8C(0xB, 270, 0)
    Fade(1000)
    SetChrPos(0x101, -84710, 0, 119250, 270)
    SetChrPos(0x103, -85200, 0, 120650, 225)
    SetChrPos(0xF8, -83460, 0, 119250, 270)
    SetChrPos(0xF9, -83730, 0, 120510, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -83460, 0, 119250, 270)
    SetChrPos(0xF8, -83730, 0, 120510, 225)

    label("loc_12B")

    OP_6D(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_176")
    OP_A2(0x4)

    label("loc_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过【小猫的搜索】】\x01",        # 0
            "【◇没完成过【小猫的搜索】】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EA"),
        (1, "loc_1F0"),
        (SWITCH_DEFAULT, "loc_1F6"),
    )


    label("loc_1EA")

    OP_A2(0x4)
    Jump("loc_1F6")

    label("loc_1F0")

    OP_A3(0x4)
    Jump("loc_1F6")

    label("loc_1F6")


    ChrTalk(    #0
        0xB,
        (
            "真是的～\x01",
            "怎么办～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #1
        0xB,
        (
            "……咦～～？\x01",
            "你们是～～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_285")

    ChrTalk(    #2
        0x101,
        (
            "#1006F好久不见。\x02\x03",

            "是看了公告板而来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BD")

    label("loc_285")


    ChrTalk(    #3
        0x101,
        (
            "#1000F嗯，我们是看了告示板来的。\x02\x03",

            "您就是伊娜女士？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD")


    ChrTalk(    #4
        0xB,
        (
            "哎呀，麻烦你们了，\x01",
            "这么晚还过来～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "开门见山～～\x01",
            "能不能帮我寻找安莉尔～～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_378")

    ChrTalk(    #6
        0x101,
        (
            "#1004F安、安莉尔……\x02\x03",

            "#1016F那只猫……\x01",
            "又走失了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "怎么样～～？\x01",
            "你们愿意帮忙吗～～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_378")

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
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    Call(1, 2)
    Jump("loc_4A4")

    label("loc_3D0")


    ChrTalk(    #8
        0x101,
        (
            "#1015F抱歉啊，现在不行。\x01",
            "手头还有点事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        "哎呀，这就不好办了～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "可是可是，这是你们的工作，\x01",
            "也没办法哦～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        "#020F多谢您的理解。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1000F不过有空了\x01",
            "我们马上就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "嗯，拜托了～\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x8000)

    label("loc_4A4")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_4A7(): pass

    label("Function_1_4A7")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -84710, 0, 119250, 270)
    SetChrPos(0x103, -85200, 0, 120650, 225)
    SetChrPos(0xF8, -83460, 0, 119250, 270)
    SetChrPos(0xF9, -83730, 0, 120510, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_521")
    SetChrPos(0xF9, -83460, 0, 119250, 270)
    SetChrPos(0xF8, -83730, 0, 120510, 225)

    label("loc_521")

    TurnDirection(0xB, 0x101, 0)
    OP_6D(-85090, 0, 119630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #14
        0xB,
        "哎呀～～游击士小姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "愿意帮我寻找\x01",
            "安莉尔了吗～？\x02",
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
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F9")
    Call(1, 2)
    Jump("loc_67B")

    label("loc_5F9")


    ChrTalk(    #16
        0x101,
        (
            "#1015F抱歉啊，现在不行。\x01",
            "还有点事情…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        "哎呀～～是吗～～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1000F有了时间的话\x01",
            "我们马上就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        "嗯，拜托了～\x02",
    )

    CloseMessageWindow()

    label("loc_67B")

    EventEnd(0x0)
    Return()

    # Function_1_4A7 end

    def Function_2_67E(): pass

    label("Function_2_67E")


    ChrTalk(    #20
        0x101,
        (
            "#1000F嗯……现在算是ＯＫ了哟。\x02\x03",

            "#1015F虽然对现在来做这件事\x01",
            "合不合适有些疑惑……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #21
        0x103,
        (
            "#026F不过处理细小事件\x01",
            "也是游击士的重要责任啊。\x02\x03",

            "#027F我们会尽力帮助你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "嗯～这就足够了～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xB, 400)

    ChrTalk(    #23
        0x103,
        (
            "#020F那就请你重新说明\x01",
            "一下委托的内容吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CE")

    ChrTalk(    #24
        0x106,
        (
            "#050F你好像在\x01",
            "寻找一只猫呢。\x02\x03",

            "就是刚才提到的\x01",
            "那只名叫安莉尔的猫吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_7CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_828")

    ChrTalk(    #25
        0x108,
        (
            "#070F你好像在\x01",
            "寻找一只猫呢。\x02\x03",

            "就是刚才提到的\x01",
            "那只名叫安莉尔的猫吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_828")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_884")

    ChrTalk(    #26
        0x104,
        (
            "#030F你好像在寻找\x01",
            "一只猫呢……\x02\x03",

            "就是刚才提到的\x01",
            "那只名叫安莉尔的猫吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DB")

    label("loc_884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(    #27
        0x105,
        (
            "#040F你好像在\x01",
            "寻找一只猫呢。\x02\x03",

            "就是刚才提到的\x01",
            "那只名叫安莉尔的猫吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")


    ChrTalk(    #28
        0xB,
        (
            "嗯，是啊～～\x01",
            "就是在找安莉尔～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "我只是稍微午睡了一会儿。\x01",
            "它就不见了～～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_974")
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x101,
        "#1007F（完、完全和上次一样啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9D7")

    ChrTalk(    #31
        0x107,
        (
            "#064F就是说从中午以后\x01",
            "就一直没回来过？\x02\x03",

            "#063F那、那倒是\x01",
            "让人有点担心了呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC5")

    label("loc_9D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #32
        0x105,
        (
            "#043F就是说已经\x01",
            "半天没回来了……\x02\x03",

            "那倒是让人挺担心的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC5")

    label("loc_A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A78")

    ChrTalk(    #33
        0x104,
        (
            "#032F就是说……\x01",
            "已经失踪半天了。\x02\x03",

            "嗯，那倒是挺\x01",
            "让人担心的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC5")

    label("loc_A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC5")

    ChrTalk(    #34
        0x108,
        (
            "#074F就是说已经\x01",
            "失踪半天了？\x02\x03",

            "嗯，那倒是挺\x01",
            "有点令人担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC5")


    ChrTalk(    #35
        0x103,
        (
            "#022F您觉得它\x01",
            "会去哪里？\x02\x03",

            "能不能告诉我们它\x01",
            "平时经常去的地方？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #36
        0xB,
        "嗯～～不知道能不能算是线索～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "根据阿姨我的直觉\x01",
            "飞船坪好像很可疑～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1011F飞船坪！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #39
        0xB,
        (
            "听整备人员说\x01",
            "好像有人看到了猫～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "而且还是褐色的，\x01",
            "一定是安莉尔～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1002F是、是吗……\x02\x03",

            "#1015F呜…猫的毛色\x01",
            "记在手册上。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C51")

    ChrTalk(    #42
        0x108,
        (
            "#070F嗯，这可是条有用的线索。\x02\x03",

            "先从这条线\x01",
            "开始调查怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D33")

    label("loc_C51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9E")

    ChrTalk(    #43
        0x106,
        (
            "#051F这可是条有用的线索。\x02\x03",

            "先从这条线\x01",
            "开始调查也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D33")

    label("loc_C9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CED")

    ChrTalk(    #44
        0x104,
        (
            "#030F啊，这可是条有用的线索。\x02\x03",

            "先从这条线\x01",
            "开始查怎么样？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D33")

    label("loc_CED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D33")

    ChrTalk(    #45
        0x105,
        (
            "#040F……很有用的情报。\x02\x03",

            "那就先从这一点\x01",
            "开始调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D33")


    ChrTalk(    #46
        0x103,
        (
            "#020F嗯，这线索有调查的价值。\x02\x03",

            "总之我们先\x01",
            "去飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #47
        0x101,
        "#1006F嗯……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "看来我的说明\x01",
            "已经足够了～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "那么，阿姨我\x01",
            "就在这里等着～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xB,
        (
            "游击士们，\x01",
            "接下来就拜托你们了～～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #51
        0x101,
        "#1006F找到了我们会来报告的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#020F嗯，那就先这样。\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x1)
    OP_28(0x74, 0x1, 0x2)
    OP_28(0x74, 0x1, 0x4)
    OP_28(0x74, 0x4, 0x4)
    OP_28(0x74, 0x4, 0x8)
    OP_A2(0x3)
    Return()

    # Function_2_67E end

    def Function_3_E5F(): pass

    label("Function_3_E5F")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xB, -85600, 0, 119540, 90)
    SetChrPos(0xC, -85720, 0, 120310, 90)
    SetChrPos(0xF, -84190, 0, 123070, 330)
    SetChrPos(0xE, -83500, 580, 117300, 270)
    SetChrPos(0xD, -83030, 580, 116830, 315)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x3)
    OP_4A(0xB, 255)
    SetChrPos(0x101, -83980, 0, 119500, 270)
    SetChrPos(0x103, -83580, 0, 120500, 273)
    SetChrPos(0xF8, -82420, 0, 119000, 270)
    SetChrPos(0xF9, -82100, 0, 120000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F74")
    SetChrPos(0xF9, -82420, 0, 119000, 270)
    SetChrPos(0xF8, -82100, 0, 120000, 270)

    label("loc_F74")

    OP_6D(-85080, 0, 120200, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #53
        0xB,
        (
            "真是的～～\x01",
            "阿姨我可吓了一跳～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        (
            "我家的安莉尔竟然\x01",
            "做了妈妈回来了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1016F#3P我们才\x01",
            "大吃一惊呢。\x02\x03",

            "没想到会\x01",
            "变成这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#020F#2P总之肯定是\x01",
            "母子都平安了。\x02\x03",

            "今后也请好好\x01",
            "养育它们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "那是当然～～\x01",
            "因为它们是我重要的家人～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "可是可是～～\x01",
            "今后也不容易啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "为小猫们起名字\x01",
            "也是一项工作～～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112A")

    ChrTalk(    #60
        0x107,
        (
            "#560F请给它们起几个\x01",
            "可爱的名字。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DA")

    label("loc_112A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1165")

    ChrTalk(    #61
        0x105,
        (
            "#040F嗯，请给它们起几个\x01",
            "可爱的名字。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DA")

    label("loc_1165")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(    #62
        0x104,
        (
            "#030F呵呵，期待你给它们起几个\x01",
            "好听的名字。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DA")

    label("loc_11A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DA")

    ChrTalk(    #63
        0x108,
        (
            "#070F嗯，请给它们起几个\x01",
            "好名字。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x9, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_11E7")
    OP_A2(0x4)

    label("loc_11E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成过【小猫的搜索】】\x01",        # 0
            "【◇没完成过【小猫的搜索】】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_125B"),
        (1, "loc_1261"),
        (SWITCH_DEFAULT, "loc_1267"),
    )


    label("loc_125B")

    OP_A2(0x4)
    Jump("loc_1267")

    label("loc_1261")

    OP_A3(0x4)
    Jump("loc_1267")

    label("loc_1267")


    ChrTalk(    #64
        0xB,
        "嗯，交给我吧～～\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1434")

    ChrTalk(    #65
        0xB,
        (
            "啊～不过各位。\x01",
            "请稍微等一下再回去～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xB,
        (
            "还有事要\x01",
            "跟你们说～～\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1015F#3P请问还有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "嗯～因为这已经是第二次\x01",
            "受到游击士的帮助了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        "是的～请你们收下这个㈱\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #70
        "\x07\x00得到了\x1F\x57\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x157, 1)

    ChrTalk(    #71
        0xB,
        (
            "这是阿姨做礼拜时\x01",
            "喜欢用的物品～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xB,
        (
            "能让人心情平静下来，\x01",
            "所以请你们一定要用用看㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1011F#3P呵呵～是吗。\x02\x03",

            "#1000F嗯，谢谢。\x01",
            "那我们就不客气了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1434")


    ChrTalk(    #74
        0xB,
        (
            "那么，各位路上\x01",
            "也请小心～\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xC, 255)
    TurnDirection(0xC, 0x101, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #75
        0xC,
        "喵～～\x02",
    )

    CloseMessageWindow()
    OP_4A(0xD, 255)
    TurnDirection(0xD, 0x101, 400)
    OP_22(0x15C, 0x0, 0x64)

    ChrTalk(    #76
        0xD,
        "咪～～\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0101   ._SN", 116, 0, 0)
    IdleLoop()
    Return()

    # Function_3_E5F end

    SaveToFile()

Try(main)
