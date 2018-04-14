from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4404   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4404.x',
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
        '杜南公爵',                             # 9
        '凯诺娜',                               # 10
        '特务兵',                               # 11
        '特务兵',                               # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '特务兵',                               # 17
        '导力战车『奥尔杰尤』',                 # 18
        '王都格兰赛尔·码头南',                 # 19
        '侵蚀狼犬',                             # 20
        '侵蚀狼犬',                             # 21
        '侵蚀狼犬',                             # 22
        '侵蚀狼犬',                             # 23
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


    AddCharChip(
        'ED6_DT07/CH02140 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH01330 ._CH',             # 02
        'ED6_DT27/CH04000 ._CH',             # 03
        'ED6_DT27/CH04001 ._CH',             # 04
        'ED6_DT07/CH00120 ._CH',             # 05
        'ED6_DT07/CH00121 ._CH',             # 06
        'ED6_DT07/CH00150 ._CH',             # 07
        'ED6_DT07/CH00151 ._CH',             # 08
        'ED6_DT27/CH04080 ._CH',             # 09
        'ED6_DT27/CH04081 ._CH',             # 0A
        'ED6_DT07/CH00340 ._CH',             # 0B
        'ED6_DT07/CH00341 ._CH',             # 0C
        'ED6_DT07/CH00344 ._CH',             # 0D
        'ED6_DT07/CH00440 ._CH',             # 0E
        'ED6_DT07/CH00441 ._CH',             # 0F
        'ED6_DT07/CH00441 ._CH',             # 10
        'ED6_DT07/CH00444 ._CH',             # 11
        'ED6_DT09/CH10060 ._CH',             # 12
        'ED6_DT09/CH10061 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02140P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH01330P._CP',             # 02
        'ED6_DT27/CH04000P._CP',             # 03
        'ED6_DT27/CH04001P._CP',             # 04
        'ED6_DT07/CH00120P._CP',             # 05
        'ED6_DT07/CH00121P._CP',             # 06
        'ED6_DT07/CH00150P._CP',             # 07
        'ED6_DT07/CH00151P._CP',             # 08
        'ED6_DT27/CH04080P._CP',             # 09
        'ED6_DT27/CH04081P._CP',             # 0A
        'ED6_DT07/CH00340P._CP',             # 0B
        'ED6_DT07/CH00341P._CP',             # 0C
        'ED6_DT07/CH00344P._CP',             # 0D
        'ED6_DT07/CH00440P._CP',             # 0E
        'ED6_DT07/CH00441P._CP',             # 0F
        'ED6_DT07/CH00441P._CP',             # 10
        'ED6_DT07/CH00444P._CP',             # 11
        'ED6_DT09/CH10060P._CP',             # 12
        'ED6_DT09/CH10061P._CP',             # 13
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x189,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -880,
        Z                   = 0,
        Y                   = -32689,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -670,
        Z                   = 0,
        Y                   = 15150,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -11530,
        Z                   = 0,
        Y                   = 35690,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13160,
        Z                   = 0,
        Y                   = 25810,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14350,
        Z                   = 0,
        Y                   = 44170,
        Unknown_0C          = 0,
        Unknown_0E          = 18,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3DE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 21200,
        Y                   = -2000,
        Z                   = 47800,
        Range               = 23000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xF35C,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_33A",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_3F1",          # 02, 2
        "Function_3_407",          # 03, 3
        "Function_4_F02",          # 04, 4
        "Function_5_F28",          # 05, 5
        "Function_6_F4E",          # 06, 6
        "Function_7_F74",          # 07, 7
        "Function_8_FBB",          # 08, 8
        "Function_9_FE1",          # 09, 9
        "Function_10_1007",        # 0A, 10
        "Function_11_1032",        # 0B, 11
        "Function_12_1058",        # 0C, 12
        "Function_13_2483",        # 0D, 13
        "Function_14_24C5",        # 0E, 14
        "Function_15_251B",        # 0F, 15
        "Function_16_256C",        # 10, 16
        "Function_17_25C2",        # 11, 17
        "Function_18_25F9",        # 12, 18
        "Function_19_2622",        # 13, 19
        "Function_20_264B",        # 14, 20
    )


    def Function_0_33A(): pass

    label("Function_0_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35A")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_35A")

    Return()

    # Function_0_33A end

    def Function_1_35B(): pass

    label("Function_1_35B")

    OP_16(0x2, 0xFA0, 0xFFFE2370, 0xFFFEE2D8, 0x23006E)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x45D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_387")

    OP_72(0x7, 0x10)
    OP_72(0xA, 0x10)
    OP_72(0xB, 0x10)
    OP_72(0x7, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0x1, 0x10)
    OP_72(0x2, 0x10)
    OP_72(0x3, 0x10)
    OP_72(0x8, 0x10)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x8, 0x4)
    OP_72(0x5, 0x10)
    OP_72(0x4, 0x10)
    OP_72(0x6, 0x10)
    OP_72(0x5, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x6, 0x4)
    OP_71(0xC, 0x4)
    Return()

    # Function_1_35B end

    def Function_2_3F1(): pass

    label("Function_2_3F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_406")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F1")

    label("loc_406")

    Return()

    # Function_2_3F1 end

    def Function_3_407(): pass

    label("Function_3_407")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_423")
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_423")

    Fade(1000)
    OP_6D(22590, 0, 54310, 0)
    OP_67(0, 12420, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(138000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 22670, 0, 55450, 90)
    SetChrPos(0xF7, 22590, 0, 54260, 90)
    SetChrPos(0x109, 21470, 0, 54830, 90)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x8, 37560, 0, 53580, 270)
    SetChrPos(0x9, 35110, 0, 55020, 270)
    SetChrPos(0xA, 38350, 0, 53580, 270)
    SetChrPos(0xB, 35840, 0, 55950, 270)
    SetChrPos(0xC, 35880, 0, 54180, 270)
    SetChrPos(0xD, 36530, 0, 56690, 270)
    SetChrPos(0xE, 36530, 0, 53240, 270)
    SetChrPos(0xF, 38030, 0, 55680, 270)
    SetChrPos(0x10, 37130, 0, 54760, 270)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    OP_20(0x7D0)

    NpcTalk(    #0
        0x9,
        "女人的声音",
        "#4P哼，果然来了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_607():
        OP_6D(33260, 0, 54610, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_607)

    def lambda_61F():
        OP_67(0, 6790, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_61F)

    def lambda_637():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_637)

    def lambda_647():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_647)

    def lambda_657():
        OP_6E(316, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_657)

    def lambda_667():
        OP_8E(0xFE, 0x7148, 0x0, 0xD9BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_667)
    Sleep(100)

    def lambda_687():
        OP_8E(0xFE, 0x7148, 0x0, 0xD53E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_687)
    Sleep(200)

    def lambda_6A7():
        OP_8E(0xFE, 0x6D4C, 0x0, 0xD818, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A7)
    Sleep(1000)
    OP_1D(0x56)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #1
        0x101,
        "#1005F#6P凯诺娜上尉！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#1182F#5P哼，是原上尉。\x02\x03",

            "军犬们那么吵闹，\x01",
            "我就知道有问题，才出来看看……\x02\x03",

            "不愧是游击士，\x01",
            "嗅觉相当灵敏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1005F#6P别小看我们！\x01",
            "竟然做出那种事！\x02\x03",

            "连无辜的孩子都……\x01",
            "绝对不能原谅！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#1181F#5P你在说什么？\x02\x03",

            "我们只是协助公爵阁下\x01",
            "继承王位而已。\x02\x03",

            "无关的外人请让开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1020F#6P啊！？\x02\x03",

            "公爵！？\x01",
            "你又在做什么愚蠢的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        (
            "#226F#6P谁、谁会支持\x01",
            "这样无谋的计划！\x02\x03",

            "这、这些家伙只是\x01",
            "打算利用我而已！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1060F嗯～好像是真的\x01",
            "很不情愿啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_917")

    ChrTalk(    #8
        0x106,
        (
            "#057F#2P这母狐狸……\x01",
            "还不说实话吗。\x02\x03",

            "你真正的目的\x01",
            "是解放理查德吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96D")

    label("loc_917")


    ChrTalk(    #9
        0x103,
        (
            "#022F#2P原上尉大人，差不多\x01",
            "该说实话了吧。\x02\x03",

            "你真正的目的\x01",
            "是为了解放理查德上校吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_96D")


    ChrTalk(    #10
        0x101,
        "#1004F#6P#3S咦咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#1183F#5P哈哈哈，连这\x01",
            "都知道就好说了……\x02\x03",

            "#1186F──现在\x01",
            "开始『再启动作战』！\x02\x03",

            "你们！\x01",
            "努力撑个两分钟吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("特务兵们")

    AnonymousTalk(    #12
        "\x07\x00#3S是·长官！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    def lambda_A42():
        OP_6D(37020, 0, 54410, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A42)

    def lambda_A5A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A5A)
    OP_43(0xD, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0xF, 0x0, 0x0, 0x5)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0x6)
    SetChrFlags(0x8, 0x20)

    def lambda_A8C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A8C)
    Sleep(50)

    def lambda_A9F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A9F)
    Sleep(50)

    def lambda_AB2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AB2)

    def lambda_AC0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AC0)
    Sleep(500)

    def lambda_AD3():
        OP_8E(0xFE, 0xBA54, 0x3E8, 0xD67E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_AD3)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0xA, 2)

    def lambda_B14():
        OP_8E(0xFE, 0xB66C, 0x3E8, 0xD37C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B14)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_B3B():
        OP_8F(0xFE, 0xB66C, 0x3E8, 0xD37C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B3B)

    def lambda_B56():

        label("loc_B56")

        OP_9E(0xFE, 0x1E, 0x0, 0x1F4, 0xBB8)
        OP_48()
        Jump("loc_B56")

    QueueWorkItem2(0x8, 2, lambda_B56)
    Sleep(200)
    SetChrChipByIndex(0xB, 15)

    def lambda_B7D():
        OP_8E(0xFE, 0xB284, 0x3E8, 0xDA8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B7D)
    SetChrChipByIndex(0xC, 12)

    def lambda_B9D():
        OP_8E(0xFE, 0xB284, 0x3E8, 0xD3A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B9D)

    def lambda_BB8():
        OP_6D(33260, 0, 54610, 1200)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_BB8)
    OP_43(0x9, 0x2, 0x0, 0x7)
    WaitChrThread(0x9, 0x0)

    ChrTalk(    #13
        0x101,
        (
            "#1005F#6P喂，等一下啊！\x02\x03",

            "公爵也就算了，\x01",
            "至少先把玲还给我们……\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x0, 0x8)
    OP_43(0xE, 0x1, 0x0, 0x9)
    OP_43(0xF, 0x1, 0x0, 0xA)
    OP_43(0x10, 0x1, 0x0, 0xB)

    def lambda_C3C():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3C)
    Sleep(100)

    def lambda_C5C():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C5C)
    Sleep(100)

    def lambda_C7C():
        OP_90(0xFE, 0x7D0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C7C)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #14
        0xD,
        (
            "#5P上尉殿下的决意和觉悟，\x01",
            "绝不能让你们阻挠！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xE,
        "#2P来吧，协会的走狗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1005F#6P可、可恶～……\x02",
    )

    CloseMessageWindow()
    Fade(400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 3)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D48")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 7)
    Jump("loc_D52")

    label("loc_D48")

    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 5)

    label("loc_D52")

    Sleep(200)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA5")

    ChrTalk(    #17
        0x106,
        (
            "#054F#2P真有种……\x01",
            "那就把你们统统打垮！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD8")

    label("loc_DA5")


    ChrTalk(    #18
        0x103,
        (
            "#024F#2P真有胆量……\x01",
            "让我好好疼爱疼爱你们吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD8")

    Sleep(100)
    SetChrChipByIndex(0xD, 12)
    SetChrChipByIndex(0xE, 12)
    SetChrChipByIndex(0xF, 15)
    SetChrChipByIndex(0x10, 15)

    def lambda_DF7():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF7)

    def lambda_E12():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_E12)

    def lambda_E2D():
        OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E2D)

    def lambda_E48():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E48)

    def lambda_E63():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E63)

    def lambda_E7E():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E7E)

    def lambda_E99():
        OP_90(0xFE, 0xFFFFF830, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E99)

    def lambda_EB4():
        OP_6B(2510, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB4)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x45D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_EF8"),
        (SWITCH_DEFAULT, "loc_EFD"),
    )


    label("loc_EF8")

    OP_B4(0x0)
    Jump("loc_EFD")

    label("loc_EFD")

    Call(0, 12)
    Return()

    # Function_3_407 end

    def Function_4_F02(): pass

    label("Function_4_F02")

    SetChrChipByIndex(0xFE, 12)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x8F16, 0x0, 0xE254, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 11)
    Return()

    # Function_4_F02 end

    def Function_5_F28(): pass

    label("Function_5_F28")

    SetChrChipByIndex(0xFE, 15)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x942A, 0x0, 0xDE44, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_5_F28 end

    def Function_6_F4E(): pass

    label("Function_6_F4E")

    SetChrChipByIndex(0xFE, 15)
    OP_8C(0xFE, 180, 400)
    OP_8F(0xFE, 0x8FDE, 0x0, 0xDE3A, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 14)
    Return()

    # Function_6_F4E end

    def Function_7_F74(): pass

    label("Function_7_F74")

    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_44(0x8, 0x2)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 45)
    OP_70(0x0, 0x1F)
    OP_22(0xD3, 0x0, 0x64)
    OP_73(0x0)
    Sleep(400)
    OP_22(0x73, 0x0, 0x64)
    Return()

    # Function_7_F74 end

    def Function_8_FBB(): pass

    label("Function_8_FBB")

    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x8BB0, 0x0, 0xD9B2, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_8_FBB end

    def Function_9_FE1(): pass

    label("Function_9_FE1")

    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x8B42, 0x0, 0xD354, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_9_FE1 end

    def Function_10_1007(): pass

    label("Function_10_1007")

    Sleep(100)
    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x91DC, 0x0, 0xD994, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_10_1007 end

    def Function_11_1032(): pass

    label("Function_11_1032")

    SetChrChipByIndex(0xFE, 15)
    OP_8E(0xFE, 0x90B0, 0x0, 0xD1E2, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    OP_8C(0xFE, 270, 600)
    Return()

    # Function_11_1032 end

    def Function_12_1058(): pass

    label("Function_12_1058")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x1)
    SetChrPos(0x101, 33440, 0, 55730, 90)
    SetChrPos(0xF7, 33440, 0, 54390, 90)
    SetChrPos(0x109, 32000, 0, 55000, 90)
    SetChrPos(0xD, 37250, 0, 55300, 270)
    SetChrPos(0xE, 37250, 0, 54000, 270)
    SetChrPos(0xF, 38260, 0, 55760, 270)
    SetChrPos(0x10, 38260, 0, 53780, 270)
    SetChrChipByIndex(0x101, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110B")
    SetChrChipByIndex(0x106, 7)
    Jump("loc_1110")

    label("loc_110B")

    SetChrChipByIndex(0x103, 5)

    label("loc_1110")

    SetChrChipByIndex(0x109, 9)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 13)
    SetChrChipByIndex(0xF, 17)
    SetChrChipByIndex(0x10, 17)
    SetChrSubChip(0xD, 3)
    SetChrSubChip(0xE, 3)
    SetChrSubChip(0xF, 3)
    SetChrSubChip(0x10, 3)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0x10, 0x0)
    OP_6D(35640, 0, 54600, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(133000, 0)
    OP_6E(316, 0)
    LoadEffect(0x0, "monster\\ms30600d.eff")
    LoadEffect(0x1, "monster\\ms30602a.eff")
    LoadEffect(0x2, "monster\\ms30602b.eff")
    LoadEffect(0x3, "monster\\ms30600b.eff")
    LoadEffect(0x4, "monster\\ms30600a.eff")
    OP_6F(0x0, 31)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0xF,
        "可、可恶……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        "#2P这些家伙……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1005F#6P趁早死心吧！\x02\x03",

            "喂！\x01",
            "赶快让开……\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0xC, 0x4)
    OP_A1(0x11, 0xC)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 47700, 1000, 54940, 270)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_20(0x0)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 2)
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1020F#6P哇哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        "#1069F什、什么！？\x02",
    )

    CloseMessageWindow()
    OP_6D(38840, 40, 54260, 1000)
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 2)
    OP_70(0x0, 0x4)
    OP_22(0x10F, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x71)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1487")

    ChrTalk(    #24
        0x106,
        (
            "#054F#2P可恶……\x01",
            "这就是设计图上的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_1487")


    ChrTalk(    #25
        0x103,
        (
            "#024F#2P难不成……\x01",
            "这就是设计图上的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B4")


    ChrTalk(    #26
        0xF,
        (
            "#5P哈哈哈……\x01",
            "看来赶上了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "情、情报部荣光永存！\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x1, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FE, 0x0, 0x64)
    OP_7C(0x0, 0xCE4, 0xBB8, 0x64)
    PlayEffect(0x2, 0xFF, 0xFF, 40310, 1500, 54930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 4)
    OP_70(0x0, 0x1D)
    Sleep(500)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x1E)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x1E)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x1E)

    def lambda_15B3():
        OP_96(0xFE, 0x8110, 0x0, 0xD9B2, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15B3)

    def lambda_15D1():
        OP_96(0xFE, 0x8110, 0x0, 0xD476, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_15D1)

    def lambda_15EF():
        OP_96(0xFE, 0x7B70, 0x0, 0xD6D8, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15EF)
    Sleep(500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #28
        0x101,
        "#1014F呀啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        "#1070F这、这是……\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x3, 0x3, 0x11, -950, 2750, -1800, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, -950, 2800, -2370, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_16B7():
        OP_6D(40070, 1000, 54760, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16B7)

    def lambda_16CF():
        OP_67(0, 2600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16CF)

    def lambda_16E7():
        OP_6B(4190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16E7)

    def lambda_16F7():
        OP_6C(90000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16F7)

    def lambda_1707():
        OP_6E(243, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1707)
    OP_43(0xD, 0x1, 0x0, 0xD)
    OP_43(0xE, 0x1, 0x0, 0xE)
    OP_43(0xF, 0x1, 0x0, 0xF)
    OP_43(0x10, 0x1, 0x0, 0x10)
    OP_24(0x75, 0x64)

    def lambda_1737():

        label("loc_1737")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1737")

    QueueWorkItem2(0x11, 3, lambda_1737)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0xC, 0x20)
    OP_B0(0xC, 0xF)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)
    Sleep(300)

    def lambda_17D8():
        OP_8E(0x11, 0xA028, 0x3E8, 0xD69C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17D8)
    OP_22(0x110, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x4, 0x5, 0x11, 500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -500, 1500, -2000, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x11, 0x1)
    OP_23(0x110)
    OP_44(0x11, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x14)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #30
        0x101,
        "#1020F#5P战、战车……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18DA")

    ChrTalk(    #31
        0x106,
        "#057F#2P这就是『奥尔杰尤』……\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FE")

    label("loc_18DA")


    ChrTalk(    #32
        0x103,
        "#022F#2P这就是『奥尔杰尤』……\x02",
    )

    CloseMessageWindow()

    label("loc_18FE")

    OP_B0(0xC, 0xF)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)

    def lambda_1916():

        label("loc_1916")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1916")

    QueueWorkItem2(0x11, 3, lambda_1916)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_19A0():
        OP_8E(0x11, 0x8944, 0x0, 0xD5D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_19A0)
    OP_22(0x110, 0x0, 0x64)
    Sleep(300)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_19CA():
        OP_96(0xFE, 0x5DAC, 0x0, 0xD6EC, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19CA)
    Sleep(50)

    def lambda_19ED():
        OP_96(0xFE, 0x61BC, 0x0, 0xD412, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_19ED)
    Sleep(50)

    def lambda_1A10():
        OP_96(0xFE, 0x61C6, 0x0, 0xD926, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A10)
    Sleep(50)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x11, 0x1)
    OP_23(0x110)
    OP_44(0x11, 0x3)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_6F(0xC, 1)
    OP_70(0xC, 0x14)
    Fade(1000)
    OP_6D(31230, 0, 53830, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(135000, 0)
    OP_6E(538, 0)
    OP_0D()
    OP_72(0xC, 0x20)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0xC, 371)
    OP_70(0xC, 0x186)
    OP_73(0xC)
    OP_73(0xC)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x1)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x9, 35050, 2000, 56100, 270)

    def lambda_1AF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1AF3)
    OP_8F(0x9, 0x88EA, 0xA28, 0xDB24, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        (
            "#1181F#6P如何呢……\x01",
            "这个『奥尔杰尤』？\x02\x03",

            "由情报部独自开发，\x01",
            "最新型的高机动导力战车哦。\x02\x03",

            "火力是帝国制战车的２倍──\x01",
            "几乎能与警备飞艇相匹敌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1068F#2P又搞出这么离谱的东西……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1009F#5P乱、乱七八糟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#1181F#6P由于没找到启动这个\x01",
            "的高输出引擎，\x01",
            "在差一步就完成的时候，引擎被王室收回了……\x02\x03",

            "真没想到能够获得要用在『埃尔赛尤』\x01",
            "上的新型引擎啊。\x02\x03",

            "哈哈哈，空之女神\x01",
            "好像对我微笑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1005F#2P慢、慢着……\x02\x03",

            "你用这种东西\x01",
            "想干什么啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#1181F#6P我说过了吧。\x01",
            "为了帮助公爵阁下即位。\x02\x03",

            "为此必须获得\x01",
            "女王陛下的认可。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1020F#2P难、难道……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7C")

    ChrTalk(    #40
        0x106,
        "#054F#2P目标是城堡里的女王吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DA4")

    label("loc_1D7C")


    ChrTalk(    #41
        0x103,
        "#024F#2P目标是城堡里的女王陛下！？\x02",
    )

    CloseMessageWindow()

    label("loc_1DA4")


    ChrTalk(    #42
        0x9,
        (
            "#1188F#6P哈哈哈！\x01",
            "你们现在明白也晚了！\x02\x03",

            "奥尔杰尤号\x01",
            "可以轻易粉碎城门！\x02\x03",

            "全城的部队也不是对手！\x02\x03",

            "你们就咬着手指\x01",
            "乖乖在一边看着吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E30():
        OP_69(0x11, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E30)
    OP_8F(0x9, 0x88EA, 0x7D0, 0xDB24, 0x7D0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0x9, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    OP_6F(0xC, 391)
    OP_70(0xC, 0x19A)
    OP_73(0xC)

    def lambda_1E78():

        label("loc_1E78")

        OP_69(0x11, 0x0)
        OP_48()
        Jump("loc_1E78")

    QueueWorkItem2(0x11, 1, lambda_1E78)
    OP_B0(0xC, 0xF)
    OP_71(0xC, 0x20)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)

    def lambda_1EA0():

        label("loc_1EA0")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1EA0")

    QueueWorkItem2(0x11, 3, lambda_1EA0)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_8E(0x11, 0x7E0E, 0x0, 0xD5D4, 0x7D0, 0x0)

    def lambda_1F3E():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F3E)

    def lambda_1F4E():
        OP_8E(0xFE, 0x53CA, 0x0, 0xD5D4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1F4E)
    OP_22(0x110, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_1FA9():
        OP_96(0xFE, 0x6482, 0x0, 0xE7F4, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FA9)
    Sleep(50)

    def lambda_1FCC():
        OP_96(0xFE, 0x6446, 0x0, 0xC576, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1FCC)
    Sleep(50)

    def lambda_1FEF():
        OP_96(0xFE, 0x5D70, 0x0, 0xE772, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FEF)

    def lambda_200D():

        label("loc_200D")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_200D")

    QueueWorkItem2(0x101, 3, lambda_200D)

    def lambda_201E():

        label("loc_201E")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_201E")

    QueueWorkItem2(0xF7, 2, lambda_201E)

    def lambda_202F():

        label("loc_202F")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_202F")

    QueueWorkItem2(0x109, 2, lambda_202F)
    WaitChrThread(0x11, 0x2)
    OP_43(0x11, 0x2, 0x0, 0x11)

    def lambda_204C():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_204C)
    OP_6F(0xC, 61)
    OP_70(0xC, 0x50)
    OP_22(0x1FE, 0x0, 0x64)
    Sleep(100)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x1E)
    OP_6F(0x8, 1)
    OP_70(0x8, 0x1E)
    Sleep(10)
    OP_6F(0x2, 1)
    OP_70(0x2, 0x1E)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x1E)
    OP_44(0x11, 0x1)

    def lambda_20B3():

        label("loc_20B3")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_20B3")

    QueueWorkItem2(0x11, 0, lambda_20B3)
    Sleep(4000)
    OP_24(0x10F, 0x5A)
    OP_24(0x110, 0x5A)
    Sleep(100)
    OP_24(0x10F, 0x50)
    OP_24(0x110, 0x50)
    Sleep(100)
    OP_24(0x10F, 0x46)
    OP_24(0x110, 0x46)
    Sleep(100)
    OP_24(0x10F, 0x3C)
    OP_24(0x110, 0x3C)
    Sleep(100)
    OP_24(0x10F, 0x32)
    OP_24(0x110, 0x32)
    Sleep(100)
    OP_24(0x10F, 0x28)
    OP_24(0x110, 0x28)
    Sleep(100)
    OP_24(0x10F, 0x1E)
    OP_24(0x110, 0x1E)
    Sleep(100)
    OP_24(0x10F, 0x14)
    OP_24(0x110, 0x14)
    Sleep(100)
    OP_24(0x10F, 0xA)
    OP_24(0x110, 0xA)
    Sleep(100)
    OP_23(0x10F)
    OP_23(0x110)
    WaitChrThread(0x11, 0x2)
    Fade(1000)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    OP_6D(23950, 0, 55930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x11, 0x0)
    OP_8C(0x109, 225, 0)
    OP_0D()
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)

    ChrTalk(    #43
        0x101,
        "#1020F#6P糟、糟了……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EF")

    ChrTalk(    #44
        0x106,
        "#054F#5P快追！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2203")

    label("loc_21EF")


    ChrTalk(    #45
        0x103,
        "#024F#5P快追！\x02",
    )

    CloseMessageWindow()

    label("loc_2203")


    def lambda_2209():
        OP_8E(0xFE, 0x448E, 0x0, 0xC9EA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2209)
    Sleep(100)

    def lambda_2229():
        OP_8E(0xFE, 0x3C1E, 0x0, 0xC3E6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2229)
    Sleep(100)

    def lambda_2249():
        OP_8E(0xFE, 0x3F84, 0x0, 0xC45E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2249)
    Sleep(1000)
    WaitChrThread(0xF7, 0x1)

    def lambda_226E():
        OP_8E(0xFE, 0x3C5A, 0x0, 0xBFFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_226E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)

    def lambda_22A3():

        label("loc_22A3")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_22A3")

    QueueWorkItem2(0x11, 0, lambda_22A3)
    SetChrPos(0x11, 13560, 0, 45760, 180)
    PlayEffect(0x0, 0x1, 0x11, 2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, -2000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(13560, 0, 45760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(32000, 0)
    OP_6E(262, 0)

    def lambda_2376():

        label("loc_2376")

        OP_69(0x11, 0x0)
        OP_48()
        Jump("loc_2376")

    QueueWorkItem2(0x11, 2, lambda_2376)
    OP_22(0x10F, 0x0, 0x64)
    OP_22(0x110, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_8E(0x11, 0x34F8, 0x0, 0x8520, 0x1194, 0x0)
    OP_43(0x11, 0x1, 0x0, 0x12)

    def lambda_23B5():
        OP_8C(0xFE, 270, 52)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_23B5)
    OP_22(0x1FE, 0x0, 0x64)
    Sleep(200)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x1E)
    Sleep(10)
    OP_6F(0x5, 1)
    OP_70(0x5, 0x1E)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x1E)
    WaitChrThread(0x11, 0x1)
    OP_43(0x11, 0x1, 0x0, 0x13)
    OP_8C(0x11, 180, 60)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_24(0x75, 0x5A)
    Sleep(100)
    OP_24(0x75, 0x50)
    Sleep(100)
    OP_24(0x75, 0x46)
    Sleep(100)
    OP_24(0x75, 0x3C)
    Sleep(100)
    OP_24(0x75, 0x32)
    Sleep(100)
    OP_24(0x75, 0x28)
    Sleep(100)
    OP_24(0x75, 0x1E)
    Sleep(100)
    OP_24(0x75, 0x14)
    Sleep(100)
    OP_24(0x75, 0xA)
    Sleep(100)
    OP_23(0x75)
    WaitChrThread(0x11, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4403   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1058 end

    def Function_13_2483(): pass

    label("Function_13_2483")

    Sleep(100)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x9100, 0x0, 0xE7F4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_13_2483 end

    def Function_14_24C5(): pass

    label("Function_14_24C5")

    Sleep(150)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 12)
    OP_8E(0xFE, 0x915A, 0x0, 0xC468, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9182, 0x0, 0xC4AE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 13)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_14_24C5 end

    def Function_15_251B(): pass

    label("Function_15_251B")

    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x9448, 0x0, 0xEA88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x96BE, 0x0, 0xEA56, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_15_251B end

    def Function_16_256C(): pass

    label("Function_16_256C")

    Sleep(50)
    OP_99(0xFE, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xFE, 16)
    OP_8E(0xFE, 0x93A8, 0x0, 0xC440, 0x7D0, 0x0)
    OP_8E(0xFE, 0x96DC, 0x0, 0xC4C2, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 17)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    SetChrSubChip(0xFE, 3)
    Return()

    # Function_16_256C end

    def Function_17_25C2(): pass

    label("Function_17_25C2")

    OP_8F(0xFE, 0x3CC8, 0x0, 0xBEBE, 0x1194, 0x0)
    OP_6F(0xC, 21)
    OP_70(0xC, 0x28)
    OP_8F(0xFE, 0x38E0, 0x0, 0x88B8, 0x1194, 0x0)
    Return()

    # Function_17_25C2 end

    def Function_18_25F9(): pass

    label("Function_18_25F9")

    OP_8F(0xFE, 0x2184, 0x0, 0x690A, 0x1194, 0x0)
    OP_8F(0xFE, 0x94C, 0x0, 0x6522, 0x1194, 0x0)
    Return()

    # Function_18_25F9 end

    def Function_19_2622(): pass

    label("Function_19_2622")

    OP_8F(0xFE, 0xFFFFFC36, 0x0, 0x4C68, 0x1194, 0x0)
    OP_8F(0xFE, 0xFFFFFD8A, 0x0, 0xFFFFDDBE, 0x1194, 0x0)
    Return()

    # Function_19_2622 end

    def Function_20_264B(): pass

    label("Function_20_264B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26C5"),
        (1, "loc_26CB"),
        (SWITCH_DEFAULT, "loc_26D1"),
    )


    label("loc_26C5")

    OP_A2(0x1200)
    Jump("loc_26D1")

    label("loc_26CB")

    OP_A2(0x1201)
    Jump("loc_26D1")

    label("loc_26D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26DF")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_26E3")

    label("loc_26DF")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_26E3")

    Return()

    # Function_20_264B end

    SaveToFile()

Try(main)
