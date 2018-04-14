from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2301   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2301.x',
        MapIndex            = 102,
        MapDefaultBGM       = "ed60021",
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
        '卡露娜',                               # 9
        '库拉茨',                               # 10
        '亡命守护者',                           # 11
        '亡命守护者',                           # 12
        '亡命守护者',                           # 13
        '亡命守护者',                           # 14
        '梅威海道方向',                         # 15
        '杰尼丝王立学院方向',                   # 16
        '水银蝰蛇',                             # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
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
        'ED6_DT09/CH10520 ._CH',             # 00
        'ED6_DT09/CH10521 ._CH',             # 01
        'ED6_DT29/CH12040 ._CH',             # 02
        'ED6_DT29/CH12041 ._CH',             # 03
        'ED6_DT09/CH10340 ._CH',             # 04
        'ED6_DT09/CH10341 ._CH',             # 05
        'ED6_DT09/CH11040 ._CH',             # 06
        'ED6_DT09/CH11041 ._CH',             # 07
        'ED6_DT09/CH11070 ._CH',             # 08
        'ED6_DT09/CH11071 ._CH',             # 09
        'ED6_DT09/CH11080 ._CH',             # 0A
        'ED6_DT09/CH11081 ._CH',             # 0B
        'ED6_DT29/CH12320 ._CH',             # 0C
        'ED6_DT07/CH01240 ._CH',             # 0D
        'ED6_DT07/CH01260 ._CH',             # 0E
        'ED6_DT09/CH11250 ._CH',             # 0F
        'ED6_DT09/CH11251 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10520P._CP',             # 00
        'ED6_DT09/CH10521P._CP',             # 01
        'ED6_DT29/CH12040P._CP',             # 02
        'ED6_DT29/CH12041P._CP',             # 03
        'ED6_DT09/CH10340P._CP',             # 04
        'ED6_DT09/CH10341P._CP',             # 05
        'ED6_DT09/CH11040P._CP',             # 06
        'ED6_DT09/CH11041P._CP',             # 07
        'ED6_DT09/CH11070P._CP',             # 08
        'ED6_DT09/CH11071P._CP',             # 09
        'ED6_DT09/CH11080P._CP',             # 0A
        'ED6_DT09/CH11081P._CP',             # 0B
        'ED6_DT29/CH12320P._CP',             # 0C
        'ED6_DT07/CH01240P._CP',             # 0D
        'ED6_DT07/CH01260P._CP',             # 0E
        'ED6_DT09/CH11250P._CP',             # 0F
        'ED6_DT09/CH11251P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 128320,
        Z                   = 20,
        Y                   = -8070,
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

    DeclNpc(
        X                   = 288640,
        Z                   = 10,
        Y                   = -9980,
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

    DeclNpc(
        X                   = 219810,
        Z                   = 770,
        Y                   = -59460,
        Direction           = 332,
        Unknown2            = 15,
        Unknown3            = 983040,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 164610,
        Z                   = 540,
        Y                   = -8970,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 161500,
        Z                   = -30,
        Y                   = -7250,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x196,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 193850,
        Z                   = 320,
        Y                   = -43450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 218740,
        Z                   = 0,
        Y                   = -37100,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x195,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 235120,
        Z                   = -10,
        Y                   = -3610,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x193,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 230490,
        Z                   = 130,
        Y                   = -5740,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x194,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 210450,
        Z                   = 10,
        Y                   = -27270,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x195,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 219810,
        Y                   = -1000,
        Z                   = -59460,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    ScpFunction(
        "Function_0_336",          # 00, 0
        "Function_1_388",          # 01, 1
        "Function_2_3CB",          # 02, 2
        "Function_3_3E1",          # 03, 3
        "Function_4_59C",          # 04, 4
        "Function_5_13CC",         # 05, 5
        "Function_6_1493",         # 06, 6
        "Function_7_14D4",         # 07, 7
        "Function_8_2D6B",         # 08, 8
        "Function_9_2D87",         # 09, 9
        "Function_10_2DA3",        # 0A, 10
        "Function_11_2DC4",        # 0B, 11
        "Function_12_2DE5",        # 0C, 12
        "Function_13_2E06",        # 0D, 13
        "Function_14_2E27",        # 0E, 14
        "Function_15_31A2",        # 0F, 15
        "Function_16_3220",        # 10, 16
        "Function_17_3289",        # 11, 17
        "Function_18_32F2",        # 12, 18
        "Function_19_335B",        # 13, 19
        "Function_20_33C4",        # 14, 20
        "Function_21_3991",        # 15, 21
        "Function_22_3A18",        # 16, 22
    )


    def Function_0_336(): pass

    label("Function_0_336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_352")
    OP_A3(0x10F0)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_387")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_36E")
    OP_A3(0x10F1)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_387")

    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_387")
    OP_A3(0x10F2)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)

    label("loc_387")

    Return()

    # Function_0_336 end

    def Function_1_388(): pass

    label("Function_1_388")

    OP_16(0x2, 0xFA0, 0x14C08, 0xFFFDA670, 0x23002A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B8")
    SetChrFlags(0x10, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_3CA")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CA")
    ClearChrFlags(0x10, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_3CA")

    Return()

    # Function_1_388 end

    def Function_2_3CB(): pass

    label("Function_2_3CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3CB")

    label("loc_3E0")

    Return()

    # Function_2_3CB end

    def Function_3_3E1(): pass

    label("Function_3_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 2)), scpexpr(EXPR_END)), "loc_3E9")
    Return()

    label("loc_3E9")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4CE"),
        (SWITCH_DEFAULT, "loc_4F1"),
    )


    label("loc_4CE")

    Fade(500)
    OP_89(0x0, 217320, -20, -51680, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_4F1")

    Battle(0xEDD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 217320, -20, -51680, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_52A"),
        (1, "loc_52D"),
        (SWITCH_DEFAULT, "loc_530"),
    )


    label("loc_52A")

    EventEnd(0x0)
    Return()

    label("loc_52D")

    OP_B4(0x0)
    Return()

    label("loc_530")

    EventBegin(0x1)
    SetChrFlags(0x10, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x12FA)
    OP_28(0xA1, 0x4, 0x10)
    OP_28(0xA1, 0x4, 0x2)
    OP_28(0xA1, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_3E1 end

    def Function_4_59C(): pass

    label("Function_4_59C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 21)
    Call(0, 22)

    label("loc_5B3")

    Call(0, 5)
    OP_6D(271510, 20, -9370, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    SetChrPos(0xA, 269300, 750, -11440, 270)
    SetChrPos(0xB, 269300, 750, -9000, 270)
    SetChrPos(0xC, 272070, 750, -12200, 270)
    SetChrPos(0xD, 272290, 750, -7890, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 237740, 100, -15610, 90)
    SetChrPos(0x102, 237590, 200, -16730, 90)
    SetChrPos(0x103, 236640, -30, -15660, 90)
    SetChrPos(0x108, 235150, -120, -16610, 90)
    SetChrPos(0x107, 236340, 10, -17100, 90)
    SetChrPos(0x106, 236570, 310, -18350, 90)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_6E3():
        OP_6D(237450, 80, -15960, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E3)

    def lambda_6FB():
        OP_67(0, 6890, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FB)

    def lambda_713():
        OP_6B(2450, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_713)

    def lambda_723():
        OP_6E(332, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_723)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_789")

    ChrTalk(    #2
        0x106,
        (
            "#053F#6P听说了情况\x01",
            "就火速赶来……\x02\x03",

            "#057F看来状况相当不妙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7DF")

    ChrTalk(    #3
        0x103,
        (
            "#026F#6P还好听说了情况\x01",
            "就火速赶来……\x02\x03",

            "#022F看来状况相当危险啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_832")

    label("loc_7DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(    #4
        0x108,
        (
            "#074F#6P还好听说了情况\x01",
            "就火速赶来……\x02\x03",

            "#072F看来状况相当严峻啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_832")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #5
        0x107,
        (
            "#065F#6P虽、虽然让嘉恩先生\x01",
            "联络了王国军……\x02\x03",

            "但是他说援军前来\x01",
            "可能要花费一点时间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94D")

    label("loc_89C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(    #6
        0x108,
        (
            "#072F#6P接待处的小哥\x01",
            "已经联络了王国军……\x02\x03",

            "但援军似乎不可能马上就到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94D")

    label("loc_8F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_94D")

    ChrTalk(    #7
        0x103,
        (
            "#022F#6P虽然让嘉恩先生\x01",
            "联络了王国军……\x02\x03",

            "但援军似乎不可能马上就到。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94D")

    OP_8C(0x101, 225, 400)

    ChrTalk(    #8
        0x101,
        "#1003F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A03")

    ChrTalk(    #9
        0x108,
        (
            "#074F#6P无论如何，既然导力兵器也不能用，\x01",
            "军方的部队来了也帮不上什么忙吧。\x02\x03",

            "#072F看来只能靠习惯白刃战的我们\x01",
            "来解决这一次的事件了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2D")

    label("loc_A03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9E")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #10
        0x106,
        (
            "#053F#6P无论如何，既然导力兵器也不能用，\x01",
            "军方的部队来了也帮不上什么忙啊。\x02\x03",

            "#050F只能靠习惯白刃战的我们\x01",
            "来解决这一次的事件了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2D")

    label("loc_A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2D")

    ChrTalk(    #11
        0x103,
        (
            "#026F#6P无论如何，既然导力兵器也不能用，\x01",
            "军方的部队来了也帮不上什么忙。\x02\x03",

            "#022F只能靠习惯白刃战的我们\x01",
            "来解决这一次的事件了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B83")

    ChrTalk(    #12
        0x107,
        (
            "#065F#6P但、但是，学院的人们\x01",
            "好像被抓起来了……\x02\x03",

            "怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_B83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDF")

    ChrTalk(    #13
        0x103,
        (
            "#522F#6P只是，学院的相关人员\x01",
            "肯定是被抓起来了。\x02\x03",

            "轻举妄动就很危险吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C43")

    label("loc_BDF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C43")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #14
        0x106,
        (
            "#552F#4P只是，学院的相关人员\x01",
            "被抓起来的可能性很高。\x02\x03",

            "轻举妄动也很不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C43")


    ChrTalk(    #15
        0x101,
        (
            "#1007F#5P确实……\x02\x03",

            "#1003F要是能想办法\x01",
            "搞清楚内部的状况了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1042F#5P………………………………\x02\x03",

            "#1035F……稍等一下。\x01",
            "我去调查学院内的情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_D6B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_D6B)

    def lambda_D79():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D79)
    Sleep(100)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #17
        0x101,
        "#1004F约、约修亚？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        "#022F#6P……什么意思？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #19
        0x102,
        (
            "#1040F#2P侦察之类的隐密活动\x01",
            "是我最为擅长的领域。\x02\x03",

            "我想应该可以将敌方战力\x01",
            "和人质的状况都调查出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        "#555F#4P原来如此啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x108,
        (
            "#074F#6P唔，能办到的话\x01",
            "那就务必麻烦你跑一趟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#065F#6P但、但是！\x01",
            "这不是很危险吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040F#2P没问题，我过去曾经在\x01",
            "更严苛的状况下进行过潜入活动。\x02\x03",

            "不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        "#063F#6P但、但是但是～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(    #25
        0x101,
        (
            "#1002F#5P……约修亚。\x01",
            "你真的坚持一个人去吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #26
        0x102,
        (
            "#1043F#4P单独行动\x01",
            "反而成功率比较高。\x02\x03",

            "#1042F还是让我一个人去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1010F#5P是吗……\x02\x03",

            "#1002F……那我就确认一件事。\x02\x03",

            "那时候的约定……\x01",
            "你还记得吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1053F#4P一起走到最后，对吧。\x02\x03",

            "#1054F没问题──我绝对不会忘记的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F#5P嗯，那就行了！\x02\x03",

            "#1025F约修亚……\x01",
            "你要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1053F#4P嗯，我明白。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #31
        0x102,
        "#1040F#2P那么我去了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_10E4():

        label("loc_10E4")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_10E4")

    QueueWorkItem2(0x101, 2, lambda_10E4)

    def lambda_10F5():

        label("loc_10F5")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_10F5")

    QueueWorkItem2(0x103, 2, lambda_10F5)

    def lambda_1106():

        label("loc_1106")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1106")

    QueueWorkItem2(0x107, 2, lambda_1106)

    def lambda_1117():

        label("loc_1117")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1117")

    QueueWorkItem2(0x106, 2, lambda_1117)

    def lambda_1128():

        label("loc_1128")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1128")

    QueueWorkItem2(0x108, 2, lambda_1128)

    def lambda_1139():
        OP_6D(244310, 100, -18660, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1139)

    def lambda_1151():
        OP_67(0, 4870, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1151)

    def lambda_1169():
        OP_6B(2770, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1169)

    def lambda_1179():
        OP_6C(105000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1179)

    def lambda_1189():
        OP_6E(371, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1189)
    OP_D2(0x2600FC, 0x260101, 0x13)
    SetChrFlags(0x102, 0x4)
    OP_8E(0x102, 0x3A5AC, 0x3E8, 0xFFFFBCD0, 0x1388, 0x0)
    OP_8E(0x102, 0x3C00A, 0x3E8, 0xFFFFAECA, 0x1388, 0x0)
    SetChrChipByIndex(0x102, 19)
    SetChrSubChip(0x102, 1)
    Sleep(500)
    SetChrSubChip(0x102, 0)
    OP_7D(0x0, 0x102, 0x14, 0x1F4)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x1000)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_11FB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_11FB)
    OP_8F(0x102, 0x3C00A, 0x1388, 0xFFFFAECA, 0x2710, 0x0)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_44(0x101, 0x2)
    OP_44(0x103, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0x106, 0x2)
    OP_44(0x108, 0x2)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(237450, 80, -15960, 0)
    OP_67(0, 6890, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    OP_0D()
    OP_8C(0x106, 0, 400)
    Sleep(500)

    ChrTalk(    #32
        0x106,
        "#552F喂……没问题吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(300)

    ChrTalk(    #33
        0x101,
        (
            "#1025F……嗯。\x02\x03",

            "这种情况下跟去\x01",
            "反而会变成累赘。\x02\x03",

            "#1012F而且……\x01",
            "我相信约修亚。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1316():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1316)
    Sleep(100)

    def lambda_1329():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1329)
    Sleep(100)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #34
        0x107,
        "#560F#6P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x103,
        (
            "#027F#6P呵呵……\x01",
            "真是变成了一个越来越有魅力的女性了嘛。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 6)
    ClearParty()
    AddParty(0x1, 0xF6, 0xFF)
    OP_A2(0x2013)
    OP_28(0xC0, 0x4, 0x2)
    OP_28(0xC0, 0x4, 0x8)
    OP_28(0xC0, 0x1, 0x1)
    SetMapFlags(0x2000000)
    OP_A2(0x10FE)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2500   ._SN", 124, 0, 0)
    IdleLoop()
    Return()

    # Function_4_59C end

    def Function_5_13CC(): pass

    label("Function_5_13CC")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1405")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1405")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1426")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_142A")

    label("loc_1426")

    AddParty(0x5, 0xFB, 0xFF)

    label("loc_142A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_143E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1477")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145F")
    AddParty(0x6, 0xFA, 0xFF)
    Jump("loc_1463")

    label("loc_145F")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_1463")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1477")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1492")
    AddParty(0x7, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_1492")

    Return()

    # Function_5_13CC end

    def Function_6_1493(): pass

    label("Function_6_1493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14A3")
    RemoveParty(0x2, 0xFF)

    label("loc_14A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14B3")
    RemoveParty(0x5, 0xFF)

    label("loc_14B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14C3")
    RemoveParty(0x6, 0xFF)

    label("loc_14C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_14D3")
    RemoveParty(0x7, 0xFF)

    label("loc_14D3")

    Return()

    # Function_6_1493 end

    def Function_7_14D4(): pass

    label("Function_7_14D4")

    EventBegin(0x0)
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0xD, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    SetChrFlags(0x10E, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_6D(235560, 50, -19240, 0)
    OP_67(0, 4780, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(45000, 0)
    OP_6E(427, 0)
    SetChrPos(0x102, 235850, 100, -20090, 270)
    SetChrPos(0x101, 233750, 10, -20340, 90)
    SetChrPos(0x107, 234430, -10, -21490, 45)
    SetChrPos(0x103, 234550, -10, -19020, 135)
    SetChrPos(0x106, 233180, 10, -21580, 90)
    SetChrPos(0x108, 233000, 30, -19660, 90)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x102,
        (
            "#1040F#2P……以上就是在侦察中\x01",
            "所得知的学院内大致的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        (
            "#070F#6P是吗……\x01",
            "调查得很清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#051F啊啊，这下\x01",
            "总算能制定详细的作战计划了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1007F#6P不过，想不到那个基尔巴特\x01",
            "居然是袭击学院的罪魁祸首……\x02\x03",

            "#1019F而且似乎\x01",
            "还想抓走科洛丝～？\x02\x03",

            "#1022F在『方舟』见到时，\x01",
            "就该把他揍个\x01",
            "满地找牙才对！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#026F#5P过去是才华横溢的市长秘书，\x01",
            "现在变成了『结社』的走狗吗……\x02\x03",

            "#524F感觉这是一个曾经的精英人物\x01",
            "在遭受挫折后人格扭曲的典型例子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007F#6P嗯，没错。\x02\x03",

            "#1015F……不过，怎么办呢。\x02\x03",

            "士兵的数量也相当多，\x01",
            "还有人偶兵器和装甲兽吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        (
            "#065F而且，既然有人偶兵器\x01",
            "在活动……\x02\x03",

            "这就是说『结社』的人，在这种状况下\x01",
            "还有可能使用导力器吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1035F#2P看来好像使用了\x01",
            "和博士发明的『零力场发生器』\x01",
            "相同的技术。\x02\x03",

            "#1042F而且似乎还没有数量限制。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#052F#6P这么说来，他们可以\x01",
            "随心所欲地使用枪或魔法了……\x02\x03",

            "#057F还真是有点棘手啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #46
        0x103,
        (
            "#026F#5P嗯，虽然很麻烦，\x01",
            "但还是兵分两路吧。\x02\x03",

            "#020F从正面诱出敌方战力，\x01",
            "再由别动队从后方突袭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x108,
        (
            "#074F#6P不过，要这么做\x01",
            "战斗力有点不足啊。\x02\x03",

            "#072F正面攻击的人\x01",
            "至少要６个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        (
            "#1043F#2P是啊……\x02\x03",

            "#1035F这样的人数应该就可以把\x01",
            "待命中的士兵吸引到这边来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1007F#6P不过６个人……\x01",
            "不是这里全部人数吗。\x02\x03",

            "#1015F还是只能像这样子\x01",
            "等待王国军部队抵达呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10E, 221680, -40, -19680, 90)
    SetChrPos(0x10A, 221970, -50, -21480, 45)
    SetChrPos(0x8, 220360, -20, -21540, 45)
    SetChrPos(0x9, 220510, 30, -20230, 45)

    NpcTalk(    #50
        0x10E,
        "男性的声音",
        (
            "#2P……这方面就\x01",
            "让我们来补足吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1B88():

        label("loc_1B88")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_1B88")

    QueueWorkItem2(0x101, 1, lambda_1B88)
    Sleep(50)

    def lambda_1B9E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1B9E)
    Sleep(50)

    def lambda_1BB1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1BB1)
    Sleep(50)

    def lambda_1BC4():

        label("loc_1BC4")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_1BC4")

    QueueWorkItem2(0x107, 1, lambda_1BC4)
    Sleep(50)

    def lambda_1BDA():

        label("loc_1BDA")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_1BDA")

    QueueWorkItem2(0x102, 1, lambda_1BDA)
    Sleep(50)

    def lambda_1BF0():

        label("loc_1BF0")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_1BF0")

    QueueWorkItem2(0x103, 1, lambda_1BF0)
    Sleep(50)
    Fade(1000)
    OP_6D(231990, 10, -19220, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(314000, 0)
    OP_6E(330, 0)
    SetChrPos(0x102, 235850, 100, -20090, 270)
    SetChrPos(0x101, 234240, 0, -20170, 90)
    SetChrPos(0x107, 234310, 0, -21170, 45)
    SetChrPos(0x103, 234590, -10, -18900, 135)
    SetChrPos(0x106, 233140, 20, -20930, 90)
    SetChrPos(0x108, 233260, 50, -19170, 90)
    OP_43(0x10E, 0x1, 0x0, 0xA)
    OP_43(0x10A, 0x1, 0x0, 0xB)
    OP_43(0x8, 0x1, 0x0, 0xC)
    OP_43(0x9, 0x1, 0x0, 0xD)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x108, 0)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x102, 0)
    Sleep(2000)
    OP_43(0x106, 0x1, 0x0, 0x8)
    OP_43(0x108, 0x1, 0x0, 0x9)
    WaitChrThread(0x9, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #51
        0x107,
        "#064F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1004F啊啊～！\x01",
            "亚妮拉丝你们！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x108,
        (
            "#071F#2P哈哈，你们来的\x01",
            "真是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#825F#5P嘿嘿，我们\x01",
            "刚刚到达卢安支部的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#835F#5P听嘉恩一说\x01",
            "就急急忙忙赶来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#021F真是的……\x01",
            "实在是求之不得的援军啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1DFF():
        OP_6D(233430, 30, -19680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DFF)

    def lambda_1E17():
        OP_67(0, 6760, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E17)

    def lambda_1E2F():
        OP_6B(2400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E2F)
    OP_8F(0x10A, 0x38CC0, 0x14, 0xFFFFB1EA, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #57
        0x10A,
        (
            "#1314F#5P……艾丝蒂尔。\x01",
            "在湖畔承蒙你解救后就没再见面了呢。\x02\x03",

            "那个时候真是多谢了。\x01",
            "在危机时刻救了我一命。\x02\x03",

            "#1316F那之后，听说艾丝蒂尔\x01",
            "被抓走了，\x01",
            "我真是十分抱歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1016F#4P啊哈哈，没关系，\x01",
            "反正我也平安无事啊。\x02\x03",

            "#1006F而且……\x01",
            "约修亚也回来了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10A,
        (
            "#1314F#5P是吗……\x02\x03",

            "#819F嘿嘿……\x01",
            "好久不见呢，约修亚！\x02\x03",

            "还记得姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1053F是……当然了。\x02\x03",

            "#1054F我不在的时候，\x01",
            "听说你们一直很照顾艾丝蒂尔。\x02\x03",

            "请务必让我表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10A,
        (
            "#816F#5P呵呵，添麻烦的\x01",
            "应该是我才对。\x02\x03",

            "#1311F话说回来我还想告诉你，\x01",
            "你不在的时候\x01",
            "艾丝蒂尔有多么寂寞……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1013F#4P慢、慢着～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10A,
        (
            "#1315F#5P嘿嘿，开玩笑啦。\x02\x03",

            "#816F……现在的状况\x01",
            "可容不得这么悠闲啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1007F#4P嗯……其实正是这样。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1015F#5P约修亚，再把学院内的情况\x01",
            "说一遍好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        "#1040F知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D2(0x2601B2, 0x2601B7, 0x11)
    Sleep(2000)
    SetChrPos(0x101, 233370, 10, -20870, 270)
    SetChrPos(0x102, 233420, 30, -19530, 270)
    SetChrPos(0x107, 234280, 0, -20840, 270)
    SetChrPos(0x103, 234500, 10, -19470, 270)
    SetChrPos(0x106, 234780, 20, -22300, 270)
    SetChrPos(0x108, 235690, 50, -21240, 270)
    SetChrPos(0x10A, 231370, 20, -20800, 90)
    OP_8C(0x102, 270, 0)
    OP_8C(0x101, 270, 0)
    OP_6D(231700, 0, -19410, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(314000, 0)
    OP_6E(334, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #67
        0x10E,
        (
            "#843F#5P原来如此……这样的情况啊。\x02\x03",

            "#842F的确需要兵分两路\x01",
            "来迅速解决目前的事态才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#824F#5P这么一来就有１０个人了……\x02\x03",

            "#820F分成正面６人，\x01",
            "后方４人应该可以吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x106,
        (
            "#053F嗯，比较妥当。\x02\x03",

            "#051F问题在于\x01",
            "要如何分组……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1004F啊，既然这样，\x01",
            "我就从后方突袭吧。\x02\x03",

            "#1016F因为这个学院\x01",
            "我比其它人都要熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1035F我也一样。\x02\x03",

            "#1040F毕竟刚刚才\x01",
            "潜入侦查过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10A,
        (
            "#1310F#5P那么我也加入\x01",
            "后方的突袭组吧？\x02\x03",

            "#811F之前和艾丝蒂尔\x01",
            "约定要一起作战的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#1025F亚妮拉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020F从隐蔽性方面考虑\x01",
            "确实是十分合适。\x02\x03",

            "#026F不过，你们３个\x01",
            "都是近身作战的类型……\x02\x03",

            "#027F要有个能做后援\x01",
            "的人同行就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10E,
        (
            "#843F#5P那就让我来吧。\x02\x03",

            "#841F我应该可以用方术\x01",
            "支持艾丝蒂尔他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1011F克鲁茨前辈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        "#1040F拜托你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x106,
        (
            "#051F哦，看来决定了嘛。\x02\x03",

            "#052F说到这个，卡露娜……\x01",
            "你的武器没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#833F#5P啊啊，导力枪是吧。\x02\x03",

            "#835F确实是伤脑筋，\x01",
            "所以我准备了这个东西。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 17)
    SetChrSubChip(0x8, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #80
        0x101,
        "#1004F那、那么大一把枪是！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#064F啊，那个难不成是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#831F#5P呵呵，是莱恩福尔特社\x01",
            "制造的火药式突击步枪哦。\x02\x03",

            "原本是武器店的爱珐小姐\x01",
            "所收藏的古董。\x02\x03",

            "被我强行借来使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        "#051F这实在是难得一见的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#027F没记错的话，火药式的枪\x01",
            "现在根本见不到了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 400)
    Sleep(300)

    ChrTalk(    #85
        0x103,
        (
            "#023F#2P对了，提妲用的也是\x01",
            "火药式的机关炮吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 400)
    Sleep(300)

    ChrTalk(    #86
        0x107,
        (
            "#061F#6P嘿嘿，是的。\x02\x03",

            "#560F爷爷借给我的\x01",
            "珍贵收藏品。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_275B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_275B)
    Sleep(100)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #87
        0x8,
        (
            "#833F#5P老实说，和导力枪相比…\x01",
            "不但很重，子弹也耗尽得很快，\x01",
            "使用起来十分不方便呢。\x02\x03",

            "#830F不过威力不容小觑，\x01",
            "应该足够用于实战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x108,
        (
            "#074F#4P唔，那么正面的\x01",
            "佯攻组看来也没问题了。\x02\x03",

            "#070F立刻开始作战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1018FＯＫ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10A,
        "#816F#5P加油！\x02",
    )

    CloseMessageWindow()
    OP_31(0xD, 0x0, 0x4F)
    OP_31(0xD, 0xFE, 0x0)
    OP_41(0xD, 0xAA, 0xFF)
    OP_41(0xD, 0x105, 0xFF)
    OP_41(0xD, 0x126, 0xFF)
    OP_37(0xD, 0x7F, 0x2)
    OP_41(0xD, 0x25D, 0x0)
    OP_41(0xD, 0x25A, 0x2)
    OP_41(0xD, 0x2CA, 0x3)
    OP_41(0xD, 0x260, 0x4)
    OP_41(0xD, 0x263, 0x5)
    OP_35(0xD, 0x0)
    OP_BB(0xD, 0x6, 0x118)
    OP_31(0x9, 0x0, 0x4D)
    OP_31(0x9, 0xFE, 0x0)
    OP_41(0x9, 0xD0, 0xFF)
    OP_41(0x9, 0x105, 0xFF)
    OP_41(0x9, 0x126, 0xFF)
    OP_37(0x9, 0x7F, 0x2)
    OP_41(0x9, 0x2C3, 0x0)
    OP_41(0x9, 0x2CA, 0x1)
    OP_41(0x9, 0x263, 0x2)
    OP_41(0x9, 0x26E, 0x4)
    OP_41(0x9, 0x25A, 0x5)
    OP_35(0x9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A3(0x0)

    label("loc_28F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B2D")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #91
        (
            "\x06\x18\x07\x05※进行队伍的重新编组。\x01",
            "　更换队员，进行必要的装备变更，\x01",
            "　确定后，请选择【继续】。\x01",
            "　艾丝蒂尔、约修亚、亚妮拉丝和克鲁茨组队前进。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【编成队伍】\x01",      # 0
            "【变更装备】\x01",      # 1
            "【继续】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A60")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #92
        (
            "\x07\x05※进行暂时的队伍编组。\x01",
            "　可以卸下其它同伴的装备给\x01",
            "　亚妮拉丝等人装配。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0x9, 0xD, 0xFFFF)
    Jump("loc_2B2A")

    label("loc_2A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2A99")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_2AC4")

    label("loc_2A99")


    AnonymousTalk(    #93
        "\x07\x05※进行队伍的编组之后再选择。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_2AC4")

    Jump("loc_2B2A")

    label("loc_2AC7")

    SetChrName("")

    AnonymousTalk(    #94
        "\x06\x18\x07\x05※可以继续剧情了吗？\x07\x00\x02",
    )

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
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2A")
    Jump("loc_2B2D")

    label("loc_2B2D")

    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x05就这样，协会的学院解放作战开始了。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #96
        (
            "\x07\x05阿加特、雪拉扎德、金、\x01",
            "卡露娜、库拉茨和提妲６人，\x01",
            "从正面将强化猎兵引诱出来……\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #97
        (
            "\x07\x05艾丝蒂尔、约修亚、亚妮拉丝和克鲁茨，\x01",
            "则是负责从背后突袭并解放人质。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(200)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    AddParty(0x9, 0xF8, 0xFF)
    AddParty(0xD, 0xF9, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C35")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C50")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2C50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C6B")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C86")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA1")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2CA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBC")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2CBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD7")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2CD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF2")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_2CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D5E")
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #98
        (
            "\x07\x05※待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　将其回收加入队伍的携带品。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2D5E")

    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_2B2A")

    Jump("loc_28F7")

    # Function_7_14D4 end

    def Function_8_2D6B(): pass

    label("Function_8_2D6B")

    OP_8F(0xFE, 0x390E4, 0x0, 0xFFFFAA74, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_8_2D6B end

    def Function_9_2D87(): pass

    label("Function_9_2D87")

    OP_8F(0xFE, 0x38F4A, 0x14, 0xFFFFB7F8, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_9_2D87 end

    def Function_10_2DA3(): pass

    label("Function_10_2DA3")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x38770, 0xFFFFFFF6, 0xFFFFB4B0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_2DA3 end

    def Function_11_2DC4(): pass

    label("Function_11_2DC4")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x387CA, 0x14, 0xFFFFAEC0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_2DC4 end

    def Function_12_2DE5(): pass

    label("Function_12_2DE5")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x381F8, 0xA, 0xFFFFAFF6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_2DE5 end

    def Function_13_2E06(): pass

    label("Function_13_2E06")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3819E, 0xA, 0xFFFFB65E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_2E06 end

    def Function_14_2E27(): pass

    label("Function_14_2E27")

    EventBegin(0x0)
    OP_D2(0x70239, 0x70245, 0x11)
    OP_D2(0x2601B3, 0x2601B8, 0x12)
    OP_D2(0x290143, 0x290147, 0x14)
    OP_D2(0x290145, 0x290149, 0x15)
    OP_D2(0x70218, 0x70224, 0x16)
    OP_D2(0x701D0, 0x701DC, 0x17)
    OP_D2(0x70248, 0x70254, 0x18)
    OP_D2(0x7026E, 0x70275, 0x19)
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(256990, 0, -10720, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(2230, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    SetChrPos(0xA, 269300, 700, -11440, 270)
    SetChrPos(0xB, 269300, 700, -9000, 270)
    SetChrPos(0xC, 272070, 700, -12200, 270)
    SetChrPos(0xD, 272290, 700, -7890, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x107, 256170, 0, -10610, 90)
    SetChrPos(0x8, 256370, -10, -11780, 90)
    SetChrPos(0x9, 254450, 10, -8039, 90)
    SetChrPos(0x106, 255080, 10, -9150, 90)
    SetChrPos(0x103, 254000, -30, -12610, 90)
    SetChrPos(0x108, 254810, 0, -13860, 90)
    SetChrChipByIndex(0x107, 17)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 18)
    SetChrSubChip(0x8, 4)
    SetChrChipByIndex(0x106, 22)
    SetChrChipByIndex(0x103, 23)
    SetChrChipByIndex(0x108, 24)
    SetChrChipByIndex(0x9, 25)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x103, 0)
    SetChrSubChip(0x108, 0)
    SetChrSubChip(0x9, 0)
    LoadEffect(0x0, "scraft\\\\sc006_01.eff")
    LoadEffect(0x1, "scraft\\\\sc006_02.eff")
    LoadEffect(0x2, "scraft\\\\sc006_03.eff")
    LoadEffect(0x3, "monster\\\\msc0310.eff")
    LoadEffect(0x4, "battle\\\\btbomb00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, 246450, -10, -8780, 0)

    def lambda_3068():

        label("loc_3068")

        OP_99(0x107, 0x0, 0x7, 0xFA0)
        OP_48()
        Jump("loc_3068")

    QueueWorkItem2(0x107, 0, lambda_3068)
    PlayEffect(0x0, 0x0, 0x107, 0, -300, 300, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x107, 0, 500, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x8, 0x1, 0x0, 0xF)
    OP_43(0x8, 0x2, 0x0, 0x14)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_3102():
        OP_6D(269830, 60, -9380, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3102)

    def lambda_311A():
        OP_67(0, 10620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_311A)

    def lambda_3132():
        OP_6B(2480, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3132)
    Sleep(1000)
    OP_43(0xA, 0x2, 0x0, 0x10)
    OP_43(0xB, 0x2, 0x0, 0x11)
    OP_43(0xC, 0x2, 0x0, 0x12)
    OP_43(0xD, 0x2, 0x0, 0x13)
    Sleep(1500)
    Sleep(500)
    Sleep(1000)
    Sleep(500)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x201F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2E27 end

    def Function_15_31A2(): pass

    label("Function_15_31A2")


    def lambda_31A8():

        label("loc_31A8")

        OP_99(0x8, 0x4, 0x5, 0x9C4)
        OP_48()
        Jump("loc_31A8")

    QueueWorkItem2(0x107, 1, lambda_31A8)
    PlayEffect(0x3, 0x2, 0x8, -100, 650, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x8, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_15_31A2 end

    def Function_16_3220(): pass

    label("Function_16_3220")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3288")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_3251():

        label("loc_3251")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3251")

    QueueWorkItem2(0xFE, 3, lambda_3251)
    OP_91(0xFE, 0x3C, 0x0, 0xFFFFFFF6, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(300)
    Jump("Function_16_3220")

    label("loc_3288")

    Return()

    # Function_16_3220 end

    def Function_17_3289(): pass

    label("Function_17_3289")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32F1")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_32BA():

        label("loc_32BA")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_32BA")

    QueueWorkItem2(0xFE, 3, lambda_32BA)
    OP_91(0xFE, 0x32, 0x0, 0xA, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(100)
    Jump("Function_17_3289")

    label("loc_32F1")

    Return()

    # Function_17_3289 end

    def Function_18_32F2(): pass

    label("Function_18_32F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_335A")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_3323():

        label("loc_3323")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_3323")

    QueueWorkItem2(0xFE, 3, lambda_3323)
    OP_91(0xFE, 0x32, 0x0, 0xFFFFFFF6, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(200)
    Jump("Function_18_32F2")

    label("loc_335A")

    Return()

    # Function_18_32F2 end

    def Function_19_335B(): pass

    label("Function_19_335B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33C3")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_338C():

        label("loc_338C")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_338C")

    QueueWorkItem2(0xFE, 3, lambda_338C)
    OP_91(0xFE, 0x6E, 0x0, 0xA, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(250)
    Jump("Function_19_335B")

    label("loc_33C3")

    Return()

    # Function_19_335B end

    def Function_20_33C4(): pass

    label("Function_20_33C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3990")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34CC")
    PlayEffect(0x1, 0x4, 0xA, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xC, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 265880, 0, -10420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xB, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3988")

    label("loc_34CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35BF")
    PlayEffect(0x1, 0x4, 0xB, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 266880, 0, -8420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3988")

    label("loc_35BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B2")
    PlayEffect(0x1, 0x4, 0xC, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 273220, 0, -9550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 273220, 0, -6550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xFF, 274220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3988")

    label("loc_36B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A5")
    PlayEffect(0x1, 0x4, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 268880, 0, -9420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xB, 0, 300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3988")

    label("loc_37A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3898")
    PlayEffect(0x1, 0x4, 0xFF, 268880, 100, -9420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xB, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xA, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xC, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3988")

    label("loc_3898")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3988")
    PlayEffect(0x1, 0x4, 0xFF, 275220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xA, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 274220, 0, -5550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_3988")

    Sleep(100)
    Jump("Function_20_33C4")

    label("loc_3990")

    Return()

    # Function_20_33C4 end

    def Function_21_3991(): pass

    label("Function_21_3991")

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
        (0, "loc_3A0B"),
        (1, "loc_3A11"),
        (SWITCH_DEFAULT, "loc_3A17"),
    )


    label("loc_3A0B")

    OP_A2(0x1200)
    Jump("loc_3A17")

    label("loc_3A11")

    OP_A2(0x1201)
    Jump("loc_3A17")

    label("loc_3A17")

    Return()

    # Function_21_3991 end

    def Function_22_3A18(): pass

    label("Function_22_3A18")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_22_3A18 end

    SaveToFile()

Try(main)
