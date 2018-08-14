from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '卡西乌斯',                             # 9
        '王国军军官',                           # 10
        '卫兵',                                 # 11
        '卫兵',                                 # 12
        '卫兵',                                 # 13
        '卫兵',                                 # 14
        '卫兵',                                 # 15
        '',                                     # 16
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH03673 ._CH',             # 01
        'ED6_DT07/CH01600 ._CH',             # 02
        'ED6_DT07/CH01640 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH03673P._CP',             # 01
        'ED6_DT07/CH01600P._CP',             # 02
        'ED6_DT07/CH01640P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 22110,
        Z                   = 0,
        Y                   = 157150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -24850,
        Z                   = 0,
        Y                   = 38600,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 23150,
        Z                   = 0,
        Y                   = 127870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2240,
        Z                   = 0,
        Y                   = 1150,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -10400,
        Z                   = 0,
        Y                   = -3510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclEvent(
        X                   = -30350,
        Y                   = -2500,
        Z                   = 38060,
        Range               = -28450,
        Unknown_10          = 0xFFFFFF06,
        Unknown_14          = 0xA3E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = 21040,
        TriggerZ            = 0,
        TriggerY            = 158020,
        TriggerRange        = 1000,
        ActorX              = 21040,
        ActorZ              = 800,
        ActorY              = 158020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1EE",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_224",          # 02, 2
        "Function_3_23A",          # 03, 3
        "Function_4_280",          # 04, 4
        "Function_5_2A1",          # 05, 5
        "Function_6_2C2",          # 06, 6
        "Function_7_2E3",          # 07, 7
        "Function_8_304",          # 08, 8
        "Function_9_6DC",          # 09, 9
        "Function_10_F84",         # 0A, 10
        "Function_11_FAD",         # 0B, 11
        "Function_12_1003",        # 0C, 12
        "Function_13_106D",        # 0D, 13
        "Function_14_1094",        # 0E, 14
        "Function_15_10D1",        # 0F, 15
        "Function_16_1110",        # 10, 16
        "Function_17_1175",        # 11, 17
        "Function_18_1598",        # 12, 18
    )


    def Function_0_1EE(): pass

    label("Function_0_1EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_216")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_216")

    Return()

    # Function_0_1EE end

    def Function_1_217(): pass

    label("Function_1_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223")

    label("loc_223")

    Return()

    # Function_1_217 end

    def Function_2_224(): pass

    label("Function_2_224")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_239")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_224")

    label("loc_239")

    Return()

    # Function_2_224 end

    def Function_3_23A(): pass

    label("Function_3_23A")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x12,
        "准将在训练场等待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "整理好装备之后，\x01",
            "请到屋外去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_23A end

    def Function_4_280(): pass

    label("Function_4_280")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0x13,
        "◆卫兵的对话信息。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_280 end

    def Function_5_2A1(): pass

    label("Function_5_2A1")

    TalkBegin(0xFE)

    ChrTalk(    #3
        0x14,
        "◆卫兵的对话信息。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_2A1 end

    def Function_6_2C2(): pass

    label("Function_6_2C2")

    TalkBegin(0xFE)

    ChrTalk(    #4
        0x15,
        "◆卫兵的对话信息。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_2C2 end

    def Function_7_2E3(): pass

    label("Function_7_2E3")

    TalkBegin(0xFE)

    ChrTalk(    #5
        0x16,
        "◆卫兵的对话信息。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_2E3 end

    def Function_8_304(): pass

    label("Function_8_304")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, 21070, 0, 136950, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20650, 0, 138370, 0)
    SetChrPos(0x10, 21360, 0, 159470, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 22110, 0, 157150, 180)
    OP_4A(0x12, 255)
    OP_6D(22020, 0, 137120, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)

    def lambda_3A5():
        OP_6D(23210, 0, 157170, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3A5)

    def lambda_3BD():
        OP_6E(297, 4000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_3BD)

    def lambda_3CD():
        OP_8E(0xFE, 0x523A, 0x0, 0x25B0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3CD)

    def lambda_3E8():
        OP_8E(0xFE, 0x546A, 0x0, 0x25724, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3E8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #6
        0x12,
        (
            "#5P这前面是司令室。\x02\x03",

            "我可以代为传话，\x01",
            "请告诉我有什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        (
            "#6P是守备队副队长贝尔克\x01",
            "和游击士亚妮拉丝小姐。\x02\x03",

            "请求面见准将。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        "#810F#4P请、请多关照！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        "#5P是，请稍等。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #10
        0x12,
        (
            "#4P贝尔克副队长和游击士\x01",
            "已经到了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10,
        "男性的声音",
        "#2P没问题，让他们进来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        "#4P是！\x02",
    )

    Jump("loc_579")

    label("loc_579")

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x565E, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #13
        0x12,
        "#5P请进。\x02",
    )

    Jump("loc_5CE")

    label("loc_5CE")

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#6P辛苦了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_5ED():
        OP_6D(22290, 0, 158760, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_5ED)

    def lambda_605():
        OP_8E(0xFE, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_605)
    Sleep(400)

    def lambda_625():
        OP_8E(0xFE, 0x51CC, 0x0, 0x26322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_625)
    WaitChrThread(0x11, 0x0)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x9)
    OP_73(0x0)
    Sleep(300)

    def lambda_660():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_660)
    Sleep(400)

    def lambda_680():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_680)
    WaitChrThread(0x11, 0x0)

    def lambda_6A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6A0)
    WaitChrThread(0x10A, 0x0)

    def lambda_6B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6B7)
    WaitChrThread(0x10A, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x12, 255)
    Call(0, 9)
    Return()

    # Function_8_304 end

    def Function_9_6DC(): pass

    label("Function_9_6DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20940, 0, 260040, 180)
    OP_6D(21250, 0, 251550, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_78E():
        OP_6D(22440, 0, 258519, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_78E)

    def lambda_7A6():
        OP_6E(305, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_7A6)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_43(0x10A, 0x0, 0x0, 0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #15
        0x11,
        "我把亚妮拉丝小姐带来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1120F嗯，辛苦了。\x02\x03",

            "你可以回自己的岗位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "是，告辞了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #18
        0x10,
        (
            "#1120F哎呀，你来得正好。\x02\x03",

            "前阵子艾丝蒂尔\x01",
            "承蒙你的照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        (
            "#810F哪里，是我麻烦她才对。\x02\x03",

            "那个，不好意思。\x01",
            "让您特地腾出时间来见我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1120F哪里，不必客气。\x02\x03",

            "对了，\x01",
            "老爷子别来无恙吧。\x02\x03",

            "今天你好像是\x01",
            "受他的指示才来的吧。\x02",
        )
    )

    Jump("loc_950")

    label("loc_950")

    CloseMessageWindow()

    ChrTalk(    #21
        0x10A,
        (
            "#810F是、是的，没错……\x02\x03",

            "您果然\x01",
            "认识爷爷？\x02",
        )
    )

    Jump("loc_98D")

    label("loc_98D")

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#1120F是啊，他是剑道的高人嘛。\x02\x03",

            "不过自从十年前我退伍之后\x01",
            "就没再见过他了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#810F原来如此……\x02\x03",

            "其实，我来这里\x01",
            "也是和当时的事有关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#1120F哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10A,
        (
            "#810F卡西乌斯先生舍弃了剑，\x01",
            "爷爷至今仍觉得很惋惜。\x02\x03",

            "因此，听说您复归了军队，\x01",
            "就立刻派我来送信了。\x02\x03",

            "想问问您\x01",
            "是否有意回归剑之道……\x02\x03",

            "……他让我来直接确认\x01",
            "卡西乌斯先生的心意。\x02",
        )
    )

    Jump("loc_AFD")

    label("loc_AFD")

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#1120F嗯……是这样吗。\x02\x03",

            "他还记得\x01",
            "我这等未成熟的剑法，\x01",
            "实在是无上的光荣……\x02\x03",

            "……但是，我并没有\x01",
            "再度拿起剑的意思。\x02",
        )
    )

    Jump("loc_B86")

    label("loc_B86")

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        (
            "#810F为、为什么？\x02\x03",

            "是因为棒术\x01",
            "比剑术更优秀吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#1120F不，武术是不分优劣的。\x02\x03",

            "只不过棒术更符合\x01",
            "我现在的目标。\x02\x03",

            "不是斩杀敌人，\x01",
            "而是让敌人无法近身的\x01",
            "象征守护的武术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10A,
        (
            "#810F怎、怎么是这样……\x02\x03",

            "我也有\x01",
            "想要守护的东西啊！\x02\x03",

            "这……\x01",
            "不能用剑来守护吗？\x02",
        )
    )

    Jump("loc_CA8")

    label("loc_CA8")

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#1120F很遗憾，这个问题\x01",
            "我没有直接的答案。\x02\x03",

            "不过，对了……\x02\x03",

            "……正好。\x01",
            "就让她来回答吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10A,
        "#810F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_D26():
        OP_6D(22330, 0, 254190, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_D26)
    OP_43(0x10, 0x0, 0x0, 0xA)

    def lambda_D45():

        label("loc_D45")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_D45")

    QueueWorkItem2(0x10A, 0, lambda_D45)
    Sleep(2500)

    ChrTalk(    #32
        0x10A,
        "#810F#5P怎、怎么回事？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x2)
    OP_44(0x10A, 0x0)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #33
        0x10,
        (
            "#1120F我去准备一下。\x02\x03",

            "亚妮拉丝……\x01",
            "你也整理一下装备，\x01",
            "然后到外面的训练场来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10A,
        "#810F#5P整、整理装备……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#1120F啊啊，\x01",
            "因为可能会有点危险。\x02\x03",

            "那么，等你过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        "#810F#5P是、是的！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0xB)
    WaitChrThread(0x10, 0x0)
    OP_6D(22800, 0, 255550, 1000)

    ChrTalk(    #37
        0x10A,
        (
            "#810F#5P呼、呼……\x02\x03",

            "虽、虽然还不是太明白，\x01",
            "看来只好照做了。\x02\x03",

            "总之，\x01",
            "先检查一下装备……\x02",
        )
    )

    Jump("loc_EF0")

    label("loc_EF0")

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x10A, 20820, 0, 156030, 180)
    OP_6D(20820, 0, 156030, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_65(0x0, 0x1)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x0)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x2000, 0x0)
    ExitThread()
    Sleep(1000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_6DC end

    def Function_10_F84(): pass

    label("Function_10_F84")

    OP_8E(0xFE, 0x4EFC, 0x0, 0x3F304, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4EFC, 0x0, 0x3E2EC, 0x7D0, 0x0)
    Return()

    # Function_10_F84 end

    def Function_11_FAD(): pass

    label("Function_11_FAD")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x5028, 0x0, 0x3DA54, 0x7D0, 0x0)
    Sleep(200)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)

    def lambda_FDD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FDD)
    OP_8E(0xFE, 0x5028, 0x0, 0x3D284, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_FAD end

    def Function_12_1003(): pass

    label("Function_12_1003")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x4F9C, 0x0, 0x3E120, 0x7D0, 0x0)
    OP_8E(0xFE, 0x5140, 0x0, 0x3D8E2, 0x7D0, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)

    def lambda_1042():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1042)
    OP_8E(0xFE, 0x5140, 0x0, 0x3D090, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Return()

    # Function_12_1003 end

    def Function_13_106D(): pass

    label("Function_13_106D")


    def lambda_1073():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1073)
    OP_8E(0xFE, 0x50AA, 0x0, 0x3E59E, 0x7D0, 0x0)
    Return()

    # Function_13_106D end

    def Function_14_1094(): pass

    label("Function_14_1094")

    Sleep(600)

    def lambda_109F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109F)

    def lambda_10B1():
        OP_8E(0xFE, 0x53F2, 0x0, 0x3E1DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B1)
    Sleep(700)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_14_1094 end

    def Function_15_10D1(): pass

    label("Function_15_10D1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #38
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_10D1 end

    def Function_16_1110(): pass

    label("Function_16_1110")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111D")
    Return()

    label("loc_111D")

    EventBegin(0x1)
    OP_4A(0x13, 255)

    ChrTalk(    #39
        0x13,
        "前面禁止入内。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13,
        "请回吧。\x02",
    )

    Jump("loc_1154")

    label("loc_1154")

    CloseMessageWindow()
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    OP_4B(0x13, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_16_1110 end

    def Function_17_1175(): pass

    label("Function_17_1175")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x10A, 21070, 0, 136950, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20650, 0, 138370, 0)
    SetChrPos(0x10, 21360, 0, 159470, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 22110, 0, 157150, 180)
    OP_6D(22020, 0, 137120, 0)
    OP_67(0, 7520, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(337, 0)

    def lambda_1212():
        OP_6D(23210, 0, 157170, 7000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_1212)

    def lambda_122A():
        OP_6E(297, 7000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_122A)

    def lambda_123A():
        OP_67(0, 5120, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_123A)

    def lambda_1252():
        OP_8E(0xFE, 0x523A, 0x0, 0x25B0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1252)

    def lambda_126D():
        OP_8E(0xFE, 0x546A, 0x0, 0x25724, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_126D)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1500)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(1000)
    Call(0, 18)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #41
        0x12,
        "#5P这前面是司令室。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x12,
        (
            "#5P我可以代为传话，\x01",
            "请告诉我有什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        (
            "#6P我奉准将之命，\x01",
            "将游击士亚妮拉丝小姐带来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#6P请求面见准将。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        "#812F#4P请、请多关照！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        "#5P是，请稍候。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #47
        0x12,
        (
            "#4P准将大人，\x01",
            "游击士已经到了。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #48
        0x10,
        "男性的声音",
        "#2P没问题，让他们进来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        "#4P是，明白！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 90, 400)
    OP_8E(0x12, 0x51F4, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8E(0x12, 0x565E, 0x0, 0x265DE, 0x7D0, 0x0)
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #50
        0x12,
        "#5P请进。\x02",
    )

    Jump("loc_148A")

    label("loc_148A")

    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#6P辛苦了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_14A9():
        OP_6D(22290, 0, 158760, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_14A9)

    def lambda_14C1():
        OP_8E(0xFE, 0x51F4, 0x0, 0x26854, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_14C1)
    Sleep(400)

    def lambda_14E1():
        OP_8E(0xFE, 0x51CC, 0x0, 0x26322, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_14E1)
    WaitChrThread(0x11, 0x0)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x9)
    OP_73(0x0)
    Sleep(300)

    def lambda_151C():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_151C)
    Sleep(400)

    def lambda_153C():
        OP_8E(0xFE, 0x538E, 0x0, 0x26F0C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_153C)
    WaitChrThread(0x11, 0x0)

    def lambda_155C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_155C)
    WaitChrThread(0x10A, 0x0)

    def lambda_1573():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1573)
    WaitChrThread(0x10A, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x12, 255)
    Call(0, 18)
    Return()

    # Function_17_1175 end

    def Function_18_1598(): pass

    label("Function_18_1598")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10A, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 20740, 0, 250590, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 20940, 0, 260040, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(21250, 0, 251550, 0)
    OP_67(0, 5040, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(297, 0)

    def lambda_1686():
        OP_6D(22360, 0, 258519, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1686)

    def lambda_169E():
        OP_6E(305, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_169E)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_43(0x10A, 0x0, 0x0, 0xE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x10A, 0x3)
    Sleep(500)

    ChrTalk(    #52
        0x11,
        "#6P我把亚妮拉丝小姐带来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#1125F#5P嗯，辛苦了。\x02\x03",

            "#1120F你可以回自己的岗位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        "#6P是，告辞了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x11, 0x0, 0x0, 0xC)
    Sleep(3000)

    def lambda_177B():
        OP_6D(22360, 0, 259980, 1500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_177B)

    def lambda_1793():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3ECC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1793)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #55
        0x10,
        (
            "#1123F#5P呼，亚妮拉丝。\x01",
            "抱歉迟到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10A,
        (
            "#816F#12P#12P哪里，没关系。\x02\x03",

            "#1316F倒是我才应该道歉。\x01",
            "百忙之中还麻烦您\x01",
            "特地抽出时间来见我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "#1121F#5P哈哈，这也是为了\x01",
            "游击士时代的可爱后辈嘛。\x01",
            "你不必介意。\x02\x03",

            "#1120F不过，还真是好久不见了呢。\x01",
            "亚妮拉丝。\x02\x03",

            "嗯……看起来\x01",
            "水平又有进步了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#819F#12P嘿嘿，还好啦……\x02\x03",

            "#816F我可不能输给\x01",
            "在远处努力着的\x01",
            "艾丝蒂尔嘛。\x02\x03",

            "姑且也算是\x01",
            "被她承认的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#1125F#5P呵呵，是啊。\x02\x03",

            "#1120F那我就期待你们\x01",
            "今后的活跃表现了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10A,
        "#811F#12P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "#1120F#5P对了……云老师\x01",
            "似乎还是那么健朗。\x02\x03",

            "今天你好像是\x01",
            "受他的指示才来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10A,
        (
            "#1316F#12P是、是的，\x01",
            "关于这件事……\x02\x03",

            "#818F卡西乌斯先生，\x01",
            "您果然认识\x01",
            "我爷爷吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1125F#5P啊啊，他是我剑道的恩师。\x02\x03",

            "#1120F已经是二十多年前的事了吧……\x01",
            "第一次见面\x01",
            "还是在士官学校学剑的时候。\x02\x03",

            "#1121F呵呵，在这个雷斯顿要塞里\x01",
            "可是被他教训得很惨呢，\x01",
            "到现在还历历在目。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10A,
        (
            "#819F#12P原、原来如此……\x02\x03",

            "#814F但、但是，\x01",
            "为什么您不告诉我\x01",
            "认识爷爷的事呢？\x02\x03",

            "您知道我是\x01",
            "爷爷的孙女吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1125F#5P……啊啊，是的。\x02\x03",

            "#1120F只是，见到你时\x01",
            "我已放弃剑术多时了。\x02\x03",

            "要自称是师兄\x01",
            "也有点心虚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10A,
        "#813F#12P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1125F#5P和云老师也已有十年不见了……\x02\x03",

            "#1120F虽然偶有联络，\x01",
            "不知他老人家还好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10A,
        (
            "#819F#12P啊，是的……\x01",
            "他倒是老样子，\x01",
            "总是生龙活虎的……\x02\x03",

            "#812F嗯，对了。\x02\x03",

            "其实，\x01",
            "我今天来这里也是和\x01",
            "十年前的事有关。\x02",
        )
    )

    Jump("loc_1D95")

    label("loc_1D95")

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "#1124F#5P哦……\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #70
        0x10A,
        (
            "#1316F#12P卡西乌斯先生舍弃了剑，\x01",
            "爷爷至今仍觉得很惋惜。\x02\x03",

            "因此，听说您复归了军队，\x01",
            "就立刻给我写了信。\x02\x03",

            "#813F想问问您\x01",
            "是否有重新拿起剑的觉悟……\x02\x03",

            "#812F……他让我来直接确认\x01",
            "卡西乌斯先生的心意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        "#1128F#5P嗯……是这样吗。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #72
        0x10,
        (
            "#1125F#5P他还记得\x01",
            "我这等未成熟的剑法，\x01",
            "实在是光荣之至……\x02\x03",

            "#1122F……但是，我并没有\x01",
            "再度拿起剑的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10A,
        (
            "#1317F#12P…………………………\x02\x03",

            "#813F这、这是……\x01",
            "为什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#1123F#5P嗯，这个啊。\x01",
            "怎么说才好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10A,
        (
            "#1316F#12P我……\x01",
            "一直有一个疑问。\x02\x03",

            "被称为『剑圣』的\x01",
            "卡西乌斯先生，\x01",
            "为什么会放弃剑……\x02\x03",

            "#813F虽然我并不是想\x01",
            "否定卡西乌斯先生\x01",
            "所用的棒术……\x02\x03",

            "#812F但是，我还是\x01",
            "无论如何也无法接受……！\x02\x03",

            "为什么回到了军队\x01",
            "却还是不想拿起剑呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        "#1122F#5P嗯………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10A,
        (
            "#1316F#12P难、难道是……\x02\x03",

            "#813F……因为您觉得棒术\x01",
            "比剑术更优秀吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "#1125F#5P不，\x01",
            "绝不是因为这个。\x02\x03",

            "只是棒术比剑\x01",
            "更适合我现在的立场──\x01",
            "如此而已。\x02\x03",

            "#1120F不是斩杀敌人，\x01",
            "而是让敌人无法近身的\x01",
            "象征守护的武术。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x10A,
        (
            "#1317F#12P怎、怎么是这样……\x01",
            "剑也不仅仅是用来\x01",
            "斩人的武器啊！\x02\x03",

            "#813F而且，我也有\x01",
            "想要守护的东西啊……！\x02\x03",

            "#30W作为剑士，作为游击士……\x01",
            "……更重要的是作为我自己………\x02\x03",

            "#815F#20W难道说……难道说……\x01",
            "您认为爷爷教的剑法\x01",
            "无法守护吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        "#1122F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10A,
        (
            "#1316F#12P对、对不起。\x01",
            "我说了些莽撞的话……\x02\x03",

            "#813F#30W但是……我……\x01",
            "无论如何也无法接受……\x02\x03",

            "至今为止从来没有\x01",
            "因为挥剑而感到迷茫……\x02\x03",

            "但是通过那件事，\x01",
            "却重新感受到了自己的软弱……\x02\x03",

            "#1316F这样下去我……\x01",
            "觉得自己无论怎样努力\x01",
            "大概也无法独当一面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1125F#5P……原来如此啊。\x02\x03",

            "嗯……\x01",
            "这也是女神的旨意吧。\x02\x03",

            "#1120F话说回来……\x01",
            "老师还是那么坏心眼。\x02",
        )
    )

    Jump("loc_24F5")

    label("loc_24F5")

    CloseMessageWindow()

    ChrTalk(    #83
        0x10A,
        "#814F#12P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#1125F#5P……亚妮拉丝。\x01",
            "很遗憾，现在的我\x01",
            "无法回答你的问题。\x02\x03",

            "#1122F因此……\x01",
            "我就让代替者来回答吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_6B(3130, 3000)
    OP_0D()
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()

    def lambda_25B2():
        OP_6D(22360, 0, 257980, 2500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_25B2)
    OP_43(0x10, 0x0, 0x0, 0xA)

    def lambda_25D1():

        label("loc_25D1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_25D1")

    QueueWorkItem2(0x10A, 0, lambda_25D1)
    Sleep(2500)

    ChrTalk(    #85
        0x10A,
        "#812F#5P要、要去哪里？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x10A, 0x2)
    OP_44(0x10A, 0x0)
    OP_8C(0x10A, 180, 400)
    WaitChrThread(0x10, 0x0)
    OP_8C(0x10, 0, 400)

    ChrTalk(    #86
        0x10,
        (
            "#1120F你很快就知道了。\x02\x03",

            "跟我来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        "#813F#5P是、是……\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x0, 0x0, 0xB)
    Sleep(600)

    def lambda_266B():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3DA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_266B)
    WaitChrThread(0x10A, 0x0)

    def lambda_268B():
        OP_8E(0xFE, 0x51CC, 0x0, 0x3D284, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_268B)

    def lambda_26A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_26A6)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/C3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_1598 end

    SaveToFile()

Try(main)
