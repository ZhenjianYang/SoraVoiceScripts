from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3100   ._SN',
            'ED6_DT21/T3100_1 ._SN',
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
        "Function_1_8B2",          # 01, 1
        "Function_2_F21",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145")

    ChrTalk(    #0
        0x101,
        (
            "#1004F啊！\x02\x03",

            "这、这是……！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_117")

    ChrTalk(    #1
        0x106,
        "#052F发现什么了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_130")

    label("loc_117")


    ChrTalk(    #2
        0x103,
        "#023F发现什么了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_130")


    ChrTalk(    #3
        0x101,
        "#1002F嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_330")

    label("loc_145")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")

    ChrTalk(    #4
        0x106,
        (
            "#052F嗯！？\x02\x03",

            "这是……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1002F发现什么了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x106,
        "#050F嗯，来看看这个。\x02",
    )

    CloseMessageWindow()
    Jump("loc_330")

    label("loc_1A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216")

    ChrTalk(    #7
        0x103,
        (
            "#023F哎呀！？\x02\x03",

            "这莫非是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1002F发现什么了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#027F艾丝蒂尔……\x01",
            "来看看这个。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_330")

    label("loc_216")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266")

    ChrTalk(    #10
        0x105,
        (
            "#044F……！？\x02\x03",

            "艾丝蒂尔，这是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1002F发现什么了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_330")

    label("loc_266")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")

    ChrTalk(    #12
        0x104,
        "#033F呀…！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1002F奥利维尔，发现什么了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x104,
        "#035F嗯，来看看这个。\x02",
    )

    CloseMessageWindow()
    Jump("loc_330")

    label("loc_2C7")


    ChrTalk(    #15
        0x107,
        (
            "#064F咦！？\x02\x03",

            "这、这是……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1002F发现什么了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #17
        0x107,
        (
            "#062F嗯、嗯。\x02\x03",

            "姐姐，看看这个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_330")

    OP_59()
    Fade(1000)
    EventBegin(0x0)
    OP_6D(35000, 500, 87940, 0)
    OP_67(0, 8109, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(143000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 36310, 0, 87490, 280)
    SetChrPos(0xF7, 35950, 0, 86340, 310)
    SetChrPos(0xF8, 37540, 0, 85600, 329)
    SetChrPos(0xF9, 37230, 0, 84600, 328)
    OP_0D()
    Sleep(400)
    OP_8E(0x101, 0x88C2, 0x1F4, 0x157B6, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D")

    ChrTalk(    #18
        0x101,
        (
            "#1002F#7P……没错。\x02\x03",

            "是那家伙的卡片。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460")

    label("loc_40D")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #19
        0x101,
        (
            "#1002F#7P这、这张卡片……\x02\x03",

            "肯定是那家伙的东西了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(    #20
        0x106,
        "#050F那么，上面写着什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AD")

    label("loc_489")


    ChrTalk(    #21
        0x103,
        (
            "#022F那么……\x01",
            "上面写着些什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD")


    ChrTalk(    #22
        0x101,
        (
            "#1002F#7P嗯、嗯……\x01",
            "等一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)
    Fade(1000)
    OP_6D(36720, 0, 87530, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_71(0x16, 0x4)
    SetChrPos(0x101, 35000, 500, 87760, 270)
    SetChrPos(0xF8, 37880, 0, 87320, 270)
    SetChrPos(0xF7, 37790, 0, 86040, 315)
    SetChrPos(0xF9, 39170, 0, 86460, 270)
    OP_0D()
    Sleep(400)
    OP_8C(0x101, 90, 400)
    OP_8F(0x101, 0x8DFE, 0x0, 0x1548C, 0x7D0, 0x0)
    Fade(1000)
    SetChrChipByIndex(0x101, 11)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05　　美丽的公主及其随从啊　　\x01",
            "　　汝等所寻之物尚在远处\x02\x03",

            "　　第二把钥匙在中央工房 　　\x01",
            "　　调查『最聪明者』吧\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #24
        0x101,
        "#1002F#5P──看来以上就是接下来的提示了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6BE")

    ChrTalk(    #25
        0x106,
        (
            "#051F#3P原来如此……\x01",
            "就是说接下来是中央工房啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_6BE")


    ChrTalk(    #26
        0x103,
        (
            "#020F#3P原来如此……\x01",
            "就是说接下来是中央工房啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F3")


    ChrTalk(    #27
        0x101,
        (
            "#1002F#5P嗯，场所倒是知道了……\x02\x03",

            "这个『最聪明者』到底\x01",
            "是谁呢？\x02\x03",

            "#1007F不会是\x01",
            "拉赛尔博士吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_79B")

    ChrTalk(    #28
        0x106,
        (
            "#050F#3P总之那个东西在\x01",
            "中央工房就是了。\x02\x03",

            "去调查看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E2")

    label("loc_79B")


    ChrTalk(    #29
        0x103,
        (
            "#020F#3P总之那个东西在\x01",
            "中央工房就是了。\x02\x03",

            "那我们就快去参观参观吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80B")

    ChrTalk(    #30
        0x104,
        "#031F嗯，那么出发吧。\x02",
    )

    CloseMessageWindow()

    label("loc_80B")


    ChrTalk(    #31
        0x101,
        "#1006F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_64(0x3, 0x1)

    def lambda_82B():
        OP_8E(0x0, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_82B)

    def lambda_846():
        OP_8E(0x1, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_846)

    def lambda_861():
        OP_8E(0x2, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_861)

    def lambda_87C():
        OP_8E(0x3, 0x9902, 0x0, 0x151BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_87C)
    OP_69(0xF9, 0x3E8)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_6A(0xFF)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_8B2(): pass

    label("Function_1_8B2")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 58240, 0, 48320, 270)
    SetChrPos(0xF7, 59110, 0, 47500, 270)
    SetChrPos(0xF8, 59440, 0, 48970, 270)
    SetChrPos(0xF9, 60100, 0, 48320, 270)
    OP_6D(56710, 0, 46620, 0)
    OP_67(0, 7560, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #32
        0x101,
        (
            "#1011F#5P３根高低不同的烟囱……\x02\x03",

            "#1015F我说，你们不觉得『尖帽子三兄弟』\x01",
            "就是指这里吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_99D():
        OP_6D(52980, 0, 43380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_99D)
    OP_67(0, 10800, -10000, 2000)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A25")

    ChrTalk(    #33
        0x107,
        (
            "#060F#2P这里烟囱的高度\x01",
            "呈逐渐变化之势。\x02\x03",

            "#061F嘿嘿，感觉真的像\x01",
            "兄弟一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A72")

    label("loc_A25")


    ChrTalk(    #34
        0x105,
        (
            "#040F#2P３根的高度都有所不同呢。\x02\x03",

            "原来如此……\x01",
            "兄弟有可能指的就是这个。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(    #35
        0x106,
        (
            "#050F#1P有３根烟囱的建筑物\x01",
            "好像只此一家呢。\x02\x03",

            "有可能就是这儿。\x01",
            "调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B22")

    label("loc_ACC")


    ChrTalk(    #36
        0x103,
        (
            "#020F#1P有３根烟囱的建筑物\x01",
            "好像只此一家呢。\x02\x03",

            "我想有可能就是这儿。\x01",
            "快调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B22")

    OP_59()

    def lambda_B29():
        OP_6D(56710, 0, 46620, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B29)

    def lambda_B41():
        OP_8E(0x101, 0xDE30, 0x0, 0xBCC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B41)
    OP_6D(59550, 0, 47740, 2000)
    WaitChrThread(0x101, 0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #37
        (
            "\x07\x05在烟囱的管子下\x01",
            "发现贴着卡片。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #38
        0x101,
        "#1018F#5P好，找到了！\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_BCF():
        OP_6D(59080, 0, 48310, 2000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_BCF)

    def lambda_BE7():
        OP_67(0, 7560, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_BE7)

    def lambda_BFF():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_BFF)
    OP_8C(0x101, 90, 400)
    OP_8E(0x101, 0xE380, 0x0, 0xBCC0, 0x7D0, 0x0)

    def lambda_C2A():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C2A)

    def lambda_C38():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C38)

    def lambda_C46():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C46)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x13, 0x1)
    WaitChrThread(0x13, 0x2)
    WaitChrThread(0x13, 0x3)
    Fade(1000)
    SetChrChipByIndex(0x101, 11)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05　　 　门已经被打开了　　\x01",
            "　勇士们的灵魂眠于安静的地下\x02\x03",

            "　　 高声献唱给女神吧　　\x01",
            "　　『Ｃ－２６Ｄ－Ｅ』！　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(    #40
        0x101,
        (
            "#1007F#5P呼～看来\x01",
            "接下来就是最后一步了。\x02\x03",

            "#1015F不过，『安静的地下』和\x01",
            "『献唱给女神』……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1E")

    ChrTalk(    #41
        0x104,
        (
            "#032F唔，『安静的地下』\x01",
            "应该就是如字面意思的地方吧。\x02\x03",

            "问题是『女神』和后面的\x01",
            "意义不明的文字。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8D")

    label("loc_E1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8D")

    ChrTalk(    #42
        0x105,
        (
            "#042F『安静的地下』\x01",
            "应该就是如字面意思的地方吧……\x02\x03",

            "问题是『女神』和后面的\x01",
            "意义不明的文字。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8D")


    ChrTalk(    #43
        0x101,
        (
            "#1006F#5P总之，我们还是先去\x01",
            "『地下』吧。\x02\x03",

            "蔡斯的地下的话，\x01",
            "就只有那里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_F02")

    ChrTalk(    #44
        0x106,
        "#051F#1P嗯，快点去吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1E")

    label("loc_F02")


    ChrTalk(    #45
        0x103,
        "#020F#1P嗯，快点去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_F1E")

    EventEnd(0x0)
    Return()

    # Function_1_8B2 end

    def Function_2_F21(): pass

    label("Function_2_F21")

    EventBegin(0x0)
    SetChrPos(0xF, 28770, 0, 61520, 71)
    SetChrPos(0x101, 27390, 0, 60100, 71)
    SetChrPos(0xF7, 26830, 0, 61050, 61)
    SetChrPos(0xF8, 27120, 0, 59000, 71)
    SetChrPos(0xF9, 26310, 0, 59830, 71)
    ClearChrFlags(0xF, 0x80)
    OP_4A(0x9, 255)
    SetChrFlags(0x10, 0x8)
    OP_72(0x1, 0x4)
    OP_71(0x15, 0x4)
    OP_64(0x2, 0x1)
    OP_6D(29300, 10850, 62850, 0)
    OP_67(0, 5320, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(330000, 0)
    OP_6E(262, 0)

    def lambda_FD7():
        OP_6D(29300, 1900, 63800, 6000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_FD7)

    def lambda_FEF():
        OP_67(0, 5320, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_FEF)

    def lambda_1007():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1007)

    def lambda_1017():
        OP_6C(296000, 6000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_1017)
    OP_0D()
    Sleep(2000)
    WaitChrThread(0x13, 0x3)
    Sleep(2000)

    def lambda_1037():
        OP_6D(26280, 0, 60230, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1037)

    def lambda_104F():
        OP_6C(283000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_104F)

    def lambda_105F():
        OP_8C(0xF7, 61, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_105F)
    OP_8C(0xF, 250, 400)
    WaitChrThread(0x13, 0x3)

    ChrTalk(    #46
        0xF,
        (
            "#791F顺利地取回了呢。\x02\x03",

            "我就知道你们\x01",
            "能做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1006F能够不负你的期待真是太好了。\x02\x03",

            "#1007F不过这次又被\x01",
            "怪盗Ｂ给大大地耍了一把。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1157")

    ChrTalk(    #48
        0x106,
        (
            "#053F#2P嗯，感觉又一次\x01",
            "了解到他的厉害了。\x02\x03",

            "#050F说不定……\x01",
            "这才是他的目标。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11A8")

    label("loc_1157")


    ChrTalk(    #49
        0x103,
        (
            "#026F#2P嗯，感觉又一次\x01",
            "了解到他的厉害了。\x02\x03",

            "#022F说不定……\x01",
            "这才是他的目标。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A8")

    OP_8C(0x101, 307, 400)

    ChrTalk(    #50
        0x101,
        (
            "#1002F通过让我们见识他的实力\x01",
            "来威胁我们？\x02\x03",

            "#1015F不，我不认为他\x01",
            "考虑得这么深。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "#792F不管怎么说\x01",
            "敌人都不简单。\x02\x03",

            "#790F今后也要\x01",
            "谨慎行动。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1270")

    ChrTalk(    #52
        0x104,
        "#030F#1P嗯，这样比较好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1294")

    ChrTalk(    #53
        0x107,
        "#062F#1P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    label("loc_1294")

    OP_8C(0x101, 71, 400)
    Sleep(400)

    ChrTalk(    #54
        0x101,
        "#1002F嗯……是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xF,
        (
            "#791F好，这样一来这件委托就完成了……\x02\x03",

            "你们就继续去忙\x01",
            "你们本来的任务吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_132A")

    ChrTalk(    #56
        0x106,
        "#050F#2P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1344")

    label("loc_132A")


    ChrTalk(    #57
        0x103,
        "#020F#2P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_1344")


    ChrTalk(    #58
        0xF,
        "#790F那我就先告辞了。\x02",
    )

    CloseMessageWindow()

    def lambda_1365():

        label("loc_1365")

        TurnDirection(0x0, 0xF, 0)
        OP_48()
        Jump("loc_1365")

    QueueWorkItem2(0x0, 1, lambda_1365)

    def lambda_1376():

        label("loc_1376")

        TurnDirection(0x1, 0xF, 0)
        OP_48()
        Jump("loc_1376")

    QueueWorkItem2(0x1, 1, lambda_1376)

    def lambda_1387():

        label("loc_1387")

        TurnDirection(0x2, 0xF, 0)
        OP_48()
        Jump("loc_1387")

    QueueWorkItem2(0x2, 1, lambda_1387)

    def lambda_1398():

        label("loc_1398")

        TurnDirection(0x3, 0xF, 0)
        OP_48()
        Jump("loc_1398")

    QueueWorkItem2(0x3, 1, lambda_1398)
    OP_8E(0xF, 0x6932, 0x0, 0xF726, 0x7D0, 0x0)
    OP_8C(0xF, 0, 400)
    OP_70(0xC, 0x1D)
    OP_73(0xC)
    OP_8E(0xF, 0x6932, 0x0, 0xFD3E, 0x7D0, 0x0)
    OP_72(0xC, 0x800)
    OP_6F(0xC, 29)
    OP_70(0xC, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xC)
    OP_71(0xC, 0x800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x02任务【被盗的招牌板】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0xF, 0x80)
    OP_4B(0x9, 255)
    SetChrPos(0x10, 13900, 0, 58910, 227)
    ClearChrFlags(0x10, 0x8)
    EventEnd(0x0)
    Return()

    # Function_2_F21 end

    SaveToFile()

Try(main)
