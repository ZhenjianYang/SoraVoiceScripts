from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Carna',                                # 9
        'Grant',                                # 10
        'Vanguard',                             # 11
        'Vanguard',                             # 12
        'Vanguard',                             # 13
        'Vanguard',                             # 14
        'Gull Seaside Way',                     # 15
        'Jenis Royal Academy',                  # 16
        'Mercury Viper',                        # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
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
        "Function_4_5B0",          # 04, 4
        "Function_5_1877",         # 05, 5
        "Function_6_193E",         # 06, 6
        "Function_7_197F",         # 07, 7
        "Function_8_3B43",         # 08, 8
        "Function_9_3B5F",         # 09, 9
        "Function_10_3B7B",        # 0A, 10
        "Function_11_3B9C",        # 0B, 11
        "Function_12_3BBD",        # 0C, 12
        "Function_13_3BDE",        # 0D, 13
        "Function_14_3BFF",        # 0E, 14
        "Function_15_3F86",        # 0F, 15
        "Function_16_4004",        # 10, 16
        "Function_17_406D",        # 11, 17
        "Function_18_40D6",        # 12, 18
        "Function_19_413F",        # 13, 19
        "Function_20_41A8",        # 14, 20
        "Function_21_4775",        # 15, 21
        "Function_22_47FB",        # 16, 22
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
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4DD"),
        (SWITCH_DEFAULT, "loc_500"),
    )


    label("loc_4DD")

    Fade(500)
    OP_89(0x0, 217320, -20, -51680, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_500")

    Battle(0xEDD, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 217320, -20, -51680, 180)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_539"),
        (1, "loc_53C"),
        (SWITCH_DEFAULT, "loc_53F"),
    )


    label("loc_539")

    EventEnd(0x0)
    Return()

    label("loc_53C")

    OP_B4(0x0)
    Return()

    label("loc_53F")

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
        "\x07\x05Exterminated monster!\x02",
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

    def Function_4_5B0(): pass

    label("Function_4_5B0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C7")
    Call(0, 21)
    Call(0, 22)

    label("loc_5C7")

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
    OP_D2(0x2600FC, 0x260101, 0x13)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xC, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_701():
        OP_6D(237450, 80, -15960, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_701)

    def lambda_719():
        OP_67(0, 6890, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_719)

    def lambda_731():
        OP_6B(2450, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_731)

    def lambda_741():
        OP_6E(332, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_741)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_7C1")

    ChrTalk(    #2
        0x106,
        (
            "#053F#5PWe came as soon as we heard.\x02\x03",

            "#057FThe situation here sounds\x01",
            "pretty messed up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF")

    label("loc_7C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_852")

    ChrTalk(    #3
        0x103,
        (
            "#026F#6PWe rushed over as soon as we heard.\x02\x03",

            "#022FIf Mickey was telling the truth at all,\x01",
            "the situation sounds beyond dire.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BF")

    label("loc_852")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_8BF")

    ChrTalk(    #4
        0x108,
        (
            "#074F#1PWe came as soon as we heard.\x02\x03",

            "#072FThe situation Mickey described\x01",
            "sounds horrible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(    #5
        0x107,
        (
            "#065F#5PMr. Jean contacted the Royal Army, but...\x02\x03",

            "He said it could be a long time\x01",
            "before reinforcements arrive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6C")

    label("loc_945")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_9D5")

    ChrTalk(    #6
        0x108,
        (
            "#072F#1PJean did his best to contact the army.\x02\x03",

            "He feared it would take some time for\x01",
            "reinforcements to reach us, however.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6C")

    label("loc_9D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_A6C")

    ChrTalk(    #7
        0x103,
        (
            "#022F#6PJean did do everything he\x01",
            "could to contact the army...\x02\x03",

            "It sounds like reinforcements could\x01",
            "be some time in coming, however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6C")

    OP_8C(0x101, 225, 400)

    ChrTalk(    #8
        0x101,
        "#1003F#6PDamn it...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B78")

    ChrTalk(    #9
        0x108,
        (
            "#074F#1PAnd even then, with orbal weaponry\x01",
            "not working, most modern army men\x01",
            "won't be reliable.\x02\x03",

            "#072FWe have little choice but to settle\x01",
            "things ourselves, since we have actual\x01",
            "experience with hand-to-hand combat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5A")

    label("loc_B78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C70")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #10
        0x106,
        (
            "#053F#2PAnd keep in mind, Army grunts these\x01",
            "days're only trained to use orbal weapons.\x01",
            "They're screwed right now.\x02\x03",

            "#050FI think we'll have to settle this one\x01",
            "ourselves, since we've all got actual\x01",
            "hand-to-hand training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5A")

    label("loc_C70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")

    ChrTalk(    #11
        0x103,
        (
            "#026F#6PThere's a further problem--the army is\x01",
            "trained mainly in the use of orbal weapons.\x01",
            "Which currently don't work.\x02\x03",

            "#022FWe're the ones with hand-to-hand combat\x01",
            "training--I fear it will fall to us in any event.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCA")

    ChrTalk(    #12
        0x107,
        (
            "#065F#5PB-But, we can't just leave the people\x01",
            "in the school as prisoners!\x02\x03",

            "What do we do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_DCA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5C")

    ChrTalk(    #13
        0x103,
        (
            "#522F#6PThey've likely taken the whole\x01",
            "school hostage, as well.\x02\x03",

            "If we move in carelessly, we could\x01",
            "hurt more than we save.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EED")

    label("loc_E5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")
    OP_8C(0x106, 0, 400)

    ChrTalk(    #14
        0x106,
        (
            "#552F#2PAnd those bastards have probably\x01",
            "taken the whole school captive.\x02\x03",

            "We just charge in and people\x01",
            "could get hurt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EED")


    ChrTalk(    #15
        0x101,
        (
            "#1007F#6PThat's the problem, isn't it?...\x02\x03",

            "#1003FIt'd be nice if we had a picture of what\x01",
            "was happening inside, but...how?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1042F#6P...\x02\x03",

            "#1035FEveryone, wait here a bit. I'm going\x01",
            "to go scout inside the academy.\x02",
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

    def lambda_105D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_105D)

    def lambda_106B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_106B)
    Sleep(100)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #17
        0x101,
        "#1004FJoshua?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x103,
        "#022F#6PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #19
        0x102,
        (
            "#1040F#4PMy mind and body were molded to be the\x01",
            "perfect spy and assassin, remember?\x02\x03",

            "I should be able to sneak in and get an\x01",
            "idea of what's inside the school and\x01",
            "the condition of the hostages, easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        "#555F#2PJoshua's...got a point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x108,
        (
            "#074F#1PHmmm. If you can do it,\x01",
            "it would certainly help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#065F#5PB-B-But!\x01",
            "Won't it be really dangerous?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1040F#4PI'll be all right, trust me.\x01",
            "I've infiltrated places FAR more\x01",
            "heavily guarded than this.\x02\x03",

            "You don't need to worry, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        "#063F#5PButbutbut...!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)

    ChrTalk(    #25
        0x101,
        (
            "#1002F#6P...Joshua. You're going alone,\x01",
            "no matter what?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #26
        0x102,
        (
            "#1043F#4PThe odds of success are much,\x01",
            "MUCH higher if I do this myself.\x02\x03",

            "#1042FTrust me on this, Estelle.\x01",
            "Let me go on my own for this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1010F#6POkay...\x02\x03",

            "#1002FI just want to ask one thing.\x02\x03",

            "You remember the promise\x01",
            "we made, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1053F#4PTo walk together to the end, right?\x02\x03",

            "#1054FDon't worry--I'm just wandering off\x01",
            "to pick daisies for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1006F#6PYou go pick those flowers,\x01",
            "then, mister!\x02\x03",

            "#1025FJoshua...be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        "#1053F#4PI will be. I promise.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #31
        0x102,
        (
            "#1040F#4PAll right, I'll be back as\x01",
            "soon as I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_1562():

        label("loc_1562")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1562")

    QueueWorkItem2(0x101, 2, lambda_1562)

    def lambda_1573():

        label("loc_1573")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1573")

    QueueWorkItem2(0x103, 2, lambda_1573)

    def lambda_1584():

        label("loc_1584")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1584")

    QueueWorkItem2(0x107, 2, lambda_1584)

    def lambda_1595():

        label("loc_1595")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1595")

    QueueWorkItem2(0x106, 2, lambda_1595)

    def lambda_15A6():

        label("loc_15A6")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_15A6")

    QueueWorkItem2(0x108, 2, lambda_15A6)

    def lambda_15B7():
        OP_6D(244310, 100, -18660, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15B7)

    def lambda_15CF():
        OP_67(0, 4870, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15CF)

    def lambda_15E7():
        OP_6B(2770, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_15E7)

    def lambda_15F7():
        OP_6C(105000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_15F7)

    def lambda_1607():
        OP_6E(371, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1607)
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

    def lambda_1679():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1679)
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
        (
            "#552FHey...\x01",
            "You really okay with this?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(300)

    ChrTalk(    #33
        0x101,
        (
            "#1025F...Yeah.\x02\x03",

            "If I insisted on going,\x01",
            "I'd just drag him down here.\x02\x03",

            "#1012FBesides...I believe in Joshua.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17C1():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_17C1)
    Sleep(100)

    def lambda_17D4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_17D4)
    Sleep(100)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #34
        0x107,
        "#560F#5PEstelle...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x103,
        (
            "#027F#6PHeehee...\x01",
            "You've grown quite a lot, Estelle.\x02",
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

    # Function_4_5B0 end

    def Function_5_1877(): pass

    label("Function_5_1877")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18B0")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_18B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_18E9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D1")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_18D5")

    label("loc_18D1")

    AddParty(0x5, 0xFB, 0xFF)

    label("loc_18D5")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_18E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1922")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_190A")
    AddParty(0x6, 0xFA, 0xFF)
    Jump("loc_190E")

    label("loc_190A")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_190E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_193D")
    AddParty(0x7, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_193D")

    Return()

    # Function_5_1877 end

    def Function_6_193E(): pass

    label("Function_6_193E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_194E")
    RemoveParty(0x2, 0xFF)

    label("loc_194E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_195E")
    RemoveParty(0x5, 0xFF)

    label("loc_195E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_196E")
    RemoveParty(0x6, 0xFF)

    label("loc_196E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_197E")
    RemoveParty(0x7, 0xFF)

    label("loc_197E")

    Return()

    # Function_6_193E end

    def Function_7_197F(): pass

    label("Function_7_197F")

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
            "#1040F#4PThat's the situation on the academy\x01",
            "grounds from what I could tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x108,
        (
            "#070F#6PPretty thorough.\x01",
            "You did a good job scouting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#051FYeah, now we should be able to\x01",
            "put some kind of plan together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1007F#6PSo that Gilbert idiot is the one who\x01",
            "led the attack on the academy...\x02\x03",

            "#1019FAnd he was seriously trying to kidnap\x01",
            "Kloe? He had the balls for that?\x02\x03",

            "#1022FI should've thrown him off the damn deck\x01",
            "of that airship when I had the chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x103,
        (
            "#026F#6PThe man who was once a peaceful secretary\x01",
            "for a mayor is now one of Ouroboros' jackals.\x02\x03",

            "#524FA member of the elite who falls to villainy\x01",
            "when they encounter hardship...\x01",
            "It's an old, old story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1007F#6PThat describes him, all right.\x02\x03",

            "#1015F...Still, though, what do we do?\x02\x03",

            "It sounds like he brought along a fair\x01",
            "number of jaegers, and he's got archaisms\x01",
            "and armored monsters, too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        (
            "#065FAnd if the archaisms are working and the\x01",
            "jaegers have guns, then...\x02\x03",

            "Then that means the society can use\x01",
            "orbments even through the shutdown\x01",
            "phenomenon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1020F#6POh, crap...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1035F#4PIt looks as though they're using something\x01",
            "similar to our Zero Field Generators.\x02\x03",

            "#1042FAnd they definitely have enough\x01",
            "for each man and machine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#052F#5PSo they're free to hose us down with\x01",
            "as much gunfire as they want...\x02\x03",

            "#057FNot the best situation I've ever been in.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #46
        0x103,
        (
            "#026F#6PThe obvious answer is to\x01",
            "split into two groups.\x02\x03",

            "#020FOne group raises hell on their front\x01",
            "and distracts them while another\x01",
            "group infiltrates from the rear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x108,
        (
            "#074F#6PWe're too short on manpower\x01",
            "to try that safely, though.\x02\x03",

            "#072FFrom what Joshua describes, I'd want\x01",
            "no less than six people to attack their\x01",
            "front. Any less is suicide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        (
            "#1043F#4PI agree.\x02\x03",

            "#1035FIf we have six people, we should be able\x01",
            "to draw their troops on standby out\x01",
            "without getting killed ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1007F#6PBut six people...\x01",
            "That's everyone here now!\x02\x03",

            "#1015FAre we just going to have to wait\x01",
            "for the Royal Army to get here?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10E, 221680, -40, -19680, 90)
    SetChrPos(0x10A, 221970, -50, -21480, 45)
    SetChrPos(0x8, 220360, -20, -21540, 45)
    SetChrPos(0x9, 220510, 30, -20230, 45)

    NpcTalk(    #50
        0x10E,
        "Man's Voice",
        (
            "#2PI believe we may be able\x01",
            "to fill in the gap.\x02",
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

    def lambda_233E():

        label("loc_233E")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_233E")

    QueueWorkItem2(0x101, 1, lambda_233E)
    Sleep(50)

    def lambda_2354():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2354)
    Sleep(50)

    def lambda_2367():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2367)
    Sleep(50)

    def lambda_237A():

        label("loc_237A")

        TurnDirection(0xFE, 0x10A, 400)
        OP_48()
        Jump("loc_237A")

    QueueWorkItem2(0x107, 1, lambda_237A)
    Sleep(50)

    def lambda_2390():

        label("loc_2390")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_2390")

    QueueWorkItem2(0x102, 1, lambda_2390)
    Sleep(50)

    def lambda_23A6():

        label("loc_23A6")

        TurnDirection(0xFE, 0x10E, 400)
        OP_48()
        Jump("loc_23A6")

    QueueWorkItem2(0x103, 1, lambda_23A6)
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
        "#2P#064FOh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1004FWHOA! Anelace! Everyone!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x108,
        "#071F#4PHaha! Perfect timing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#825F#6PHeh. We actually just stopped\x01",
            "in at the Ruan branch a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "#835F#3POnce we heard the story from Jean,\x01",
            "we came running as fast as we could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        (
            "#021FI think this is another one\x01",
            "for the 'divine providence' column.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2613():
        OP_6D(233430, 30, -19680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2613)

    def lambda_262B():
        OP_67(0, 6760, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_262B)

    def lambda_2643():
        OP_6B(2400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2643)
    OP_8F(0x10A, 0x38CC0, 0x14, 0xFFFFB1EA, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #57
        0x10A,
        (
            "#1314F#6PEstelle...thanks for saving me\x01",
            "back at that lab.\x02\x03",

            "You really saved me from...a lot.\x01",
            "I owe you.\x02\x03",

            "#1316FI was so, so angry with myself\x01",
            "when I heard they captured you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1016F#4PHaha, don't worry! It ended up fine,\x01",
            "they didn't rough me up much.\x02\x03",

            "#1006FBesides! I got Joshua back\x01",
            "in that whole mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10A,
        (
            "#1314F#6PYeah...\x02\x03",

            "#819FAhaha...\x01",
            "It's been forever, Joshua!\x02\x03",

            "Didja forget about your sterling\x01",
            "role model Anelace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1053FHaha... No, of course not.\x02\x03",

            "#1054FIt sounds like you helped Estelle\x01",
            "a great deal while I was away.\x02\x03",

            "Thank you for everything, Anelace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10A,
        (
            "#816F#6PWellll, if anything, she was\x01",
            "helping me out, I think.\x02\x03",

            "#1311FWhat I REALLY wanna do is tell you alllll\x01",
            "about just how lonely Estelle was without\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1013F#4PEr, wait, she is FULL of lies and you\x01",
            "shouldn't believe a word she says!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10A,
        (
            "#1315F#6PHeehee! Just kidding, just kidding.\x02\x03",

            "#816FBesides, I don't think we can really\x01",
            "afford to shoot the breeze much here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1007F#4PYeah, seriously.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #65
        0x101,
        (
            "#1015F#6PJoshua, mind filling everyone in\x01",
            "on the situation inside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        "#1040FOf course.\x02",
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
            "#843F#6PI see.\x01",
            "A grim situation.\x02\x03",

            "#842FI agree with your plan. A two-pronged\x01",
            "assault will resolve this quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#824F#6PWell, now we got ten people, so...\x02\x03",

            "#820FSix to assault the front and four\x01",
            "from the rear. That work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x106,
        (
            "#2P#053FSeems like a good split to me.\x02\x03",

            "#051FThe only real question is who\x01",
            "goes chargin' at what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#2P#1004FOh, in that case, can I lead the\x01",
            "infiltrate-from-the-rear team?\x02\x03",

            "#1016FNo offense, but I think I know\x01",
            "the academy better than anyone\x01",
            "here at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1035FExcept perhaps for me, Estelle.\x02\x03",

            "#1040FRemember, I did just scout the\x01",
            "entire grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10A,
        (
            "#1310F#6PMind if I go with Estelle, then?\x02\x03",

            "#811FWe did promise to go into gloooorious\x01",
            "battle together once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#2P#1025FAnelace...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020FGiven how quick you are, it's\x01",
            "a good idea regardless.\x02\x03",

            "#026FYou three are all scrappers, though...\x02\x03",

            "#027FThe best choice for a fourth would be\x01",
            "someone who can support you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10E,
        (
            "#843F#6PAllow me to serve that role, then.\x02\x03",

            "#841FI need no orbment to use MY arts.\x01",
            "I can aid Estelle's group with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#2P#1011FKurt...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        "#1040FThank you, Kurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x106,
        (
            "#2P#051FHeh, looks like that's our teams, then.\x02\x03",

            "#052FOh, on that note, though...\x01",
            "Carna, you gonna be all right?\x01",
            "Your weapon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#833F#3POh, you mean my orbal gun.\x02\x03",

            "#835FYeah, losing that was rough.\x01",
            "I've had to fall back on this\x01",
            "noisy old thing.\x02",
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
        (
            "#2P#1004FWhat in the world is\x01",
            "that huge gun?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#064FThat's a...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#831F#3PHeheh. It's an old Reinford-model\x01",
            "GUNPOWDER assault rifle!\x02\x03",

            "Eva, an old friend of mine who runs\x01",
            "a weapon shop, lent it to me.\x02\x03",

            "She collects things like this and\x01",
            "let me run off with it for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        (
            "#2P#051FA gunpowder rifle.\x01",
            "Now that's old school, hell yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        (
            "#027FNow that I think about it, I haven't seen\x01",
            "any firearms that use gunpowder lately.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 400)
    Sleep(300)

    ChrTalk(    #85
        0x103,
        (
            "#023F#2PWait, Tita, that gatling gun of yours\x01",
            "is a gunpowder weapon, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x103, 400)
    Sleep(300)

    ChrTalk(    #86
        0x107,
        (
            "#061F#5PHeehee! Yep!\x02\x03",

            "#560FIt's part of Grandpa's treasured collection!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_337C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_337C)
    Sleep(100)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #87
        0x8,
        (
            "#833F#3PHonestly, it's far heavier than an orbal\x01",
            "gun, it runs out of ammo in seconds,\x01",
            "and it's just harder to use in every way.\x02\x03",

            "#830FIt's got plenty of stopping power, though,\x01",
            "so it'll be fine for a quick strike like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x108,
        (
            "#074F#2PMmm, yes, it sounds like you'll\x01",
            "be all right in the assault group.\x02\x03",

            "#070FLet's start the plan, then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#2P#1018FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10A,
        "#816F#6PWe'll do our best!\x02",
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
    OP_41(0x9, 0x0, 0xFF)
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

    label("loc_35B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3871")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #91
        (
            "\x06\x18\x07\x05Now entering party selection.\x01",
            "Change your party to swap out equipment as necessary,\x01",
            "and when done, select 'Begin Assault.' You will proceed\x01",
            "with a team of Estelle, Joshua, Anelace, and Kurt.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Change Party\x01",          # 0
            "Change Equipment\x01",      # 1
            "Begin Assault\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3784")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #92
        (
            "\x07\x05Temporarily rearranging the party.\x01",
            "You may remove equipment from other members\x01",
            "to equip Anelace and Kurt.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0x9, 0xD, 0xFFFF)
    Jump("loc_386E")

    label("loc_3784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_37BD")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_37F9")

    label("loc_37BD")


    AnonymousTalk(    #93
        "\x07\x05Please select this after changing your party.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_37F9")

    Jump("loc_386E")

    label("loc_37FC")

    SetChrName("")

    AnonymousTalk(    #94
        "\x06\x18\x07\x05Are you ready to proceed with the assault?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386E")
    Jump("loc_3871")

    label("loc_3871")

    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "\x07\x05And so the guild's plan to liberate the Jenis Royal\x01",
            "Academy was set into motion.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #96
        (
            "\x07\x05Agate, Scherazard, Zin, Carna, Grant, and Tita\x01",
            "created a distraction at the main gate to lure\x01",
            "the jaegers out...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #97
        (
            "\x07\x05While Estelle, Joshua, Anelace, and Kurt struck\x01",
            "from behind to free the hostages.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    AddParty(0x1, 0xF7, 0xFF)
    AddParty(0x9, 0xF8, 0xFF)
    AddParty(0xD, 0xF9, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E0")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_39E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FB")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_39FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A16")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A31")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4C")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A67")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A82")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9D")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x1)

    label("loc_3A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3B36")
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #98
        (
            "\x07\x05The infiltration team has been given the\x01",
            "remaining Zero Field Generators.\x01",
            "They have been placed in the inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_3B36")

    OP_A2(0x10F2)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_386E")

    Jump("loc_35B2")

    # Function_7_197F end

    def Function_8_3B43(): pass

    label("Function_8_3B43")

    OP_8F(0xFE, 0x390E4, 0x0, 0xFFFFAA74, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_8_3B43 end

    def Function_9_3B5F(): pass

    label("Function_9_3B5F")

    OP_8F(0xFE, 0x38F4A, 0x14, 0xFFFFB7F8, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_9_3B5F end

    def Function_10_3B7B(): pass

    label("Function_10_3B7B")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x38770, 0xFFFFFFF6, 0xFFFFB4B0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_10_3B7B end

    def Function_11_3B9C(): pass

    label("Function_11_3B9C")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x387CA, 0x14, 0xFFFFAEC0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_3B9C end

    def Function_12_3BBD(): pass

    label("Function_12_3BBD")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x381F8, 0xA, 0xFFFFAFF6, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_3BBD end

    def Function_13_3BDE(): pass

    label("Function_13_3BDE")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3819E, 0xA, 0xFFFFB65E, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_3BDE end

    def Function_14_3BFF(): pass

    label("Function_14_3BFF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
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

    def lambda_3E4B():

        label("loc_3E4B")

        OP_99(0x107, 0x0, 0x7, 0xFA0)
        OP_48()
        Jump("loc_3E4B")

    QueueWorkItem2(0x107, 0, lambda_3E4B)
    PlayEffect(0x0, 0x0, 0x107, 0, -300, 300, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0x107, 0, 500, 300, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x8, 0x1, 0x0, 0xF)
    OP_43(0x8, 0x2, 0x0, 0x14)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_3EE5():
        OP_6D(269830, 60, -9380, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3EE5)

    def lambda_3EFD():
        OP_67(0, 10620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3EFD)

    def lambda_3F15():
        OP_6B(2480, 3000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3F15)
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
    OP_DC()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3BFF end

    def Function_15_3F86(): pass

    label("Function_15_3F86")


    def lambda_3F8C():

        label("loc_3F8C")

        OP_99(0x8, 0x4, 0x5, 0x9C4)
        OP_48()
        Jump("loc_3F8C")

    QueueWorkItem2(0x107, 1, lambda_3F8C)
    PlayEffect(0x3, 0x2, 0x8, -100, 650, 1300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x8, 0, 500, 200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_15_3F86 end

    def Function_16_4004(): pass

    label("Function_16_4004")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_406C")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_4035():

        label("loc_4035")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_4035")

    QueueWorkItem2(0xFE, 3, lambda_4035)
    OP_91(0xFE, 0x3C, 0x0, 0xFFFFFFF6, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(300)
    Jump("Function_16_4004")

    label("loc_406C")

    Return()

    # Function_16_4004 end

    def Function_17_406D(): pass

    label("Function_17_406D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40D5")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_409E():

        label("loc_409E")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_409E")

    QueueWorkItem2(0xFE, 3, lambda_409E)
    OP_91(0xFE, 0x32, 0x0, 0xA, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(100)
    Jump("Function_17_406D")

    label("loc_40D5")

    Return()

    # Function_17_406D end

    def Function_18_40D6(): pass

    label("Function_18_40D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_413E")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_4107():

        label("loc_4107")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_4107")

    QueueWorkItem2(0xFE, 3, lambda_4107)
    OP_91(0xFE, 0x32, 0x0, 0xFFFFFFF6, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(200)
    Jump("Function_18_40D6")

    label("loc_413E")

    Return()

    # Function_18_40D6 end

    def Function_19_413F(): pass

    label("Function_19_413F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41A7")
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_8C(0xFE, 270, 0)

    def lambda_4170():

        label("loc_4170")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_4170")

    QueueWorkItem2(0xFE, 3, lambda_4170)
    OP_91(0xFE, 0x6E, 0x0, 0xA, 0x2710, 0x0)
    OP_44(0xFE, 0x3)
    Sleep(250)
    Jump("Function_19_413F")

    label("loc_41A7")

    Return()

    # Function_19_413F end

    def Function_20_41A8(): pass

    label("Function_20_41A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4774")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B0")
    PlayEffect(0x1, 0x4, 0xA, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xC, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 265880, 0, -10420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xB, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_476C")

    label("loc_42B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43A3")
    PlayEffect(0x1, 0x4, 0xB, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 266880, 0, -8420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_476C")

    label("loc_43A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4496")
    PlayEffect(0x1, 0x4, 0xC, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xFF, 273220, 0, -9550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 273220, 0, -6550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xFF, 274220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_476C")

    label("loc_4496")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4589")
    PlayEffect(0x1, 0x4, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 268880, 0, -9420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x7, 0xB, 0, 300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_476C")

    label("loc_4589")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467C")
    PlayEffect(0x1, 0x4, 0xFF, 268880, 100, -9420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xB, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xA, 0, 400, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x5, 0xC, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_476C")

    label("loc_467C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476C")
    PlayEffect(0x1, 0x4, 0xFF, 275220, 0, -8550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xD, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x4, 0xA, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x1, 0x6, 0xFF, 274220, 0, -5550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_476C")

    Sleep(100)
    Jump("Function_20_41A8")

    label("loc_4774")

    Return()

    # Function_20_41A8 end

    def Function_21_4775(): pass

    label("Function_21_4775")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47EE"),
        (1, "loc_47F4"),
        (SWITCH_DEFAULT, "loc_47FA"),
    )


    label("loc_47EE")

    OP_A2(0x1200)
    Jump("loc_47FA")

    label("loc_47F4")

    OP_A2(0x1201)
    Jump("loc_47FA")

    label("loc_47FA")

    Return()

    # Function_21_4775 end

    def Function_22_47FB(): pass

    label("Function_22_47FB")

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

    # Function_22_47FB end

    SaveToFile()

Try(main)
