from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3111_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3111_1 ._SN',
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
        "Function_1_D34",          # 01, 1
        "Function_2_D78",          # 02, 2
        "Function_3_DA8",          # 03, 3
        "Function_4_DD8",          # 04, 4
        "Function_5_E08",          # 05, 5
        "Function_6_1072",         # 06, 6
        "Function_7_11C0",         # 07, 7
        "Function_8_1FCF",         # 08, 8
        "Function_9_2063",         # 09, 9
        "Function_10_26DB",        # 0A, 10
        "Function_11_2A71",        # 0B, 11
        "Function_12_2EB3",        # 0C, 12
        "Function_13_3569",        # 0D, 13
        "Function_14_35C1",        # 0E, 14
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -116560, -4000, -111330, 180)
    SetChrPos(0xF7, -115650, -4000, -111150, 180)
    SetChrPos(0xF8, -116560, -4000, -110220, 180)
    SetChrPos(0xF9, -115500, -4000, -110020, 180)
    OP_8C(0xE, 0, 0)
    OP_4A(0xE, 0)
    OP_69(0x101, 0x0)
    OP_6D(-116200, -4000, -111770, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 3)), scpexpr(EXPR_END)), "loc_1E0")

    ChrTalk(    #0
        0x101,
        "#1011F菲小姐，打扰一下好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "哎呀，是你们啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "难道\x01",
            "是工作的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1006F嗯，算是吧。\x02\x03",

            "有事情想要问哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "咦，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "什么事，说说看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_366")

    label("loc_1E0")


    ChrTalk(    #6
        0xFE,
        "哎呀，是你们啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "好久不见，还好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1001F啊，菲小姐！\x02\x03",

            "#1000F嗯，真是好久不见了啊。\x01",
            "菲小姐最近怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "哈哈，我还是和以前一样\x01",
            "每天忙得要死。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2D5")

    ChrTalk(    #10
        0xFE,
        (
            "多亏你们，\x01",
            "我和布拉姆重新和好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "总之，感觉还算是很充实啦！\x02",
    )

    CloseMessageWindow()
    Jump("loc_304")

    label("loc_2D5")


    ChrTalk(    #12
        0xFE,
        (
            "这里的输出也很顺利，\x01",
            "地下工厂没有休息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_304")


    ChrTalk(    #13
        0xFE,
        (
            "你们也在\x01",
            "这里工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006F嗯，算是吧。\x02\x03",

            "跟你说，其实有件工作\x01",
            "想问你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "哎，什么？\x02",
    )

    CloseMessageWindow()

    label("loc_366")


    ChrTalk(    #16
        0x101,
        (
            "#1015F能不能\x01",
            "看一下这个？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #17
        (
            "\x07\x05把布卢布兰留下的\x01",
            "信息笔记给菲看。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #18
        0xFE,
        (
            "安静的地下……\x01",
            "女神……之后是字符串吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "……这怎么了？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_469")

    ChrTalk(    #20
        0x106,
        (
            "#050F好像是在\x01",
            "说这里……\x01",
            "但是有些地方搞不明白。\x02\x03",

            "想着你可能知道\x01",
            "就来找你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_469")


    ChrTalk(    #21
        0x103,
        (
            "#020F好像是在\x01",
            "说这个地方……\x01",
            "但是有些地方搞不明白。\x02\x03",

            "想着你可能知道\x01",
            "就来找你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF")


    ChrTalk(    #22
        0xFE,
        (
            "这些文字\x01",
            "是说地下工厂吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "那，那么可能是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002F想到什么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "这，这个女神\x01",
            "难道是说我！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x101,
        (
            "#1016F不，这个……\x02\x03",

            "实、实在抱歉\x01",
            "这个就别管了吧。\x02\x03",

            "先不说这个，\x01",
            "还有搞不明白的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #27
        0xFE,
        "啊……抱、抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "嗯，是这个字符串吧。\x01",
            "『Ｃ－２６Ｄ－Ｅ』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "看起来的感觉，像是管理用的\x01",
            "产品序号似的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1011F产品序号？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_701")

    ChrTalk(    #31
        0x107,
        (
            "#064F我也不太清楚……\x02\x03",

            "就是存放在仓库里的东西\x01",
            "所带的序号吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "嗯，仓库里的物品\x01",
            "全部都是用这个序号来管理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "所以只要知道序号\x01",
            "不管什么都能用传送带送出来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75F")

    label("loc_701")


    ChrTalk(    #34
        0xFE,
        (
            "嗯，这个序号是仓库里\x01",
            "所有物品都有的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "所以只要知道序号\x01",
            "不管什么都能用传送带送出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75F")


    ChrTalk(    #36
        0x101,
        (
            "#1015F这么说……\x01",
            "这个号码的东西也能送出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "当然能了。\x01",
            "要不试试看？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7D6")

    ChrTalk(    #38
        0x106,
        "#050F可以的话就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F5")

    label("loc_7D6")


    ChrTalk(    #39
        0x103,
        "#020F可以的话就麻烦你了。\x02",
    )

    CloseMessageWindow()

    label("loc_7F5")


    ChrTalk(    #40
        0xFE,
        (
            "小事一桩。\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_817():
        OP_6D(-114050, -4000, -110140, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_817)

    def lambda_82F():

        label("loc_82F")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_82F")

    QueueWorkItem2(0x101, 1, lambda_82F)

    def lambda_840():

        label("loc_840")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_840")

    QueueWorkItem2(0xF7, 1, lambda_840)

    def lambda_851():

        label("loc_851")

        TurnDirection(0xF8, 0xE, 400)
        OP_48()
        Jump("loc_851")

    QueueWorkItem2(0xF8, 1, lambda_851)

    def lambda_862():

        label("loc_862")

        TurnDirection(0xF9, 0xE, 400)
        OP_48()
        Jump("loc_862")

    QueueWorkItem2(0xF9, 1, lambda_862)
    OP_8E(0xFE, 0xFFFE3A40, 0xFFFFF060, 0xFFFE48F0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE4512, 0xFFFFF060, 0xFFFE4DC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0xE, 0x1)
    Sleep(400)

    ChrTalk(    #41
        0xFE,
        (
            "我是菲。\x01",
            "能打扰一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "产品序号Ｃ－２６Ｄ－Ｅ\x01",
            "麻烦送来这边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "对，Ｃ－２６Ｄ－Ｅ……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        "……谢了，拜托了哦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #45
        0xFE,
        "有那个号码的物品。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "说是现在就送来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1004F真、真的有吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "好像那边的负责人\x01",
            "也吓了一大跳呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "好～了，会有什么过来呢……\x02",
    )

    CloseMessageWindow()
    OP_22(0xA0, 0x1, 0x64)
    OP_76(0xFF, 0x16, 0x1, 0x2, 0x0, 0x3E8, 0x0, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)

    def lambda_9FF():
        OP_6D(-109200, -4000, -110660, 4000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_9FF)

    def lambda_A17():
        OP_67(0, 6920, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A17)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x1, 0x2)
    Sleep(600)
    OP_43(0x101, 0x1, 0x1, 0x1)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x1, 0x3)
    Sleep(1000)
    OP_43(0xF9, 0x1, 0x1, 0x4)
    WaitChrThread(0xF9, 0x1)
    OP_44(0xE, 0x0)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_43(0xE, 0x3, 0x1, 0xD)
    OP_A6(0x11)

    def lambda_A86():

        label("loc_A86")

        TurnDirection(0x0, 0x13, 400)
        OP_48()
        Jump("loc_A86")

    QueueWorkItem2(0x0, 1, lambda_A86)

    def lambda_A97():

        label("loc_A97")

        TurnDirection(0x1, 0x13, 400)
        OP_48()
        Jump("loc_A97")

    QueueWorkItem2(0x1, 1, lambda_A97)

    def lambda_AA8():

        label("loc_AA8")

        TurnDirection(0x2, 0x13, 400)
        OP_48()
        Jump("loc_AA8")

    QueueWorkItem2(0x2, 1, lambda_AA8)

    def lambda_AB9():

        label("loc_AB9")

        TurnDirection(0x3, 0x13, 400)
        OP_48()
        Jump("loc_AB9")

    QueueWorkItem2(0x3, 1, lambda_AB9)

    def lambda_ACA():

        label("loc_ACA")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_ACA")

    QueueWorkItem2(0xFE, 1, lambda_ACA)

    ChrTalk(    #50
        0x101,
        "#1011F啊，好像来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "嗯？那是什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "好像见过\x01",
            "又好像没见过……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 0x3)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_44(0xFE, 0x1)
    Sleep(1000)

    ChrTalk(    #53
        0x101,
        (
            "#1007F啊～太好了。\x01",
            "终－于找到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #54
        0xFE,
        "……啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "难、难不成这个\x01",
            "是游击士协会的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #56
        0x101,
        "#1007F嗯，就是那个难不成。\x02",
    )

    CloseMessageWindow()

    def lambda_BE9():
        OP_6D(-109730, -4000, -110940, 1000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_BE9)

    def lambda_C01():
        TurnDirection(0xF7, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C01)
    Sleep(150)

    def lambda_C14():
        TurnDirection(0xF8, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_C14)
    Sleep(100)
    TurnDirection(0xF9, 0xE, 400)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C67")

    ChrTalk(    #57
        0x106,
        (
            "#051F#1P多亏你帮大忙了。\x01",
            "多谢帮忙啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C92")

    label("loc_C67")


    ChrTalk(    #58
        0x103,
        (
            "#021F#1P多亏你帮大忙了。\x01",
            "多谢帮忙啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C92")

    TurnDirection(0xE, 0xF7, 400)

    ChrTalk(    #59
        0xFE,
        "这、这个先不说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "为什么协会的招牌\x01",
            "会在我们的仓库里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1016F嗯、嗯～……\x01",
            "从哪里开始说明好呢。\x02\x03",

            "说来就话长了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x142B)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_D34(): pass

    label("Function_1_D34")

    OP_8E(0xFE, 0xFFFE4580, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE53F4, 0xFFFFF060, 0xFFFE4E40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE5570, 0xFFFFF060, 0xFFFE4FBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_1_D34 end

    def Function_2_D78(): pass

    label("Function_2_D78")

    OP_8E(0xFE, 0xFFFE4580, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE50D4, 0xFFFFF060, 0xFFFE4FBC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_2_D78 end

    def Function_3_DA8(): pass

    label("Function_3_DA8")

    OP_8E(0xFE, 0xFFFE424C, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE5570, 0xFFFFF060, 0xFFFE49CC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_3_DA8 end

    def Function_4_DD8(): pass

    label("Function_4_DD8")

    OP_8E(0xFE, 0xFFFE424C, 0xFFFFF060, 0xFFFE4A76, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE50D4, 0xFFFFF060, 0xFFFE49CC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_4_DD8 end

    def Function_5_E08(): pass

    label("Function_5_E08")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #62
        0x8,
        (
            "欢迎光临中央工房\x01",
            "的维修窗口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "在找什么吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1015F#4P嗯，在找东西的\x01",
            "不是你吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "找东西的是我……唔。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #66
        0x8,
        (
            "啊，难道\x01",
            "各位是游击士吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_EF0")

    ChrTalk(    #67
        0x106,
        "#050F#1P啊啊，看了公告板才来的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F14")

    label("loc_EF0")


    ChrTalk(    #68
        0x103,
        "#020F#1P嗯嗯，看了公告板来的。\x02",
    )

    CloseMessageWindow()

    label("loc_F14")


    ChrTalk(    #69
        0x8,
        (
            "得、得救了。\x01",
            "其实是碰到点难事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "总之能听我说说吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE6")

    ChrTalk(    #71
        0x101,
        (
            "#1006F#4P嗯，好啊。\x02\x03",

            "事不宜迟，\x01",
            "好像在找什么是吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x4)
    Call(1, 7)
    Jump("loc_1071")

    label("loc_FE6")


    ChrTalk(    #72
        0x101,
        (
            "#1007F#4P啊，抱歉。\x01",
            "现在有点忙。\x02\x03",

            "有时间的时候\x01",
            "再来接受委托吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "啊，是这样吗？\x01",
            "我倒是无所谓。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "那么，稍后\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x1, 0x8000)
    EventEnd(0x0)

    label("loc_1071")

    Return()

    # Function_5_E08 end

    def Function_6_1072(): pass

    label("Function_6_1072")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #75
        0x8,
        (
            "啊，各位。\x01",
            "辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "那个，关于工作，\x01",
            "现在有时间了吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1151")

    ChrTalk(    #77
        0x101,
        (
            "#1006F#4P嗯，没问题了。\x02\x03",

            "事不宜迟，\x01",
            "好像在找什么是吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x4)
    Call(1, 7)
    Jump("loc_11BF")

    label("loc_1151")


    ChrTalk(    #78
        0x101,
        (
            "#1007F#4P抱、抱歉……\x01",
            "其实还不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "嗯～真忙啊。\x01",
            "唉，没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        (
            "那么，如果有空闲了\x01",
            "再请马上来。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_11BF")

    Return()

    # Function_6_1072 end

    def Function_7_11C0(): pass

    label("Function_7_11C0")

    EventBegin(0x0)

    ChrTalk(    #81
        0x8,
        (
            "嗯嗯，我在找导力器用的\x01",
            "小零件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "地震后检查了\x01",
            "各设施的备用品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "似乎是那时候从口袋的洞里\x01",
            "全部漏掉了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #84
        0x101,
        (
            "#1004F#4P口袋上有洞？\x02\x03",

            "#1016F哎呀～\x01",
            "那不丢才怪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "是，是……\x01",
            "完全是我的失误。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "虽然早就知道\x01",
            "磨破了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "地震的时候一慌，\x01",
            "想也没想就塞口袋里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1347")

    ChrTalk(    #88
        0x108,
        (
            "#070F然后走来走去\x01",
            "就从洞口掉了啊。\x02\x03",

            "原来如此，事情明白了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E6")

    label("loc_1347")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1398")

    ChrTalk(    #89
        0x105,
        (
            "#040F然后走来走去\x01",
            "就从洞口掉了吗。\x02\x03",

            "原来如此，事情明白了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E6")

    label("loc_1398")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E6")

    ChrTalk(    #90
        0x104,
        (
            "#030F然后走来走去\x01",
            "就从洞口掉了吧。\x02\x03",

            "原来如此，事情明白了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_141D")

    ChrTalk(    #91
        0x106,
        (
            "#050F#1P寻找那个零件\x01",
            "就是这次的委托吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144A")

    label("loc_141D")


    ChrTalk(    #92
        0x103,
        (
            "#020F#1P寻找那个零件\x01",
            "就是这次的委托吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")


    ChrTalk(    #93
        0x8,
        "是，没错。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CA")

    ChrTalk(    #94
        0x105,
        (
            "#043F不过，导力器的零件\x01",
            "一般来说都很细小吧。\x02\x03",

            "要找出来\x01",
            "估计很麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15A1")

    label("loc_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1538")

    ChrTalk(    #95
        0x104,
        (
            "#032F不过，导力器的零件\x01",
            "好像都很细小吧。\x02\x03",

            "要找出来\x01",
            "估计会很麻烦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15A1")

    label("loc_1538")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A1")

    ChrTalk(    #96
        0x107,
        (
            "#063F不过，导力器的零件\x01",
            "是很细小的吧。\x02\x03",

            "要找出来\x01",
            "估计会很麻烦……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15A1")


    def lambda_15A7():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_15A7)

    def lambda_15B5():
        TurnDirection(0xF8, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_15B5)

    def lambda_15C3():
        TurnDirection(0xF9, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_15C3)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #97
        0x101,
        (
            "#1015F#4P这么一说……\x01",
            "确、确实很麻烦的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        "嗯嗯，我也这么想。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "不过请放心，\x01",
            "这次有秘密武器。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1647():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1647)

    def lambda_1655():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1655)

    def lambda_1663():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1663)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #100
        0x101,
        "#1011F#4P秘密武器……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        "请使用这个。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x1F\x82\x03\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x382, 1)

    ChrTalk(    #103
        0x101,
        "#1004F#4P这是什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "嗯，是我开发的\x01",
            "材料可选金属探测器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "这个探测器啊……\x01",
            "能选择需要探知的金属种类。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "也就是只选择特定的材质\x01",
            "并且找出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1015F#4P好、好像很厉害……\x02\x03",

            "#1000F不过这和这次的工作有关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        "当然，关系大了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1849")

    ChrTalk(    #109
        0x107,
        (
            "#060F大概是这样吧。\x02\x03",

            "把零件所使用的特定金属\x01",
            "设定为探知目标……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x107, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1918")

    label("loc_1849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B2")

    ChrTalk(    #110
        0x104,
        (
            "#030F恐怕是这样吧。\x02\x03",

            "把零件所使用的特定金属\x01",
            "设定为探知目标……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1918")

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1918")

    ChrTalk(    #111
        0x105,
        (
            "#040F大概是这样吧。\x02\x03",

            "把零件所使用的特定金属\x01",
            "设定为探知目标……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197B")

    def lambda_192C():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_192C)

    def lambda_193A():
        TurnDirection(0x108, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_193A)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #112
        0x108,
        (
            "#070F唔，原来如此。\x02\x03",

            "只对零件作出反应吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A31")

    label("loc_197B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19CF")

    def lambda_198F():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_198F)

    def lambda_199D():
        TurnDirection(0x105, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_199D)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #113
        0x105,
        (
            "#040F只对零件\x01",
            "作出反应吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A31")

    label("loc_19CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A31")

    def lambda_19E3():
        TurnDirection(0xF7, 0x14, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_19E3)

    def lambda_19F1():
        TurnDirection(0x104, 0x14, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19F1)
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #114
        0x104,
        (
            "#030F唔，原来如此啊。\x02\x03",

            "只对零件作出反应吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A31")


    ChrTalk(    #115
        0x101,
        (
            "#1018F#4P啊，对哦。\x01",
            "确实是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        "嗯嗯，说得太对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "接近想调查的地方\x01",
            "使用探测器就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "如果有零件\x01",
            "应该会有反应的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ABF():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1ABF)

    def lambda_1ACD():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1ACD)
    Sleep(30)

    def lambda_1AE0():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1AE0)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #119
        0x101,
        "#1006F#4P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B6E")

    ChrTalk(    #120
        0x106,
        (
            "#050F#1P即使可以用这机器，\x01",
            "地方还是个问题呢。\x02\x03",

            "掉落零件的时候，\x01",
            "你记得都去哪儿了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC8")

    label("loc_1B6E")


    ChrTalk(    #121
        0x103,
        (
            "#020F#1P即使可以用这机器，\x01",
            "地方还是个问题呢。\x02\x03",

            "掉落零件的时候，\x01",
            "你记得都去哪儿了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC8")


    ChrTalk(    #122
        0x8,
        (
            "我去检查的\x01",
            "是３层的工作室和４层的实验室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "途中的电梯和走廊\x01",
            "我已经自己调查过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "各位就到研究室中\x01",
            "集中性地找找吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1C93")

    ChrTalk(    #125
        0x106,
        (
            "#050F#1P３层的工作室和４层的实验室吧。\x02\x03",

            "……好，明白了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD1")

    label("loc_1C93")


    ChrTalk(    #126
        0x103,
        (
            "#020F#1P３层的工作室和４层的实验室对吧？\x02\x03",

            "嗯嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD1")


    ChrTalk(    #127
        0x8,
        (
            "大概还有８个左右的\x01",
            "零件丢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "至少找到一半\x01",
            "我的工作也好办多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1000F#4P嗯，我们会努力看看的。\x02\x03",

            "如果发现了零件\x01",
            "再返回这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "嗯嗯，麻烦你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "那个时候探测器\x01",
            "也请一起归还。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1DD7")

    ChrTalk(    #132
        0x106,
        (
            "#050F#1P还有其他情报吗？\x01",
            "没有我们就走了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E08")

    label("loc_1DD7")


    ChrTalk(    #133
        0x103,
        (
            "#027F#1P还有其他情报吗？\x01",
            "没有我们就走了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E08")


    ChrTalk(    #134
        0x8,
        "啊，那么再说一点。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x8,
        (
            "４层的实验室\x01",
            "请特别仔细调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "在那里和安东尼\x01",
            "一起玩过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "零件一定也\x01",
            "丢了很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1011F#4P安东尼是……\x01",
            "住在工房里的猫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        "嗯嗯，就是那只安东尼。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        (
            "虽然很可爱，\x01",
            "但这次可真有点冤哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "唉，虽然完全是迁怒。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016F#4P啊哈哈，确实\x01",
            "安东尼有点可怜呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1F63")

    ChrTalk(    #143
        0x106,
        "#053F#1P好，那就走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F81")

    label("loc_1F63")


    ChrTalk(    #144
        0x103,
        "#020F#1P好了，那就走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1F81")


    ChrTalk(    #145
        0x8,
        "那么，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1006F#4P嗯，我们走了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x8)
    OP_28(0x6F, 0x1, 0x1)
    OP_28(0x6F, 0x1, 0x2)
    OP_28(0x6F, 0x1, 0x4)
    OP_A2(0xC)
    EventEnd(0x0)
    Return()

    # Function_7_11C0 end

    def Function_8_1FCF(): pass

    label("Function_8_1FCF")


    ChrTalk(    #147
        0x8,
        (
            "要找到零件的话\x01",
            "请去３层的工作室和４层的实验室。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "到了调查的场所\x01",
            "就在那里使用探测器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x8,
        (
            "如果有零件\x01",
            "应该会有反应的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        "那么，拜托了。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_8_1FCF end

    def Function_9_2063(): pass

    label("Function_9_2063")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #151
        0x8,
        (
            "呀，各位。\x01",
            "零件找到了吗？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_20AB")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_20C4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_20DD")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_20F6")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_210F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_210F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_2128")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2128")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x200)"), scpexpr(EXPR_END)), "loc_2141")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2141")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_215A")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_215A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A1")

    ChrTalk(    #152
        0x101,
        (
            "#1007F#5P嗯～完全没找到。\x02\x03",

            "多找找\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_21A1")


    ChrTalk(    #153
        0x101,
        (
            "#1015F#4P正在努力……的样子吧。\x02\x03",

            "总之，\x01",
            "报告一下状况吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (1, "loc_2214"),
        (2, "loc_2230"),
        (3, "loc_224C"),
        (4, "loc_2268"),
        (5, "loc_2284"),
        (6, "loc_22A0"),
        (7, "loc_22BC"),
        (8, "loc_22D8"),
        (SWITCH_DEFAULT, "loc_22F4"),
    )


    label("loc_2214")


    AnonymousTalk(    #154
        "\x07\x05报告发现了１个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_2230")


    AnonymousTalk(    #155
        "\x07\x05报告发现了２个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_224C")


    AnonymousTalk(    #156
        "\x07\x05报告发现了３个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_2268")


    AnonymousTalk(    #157
        "\x07\x05报告发现了４个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_2284")


    AnonymousTalk(    #158
        "\x07\x05报告发现了５个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_22A0")


    AnonymousTalk(    #159
        "\x07\x05报告发现了６个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_22BC")


    AnonymousTalk(    #160
        "\x07\x05报告发现了７个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_22D8")


    AnonymousTalk(    #161
        "\x07\x05报告发现了８个零件。\x02",
    )

    Jump("loc_22F4")

    label("loc_22F4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2311")
    Return()

    label("loc_2311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_264A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_245B")

    ChrTalk(    #162
        0x8,
        (
            "作为成果\x01",
            "我想已经足够了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "打算怎么办？\x01",
            "还继续搜索吗？\x02",
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
            "【结束搜索】\x01",      # 0
            "【继续搜索】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2402")

    ChrTalk(    #164
        0x101,
        (
            "#1015F#4P嗯，既然委托人这么说了\x01",
            "就搜索到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2458")

    ChrTalk(    #165
        0x101,
        (
            "#1006F#4P嗯，再稍微\x01",
            "努力看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "那么，拜托你们\x01",
            "继续搜索了。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_2458")

    Jump("loc_2647")

    label("loc_245B")


    ChrTalk(    #167
        0x8,
        (
            "啊，看来\x01",
            "找到不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "嗯，只要有这些\x01",
            "我想就足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1004F#4P哎，但是\x01",
            "还有零件没找到哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        "嗯嗯，虽然是没错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "嗯，难道\x01",
            "你们想继续搜索吗？\x02",
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
            "【结束搜索】\x01",      # 0
            "【继续搜索】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(    #172
        0x101,
        (
            "#1015F#4P嗯，既然委托人这么说了\x01",
            "就搜索到这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    label("loc_2595")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2647")

    ChrTalk(    #173
        0x101,
        (
            "#1015F#4P你这样说\x01",
            "我们是很高兴……\x02\x03",

            "#1000F还是再稍微\x01",
            "努力看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        "原来如此，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "那么，拜托你们\x01",
            "继续搜索了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#1006F#4P嗯，我们走了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x1, 0x800)
    EventEnd(0x0)

    label("loc_2647")

    Jump("loc_26DA")

    label("loc_264A")


    ChrTalk(    #177
        0x8,
        (
            "嗯，希望你们\x01",
            "搜索顺利……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "零件的数量\x01",
            "还有点不够啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        (
            "#1011F#4P啊，果然。\x02\x03",

            "#1006F那么，再稍微\x01",
            "努力看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        "嗯嗯，拜托了哦。\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_26DA")

    Return()

    # Function_9_2063 end

    def Function_10_26DB(): pass

    label("Function_10_26DB")

    EventBegin(0x0)
    Call(1, 14)

    ChrTalk(    #181
        0x8,
        (
            "哎！？\x01",
            "要取消工作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A2E")

    ChrTalk(    #182
        0x101,
        (
            "#1007F#4P是，对不起。\x02\x03",

            "非常抱歉，\x01",
            "突然有急事要办。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "这样啊……\x01",
            "那就没办法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "嗯，明白了。\x01",
            "我还是自己想想办法吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27F3")

    ChrTalk(    #185
        0x106,
        "#552F#1P啊啊，抱歉了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_280F")

    label("loc_27F3")


    ChrTalk(    #186
        0x103,
        "#025F#1P嗯嗯，抱歉哦。\x02",
    )

    CloseMessageWindow()

    label("loc_280F")


    ChrTalk(    #187
        0x8,
        "哪里哪里，别在意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "本来就是我自己不小心，\x01",
            "当然该自己收拾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "那么，麻烦把找到的零件\x01",
            "和探测器交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1015F#4P啊，对哦。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #191
        "\x1F\x82\x03\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2929")
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #192
        "\x1F\x33\x02\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2929")

    OP_3F(0x382, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2997")

    ChrTalk(    #193
        0x106,
        (
            "#050F#1P那么，我们\x01",
            "这就告辞了。\x02\x03",

            "今天真是抱歉了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29CE")

    label("loc_2997")


    ChrTalk(    #194
        0x103,
        (
            "#020F#1P那么，我们\x01",
            "这就告辞了。\x02\x03",

            "今天真是对不起。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29CE")


    ChrTalk(    #195
        0x8,
        "哪里，我才是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x8,
        "那么请当心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1000F#4P嗯，那么再见哦。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x40)
    OP_28(0x6F, 0x4, 0x80)
    OP_28(0x6F, 0x3, 0x8)
    OP_28(0x6F, 0x1, 0x4000)
    OP_A2(0xD)
    Jump("loc_2A6E")

    label("loc_2A2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6E")

    ChrTalk(    #198
        0x8,
        "呼，别吓人嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x8,
        (
            "那么，拜托你们\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6E")

    EventEnd(0x0)
    Return()

    # Function_10_26DB end

    def Function_11_2A71(): pass

    label("Function_11_2A71")


    ChrTalk(    #200
        0x8,
        "辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "那么零件\x01",
            "和探测器就还给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #202
        "\x1F\x82\x03\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #203
        "\x1F\x33\x02\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x382, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)
    OP_3F(0x233, 1)

    ChrTalk(    #204
        0x8,
        "呼，今天真是承蒙关照了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x8,
        (
            "由于我的疏忽\x01",
            "还给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006F#4P哪里，别放在心上。\x02\x03",

            "#1015F不过，这样\x01",
            "工作真的没问题了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x8,
        "哈哈，别担心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        (
            "有这些零件\x01",
            "目前就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C5D")

    ChrTalk(    #209
        0x107,
        (
            "#064F那就好……\x02\x03",

            "#560F那个，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFE")

    label("loc_2C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAD")

    ChrTalk(    #210
        0x105,
        (
            "#047F那就好……\x02\x03",

            "#045F不过，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CFE")

    label("loc_2CAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(    #211
        0x104,
        (
            "#035F唔，那就好……\x02\x03",

            "#030F但是，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFE")

    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #212
        0x8,
        "啊，对，对哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x8,
        "得去找针线包才行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x101,
        (
            "#1006F#4P需要帮忙的话\x01",
            "请马上联络协会。\x02\x03",

            "会带上针线\x01",
            "立刻来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        "啊哈哈，真是多谢你们关心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "那么，今天真是谢谢了。\x01",
            "以后还请多关照哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        "……针线是另外一回事，嗯。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E1B")

    ChrTalk(    #218
        0x106,
        "#051F#1P啊啊，请多关照。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E37")

    label("loc_2E1B")


    ChrTalk(    #219
        0x103,
        "#020F#1P嗯嗯，多关照。\x02",
    )

    CloseMessageWindow()

    label("loc_2E37")


    ChrTalk(    #220
        0x101,
        "#1018F#4P那么，回头见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x10)
    OP_28(0x6F, 0x1, 0x1000)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #221
        "\x07\x02任务【零件搜索】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    EventEnd(0x0)
    Return()

    # Function_11_2A71 end

    def Function_12_2EB3(): pass

    label("Function_12_2EB3")


    ChrTalk(    #222
        0x8,
        "咦，难道……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x8,
        (
            "８，８个零件全都\x01",
            "找到了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1011F#4P啊，全部找齐了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        (
            "好、好厉害啊。\x01",
            "我本来早就死心了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        (
            "总、总之先把零件和\x01",
            "探测器还给我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #227
        "\x1F\x82\x03\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #228
        "\x1F\x33\x02\x07\x00全部交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x382, 1)
    OP_3F(0x233, 8)

    ChrTalk(    #229
        0x8,
        "呀～今天真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x8,
        (
            "没想到全部零件\x01",
            "都能找回来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x101,
        (
            "#1017F#4P嘿嘿，能都找到\x01",
            "真是再好不过了。\x02\x03",

            "这样的话，工作的事情\x01",
            "就没问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x8,
        "嗯嗯，当然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x8,
        (
            "让你们这么费心，\x01",
            "我真是过意不去啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x8,
        "……啊，对了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x8,
        (
            "这么说来，\x01",
            "那个应该还在……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 135, 400)
    OP_8E(0x8, 0x2A62, 0x0, 0xFFFFF678, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    OP_8C(0x8, 315, 400)
    OP_8E(0x8, 0x21CA, 0x0, 0xFFFFFA6A, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #236
        0x8,
        "请收下这个吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x8,
        (
            "虽然是微薄之物，\x01",
            "就当是我的一点谢礼吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #238
        "\x07\x00得到了\x1F\x56\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x156, 1)
    Sleep(500)

    ChrTalk(    #239
        0x101,
        "#1001F#4P哇，谢谢！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_322C")

    ChrTalk(    #240
        0x106,
        "#052F#1P可以收下它吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3248")

    label("loc_322C")


    ChrTalk(    #241
        0x103,
        "#023F#1P可以给我们吗？\x02",
    )

    CloseMessageWindow()

    label("loc_3248")


    ChrTalk(    #242
        0x8,
        (
            "嗯嗯，别介意。\x01",
            "只是我的一点心意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x8,
        (
            "不管怎样，大家\x01",
            "今天真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x8,
        (
            "有各位，延迟的工作\x01",
            "也总算能挽回了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330F")

    ChrTalk(    #245
        0x107,
        (
            "#064F那就好……\x02\x03",

            "#560F那个，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B0")

    label("loc_330F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_335F")

    ChrTalk(    #246
        0x105,
        (
            "#047F那就好……\x02\x03",

            "#045F不过，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33B0")

    label("loc_335F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B0")

    ChrTalk(    #247
        0x104,
        (
            "#035F唔，那就好……\x02\x03",

            "#030F但是，口袋上的洞\x01",
            "最好是早点缝上哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B0")

    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #248
        0x8,
        "啊，对，对哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        "得去找针线包才行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x101,
        (
            "#1006F#4P需要帮忙的话\x01",
            "请马上联络协会。\x02\x03",

            "会带上针线\x01",
            "立刻来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        "啊哈哈，真是多谢你们关心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x8,
        (
            "那么，要是再有什么事\x01",
            "我再联络协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x8,
        "……针线是另外一回事，嗯。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_34C7")

    ChrTalk(    #254
        0x106,
        "#050F#1P啊啊，多关照。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E3")

    label("loc_34C7")


    ChrTalk(    #255
        0x103,
        "#020F#1P嗯嗯，多关照。\x02",
    )

    CloseMessageWindow()

    label("loc_34E3")


    ChrTalk(    #256
        0x101,
        "#1018F#4P那么，回头见。\x02",
    )

    CloseMessageWindow()
    OP_28(0x6F, 0x4, 0x10)
    OP_28(0x6F, 0x1, 0x2000)
    OP_2B(0x6F, 0x1)
    OP_2C(0x6F, 0x3E8)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #257
        "\x07\x02任务【零件搜索】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xD)
    EventEnd(0x0)
    Return()

    # Function_12_2EB3 end

    def Function_13_3569(): pass

    label("Function_13_3569")

    OP_A1(0x13, 0x19)
    SetChrPos(0x13, -95360, -3200, -109100, 14)
    OP_72(0x19, 0x4)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)

    def lambda_3594():
        OP_8F(0xFE, 0xFFFE5304, 0xFFFFF380, 0xFFFE55D4, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3594)
    Sleep(2500)
    OP_A2(0x11)
    WaitChrThread(0x13, 0x1)
    OP_75(0xFF, 0x16, 0x5)
    OP_23(0xA0)
    Return()

    # Function_13_3569 end

    def Function_14_35C1(): pass

    label("Function_14_35C1")

    Fade(1000)
    SetChrPos(0x8, 8650, 0, -1430, 270)
    SetChrPos(0x101, 6570, 0, -1750, 90)
    SetChrPos(0xF7, 6440, 0, -780, 90)
    SetChrPos(0xF8, 5430, 0, -1590, 90)
    SetChrPos(0xF9, 5190, 0, -570, 90)
    OP_6D(7540, 0, -1430, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Return()

    # Function_14_35C1 end

    SaveToFile()

Try(main)
