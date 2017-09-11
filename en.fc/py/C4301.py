from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C4301   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4301.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60035",
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
        'Captain Amalthea',                     # 9
        'Professor Russell',                    # 10
        'Sieg',                                 # 11
        'Mech',                                 # 12
        'Mech',                                 # 13
        'Scherazard',                           # 14
        'Olivier',                              # 15
        'Kloe',                                 # 16
        'Agate',                                # 17
        'Tita',                                 # 18
        'Zin',                                  # 19
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
        'ED6_DT07/CH00280 ._CH',             # 00
        'ED6_DT09/CH10990 ._CH',             # 01
        'ED6_DT07/CH02020 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00120 ._CH',             # 08
        'ED6_DT07/CH00121 ._CH',             # 09
        'ED6_DT07/CH00130 ._CH',             # 0A
        'ED6_DT07/CH00131 ._CH',             # 0B
        'ED6_DT07/CH00140 ._CH',             # 0C
        'ED6_DT07/CH00141 ._CH',             # 0D
        'ED6_DT07/CH00150 ._CH',             # 0E
        'ED6_DT07/CH00151 ._CH',             # 0F
        'ED6_DT07/CH00160 ._CH',             # 10
        'ED6_DT07/CH00161 ._CH',             # 11
        'ED6_DT07/CH00170 ._CH',             # 12
        'ED6_DT07/CH00171 ._CH',             # 13
        'ED6_DT09/CH10991 ._CH',             # 14
        'ED6_DT06/CH20040 ._CH',             # 15
        'ED6_DT07/CH00020 ._CH',             # 16
        'ED6_DT07/CH00030 ._CH',             # 17
        'ED6_DT07/CH00040 ._CH',             # 18
        'ED6_DT06/CH20053 ._CH',             # 19
        'ED6_DT07/CH00060 ._CH',             # 1A
        'ED6_DT07/CH00070 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT07/CH00280P._CP',             # 00
        'ED6_DT09/CH10990P._CP',             # 01
        'ED6_DT07/CH02020P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00120P._CP',             # 08
        'ED6_DT07/CH00121P._CP',             # 09
        'ED6_DT07/CH00130P._CP',             # 0A
        'ED6_DT07/CH00131P._CP',             # 0B
        'ED6_DT07/CH00140P._CP',             # 0C
        'ED6_DT07/CH00141P._CP',             # 0D
        'ED6_DT07/CH00150P._CP',             # 0E
        'ED6_DT07/CH00151P._CP',             # 0F
        'ED6_DT07/CH00160P._CP',             # 10
        'ED6_DT07/CH00161P._CP',             # 11
        'ED6_DT07/CH00170P._CP',             # 12
        'ED6_DT07/CH00171P._CP',             # 13
        'ED6_DT09/CH10991P._CP',             # 14
        'ED6_DT06/CH20040P._CP',             # 15
        'ED6_DT07/CH00020P._CP',             # 16
        'ED6_DT07/CH00030P._CP',             # 17
        'ED6_DT07/CH00040P._CP',             # 18
        'ED6_DT06/CH20053P._CP',             # 19
        'ED6_DT07/CH00060P._CP',             # 1A
        'ED6_DT07/CH00070P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclEvent(
        X                   = 46000,
        Y                   = -1000,
        Z                   = -10460,
        Range               = 49420,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFB884,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 62990,
        TriggerZ            = 0,
        TriggerY            = -2920,
        TriggerRange        = 1000,
        ActorX              = 62990,
        ActorZ              = 1200,
        ActorY              = -2920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32E",          # 00, 0
        "Function_1_362",          # 01, 1
        "Function_2_3AC",          # 02, 2
        "Function_3_3C2",          # 03, 3
        "Function_4_42C",          # 04, 4
        "Function_5_51D",          # 05, 5
        "Function_6_59A",          # 06, 6
        "Function_7_637",          # 07, 7
        "Function_8_6A5",          # 08, 8
        "Function_9_702",          # 09, 9
        "Function_10_8A8",         # 0A, 10
        "Function_11_8EE",         # 0B, 11
        "Function_12_911",         # 0C, 12
        "Function_13_2131",        # 0D, 13
        "Function_14_275E",        # 0E, 14
        "Function_15_28A2",        # 0F, 15
        "Function_16_2CDA",        # 10, 16
        "Function_17_2DAF",        # 11, 17
    )


    def Function_0_32E(): pass

    label("Function_0_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_345")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 15)

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_END)), "loc_350")
    Call(0, 14)

    label("loc_350")

    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_32E end

    def Function_1_362(): pass

    label("Function_1_362")

    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x6, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_362 end

    def Function_2_3AC(): pass

    label("Function_2_3AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3AC")

    label("loc_3C1")

    Return()

    # Function_2_3AC end

    def Function_3_3C2(): pass

    label("Function_3_3C2")

    TalkBegin(0xD)

    ChrTalk(    #0
        0xD,
        (
            "#020FEstelle... Don't overdo it.\x02\x03",

            "We still have a ways to go. We\x01",
            "can't afford to be reckless.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_3_3C2 end

    def Function_4_42C(): pass

    label("Function_4_42C")

    TalkBegin(0xE)

    ChrTalk(    #1
        0xE,
        (
            "#030FA vast underground ruin, slumbering\x01",
            "beneath a royal castle...\x02\x03",

            "What a delightfully tragic poem\x01",
            "this all would make!\x02\x03",

            "Well, minus the bits about the maniacal\x01",
            "soldiers and deadly mechanical demons.\x01",
            "There's little art in that!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_4_42C end

    def Function_5_51D(): pass

    label("Function_5_51D")

    TalkBegin(0xF)

    ChrTalk(    #2
        0xF,
        (
            "#042FSo the Aureole is... Why here?\x01",
            "There must be a reason!\x02\x03",

            "How much does Colonel Richard\x01",
            "REALLY know about it?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_5_51D end

    def Function_6_59A(): pass

    label("Function_6_59A")

    TalkBegin(0x10)

    ChrTalk(    #3
        0x10,
        (
            "#050FWe've gone a long way down, and\x01",
            "we're still only halfway there.\x02\x03",

            "We really are in over our heads, I think.\x01",
            "Both literally and figuratively.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_6_59A end

    def Function_7_637(): pass

    label("Function_7_637")

    TalkBegin(0x11)

    ChrTalk(    #4
        0x11,
        (
            "#062FI wonder if those monsters are\x01",
            "orbal-powered...\x02\x03",

            "If they are, then that means\x01",
            "these ruins...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x11)
    Return()

    # Function_7_637 end

    def Function_8_6A5(): pass

    label("Function_8_6A5")

    TalkBegin(0x12)

    ChrTalk(    #5
        0x12,
        (
            "#070FEvery monster in here presents\x01",
            "a challenge for us.\x02\x03",

            "My muscles are singing!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_8_6A5 end

    def Function_9_702(): pass

    label("Function_9_702")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Buy\x01",                  # 2
            "Change Members\x01",       # 3
            "Leave\x01",                # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_781")
    Call(0, 10)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79B")
    Call(0, 11)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_79B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    Call(0, 13)
    OP_4B(0x9, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_800")
    TalkEnd(0x9)
    Return()

    label("loc_800")


    ChrTalk(    #6
        0x9,
        (
            "#104FNo turning back now...\x02\x03",

            "#102FYou need to prepare yourselves to face the\x01",
            "colonel at any moment, as there's simply no\x01",
            "telling when the showdown will occur.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_9_702 end

    def Function_10_8A8(): pass

    label("Function_10_8A8")


    ChrTalk(    #7
        0x9,
        (
            "#100FCome on, then. I'll fix those\x01",
            "up better than brand new!\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)
    Return()

    # Function_10_8A8 end

    def Function_11_8EE(): pass

    label("Function_11_8EE")


    ChrTalk(    #8
        0x9,
        "#100FWhat is it you need?\x02",
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)
    Return()

    # Function_11_8EE end

    def Function_12_911(): pass

    label("Function_12_911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91E")
    Return()

    label("loc_91E")

    OP_A2(0x668)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    OP_9F(0xB, 0xFF, 0x0, 0x0, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x8, 61000, 0, -13970, 270)
    SetChrPos(0xB, 59250, 6000, -11650, 270)
    SetChrPos(0xC, 59250, 6000, -16329, 270)

    NpcTalk(    #9
        0x8,
        "Woman's Voice",
        "I figured you'd come...\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A17():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A17)

    def lambda_A25():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A25)

    def lambda_A33():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A33)

    def lambda_A41():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A41)

    def lambda_A4F():
        OP_67(0, 8170, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A4F)

    def lambda_A67():
        OP_6C(37000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A67)
    OP_6D(57560, 0, -13380, 2000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9F")
    SetChrChipByIndex(0x103, 8)

    label("loc_A9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB2")
    SetChrChipByIndex(0x104, 10)

    label("loc_AB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC5")
    SetChrChipByIndex(0x106, 14)

    label("loc_AC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD8")
    SetChrChipByIndex(0x105, 12)

    label("loc_AD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEB")
    SetChrChipByIndex(0x107, 16)

    label("loc_AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFE")
    SetChrChipByIndex(0x108, 18)

    label("loc_AFE")

    SetChrPos(0x0, 45670, 0, -14030, 90)
    SetChrPos(0x1, 45670, 0, -14030, 90)
    SetChrPos(0x2, 45670, 0, -14030, 90)
    SetChrPos(0x3, 45670, 0, -14030, 90)

    def lambda_B48():
        OP_8E(0xFE, 0xD110, 0x0, 0xFFFFCBA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B48)
    Sleep(500)

    def lambda_B68():
        OP_8E(0xFE, 0xD110, 0x0, 0xFFFFC68A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B68)
    Sleep(500)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_BC4")
    Sleep(500)

    def lambda_BAC():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BAC)
    Jump("loc_BDF")

    label("loc_BC4")


    def lambda_BCA():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_BCA)

    label("loc_BDF")

    OP_A2(0x6)

    label("loc_BE2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C21")
    Sleep(500)

    def lambda_C09():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_C09)
    Jump("loc_C3C")

    label("loc_C21")


    def lambda_C27():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_C27)

    label("loc_C3C")

    OP_A2(0x6)

    label("loc_C3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_C7E")
    Sleep(500)

    def lambda_C66():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_C66)
    Jump("loc_C99")

    label("loc_C7E")


    def lambda_C84():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_C84)

    label("loc_C99")

    OP_A2(0x6)

    label("loc_C9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_CDB")
    Sleep(500)

    def lambda_CC3():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFC145, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_CC3)
    Jump("loc_CF6")

    label("loc_CDB")


    def lambda_CE1():
        OP_8E(0xFE, 0xCE7C, 0x0, 0xFFFFD080, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_CE1)

    label("loc_CF6")

    OP_A2(0x6)

    label("loc_CF9")

    WaitChrThread(0x0, 0x0)
    OP_8C(0x0, 90, 0)
    WaitChrThread(0x1, 0x0)
    OP_8C(0x1, 90, 0)
    WaitChrThread(0x2, 0x0)
    OP_8C(0x2, 90, 0)
    WaitChrThread(0x3, 0x0)
    OP_8C(0x3, 90, 0)

    ChrTalk(    #10
        0x102,
        "#012FCaptain Amalthea...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #11
        0x101,
        (
            "#004FWh-What the hell are\x01",
            "you doing here?!\x02\x03",

            "You were out cold at\x01",
            "the Garden Terrace...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#180FHa... You actually thought\x01",
            "I'd be so easily defeated?\x02\x03",

            "#181FThough it seems that Grancel\x01",
            "Castle has been taken...\x02\x03",

            "#188FIt's no matter, though. Once His Excellency\x01",
            "obtains the Shining Ring, it can be retaken\x01",
            "at any time.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(    #13
        0x103,
        (
            "#025F#5PYou must be joking. You don't\x01",
            "ever learn, do you?\x02\x03",

            "#027FYou're more like a snake\x01",
            "than a vixen.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_11E2")

    label("loc_F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC0")

    ChrTalk(    #14
        0x104,
        (
            "#035F#5PHeh... I suppose that those with no place\x01",
            "left to turn will cling fiercely to any\x01",
            "dream, no matter how ephemeral.\x02\x03",

            "#030FIt is a bit sad, truly.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11E2")

    label("loc_FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1030")

    ChrTalk(    #15
        0x106,
        (
            "#053F#5PWell, vixens usually are pretty carefree.\x02\x03",

            "#057FYou just hang onto that dream.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11E2")

    label("loc_1030")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1088")

    ChrTalk(    #16
        0x107,
        (
            "#065F#5PU-Umm, what's all this mean?\x02\x03",

            "I...don't really get it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_11E2")

    label("loc_1088")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1123")

    ChrTalk(    #17
        0x108,
        (
            "#075F#5P*sigh* I think you're really\x01",
            "just missing the point.\x02\x03",

            "#070FIt's a real shame, too. Look at\x01",
            "you. You're a beautiful woman.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_11E2")

    label("loc_1123")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11E2")

    ChrTalk(    #18
        0x105,
        (
            "#043F#5PThis 'Shining Ring'... Do you even\x01",
            "know if it's possible for a human\x01",
            "being to make use of it?\x02\x03",

            "There may be a reason it was\x01",
            "sealed so far beneath the\x01",
            "surface...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_11E2")


    ChrTalk(    #19
        0x8,
        (
            "#186FEnough!\x02\x03",

            "If nothing else, I will not\x01",
            "permit you to interfere with\x01",
            "the colonel!\x02\x03",

            "#185FTo me, archaisms!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1259():
        OP_96(0xFE, 0xE772, 0x0, 0xFFFFD27E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1259)
    OP_9F(0xB, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xB, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_12A8():

        label("loc_12A8")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_12A8")

    QueueWorkItem2(0xB, 1, lambda_12A8)

    def lambda_12BB():
        OP_96(0xFE, 0xE772, 0x0, 0xFFFFC037, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12BB)
    OP_9F(0xC, 0x64, 0x64, 0xFF, 0xFF, 0x64)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    WaitChrThread(0xC, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)

    def lambda_130A():

        label("loc_130A")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_130A")

    QueueWorkItem2(0xC, 1, lambda_130A)

    ChrTalk(    #20
        0x101,
        "#580FWhoa...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#012FYou're using the ancient machines...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#188FHa ha... We don't care for being\x01",
            "so casually underestimated.\x02\x03",

            "We've already collected an\x01",
            "incredible amount of data\x01",
            "since our survey here began.\x02\x03",

            "Even controlling these archaisms\x01",
            "is easily within our grasp.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1475")

    ChrTalk(    #23
        0x103,
        "#025F#5P*sigh*... I hate stubborn women.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_1475")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14CB")

    ChrTalk(    #24
        0x104,
        (
            "#035F#5PHeh... I'm personally a bit\x01",
            "touched by the effort.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_14CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_151F")

    ChrTalk(    #25
        0x106,
        (
            "#057F#5PCrap... This ain't gonna be\x01",
            "no walk in the park.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_151F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1596")

    ChrTalk(    #26
        0x107,
        (
            "#063F#5PI-If technology like that is\x01",
            "real, then there have to be\x01",
            "better ways of using it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_1596")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15EB")

    ChrTalk(    #27
        0x108,
        (
            "#075F#5PHey, now... Don't you think\x01",
            "that's a little much?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1637")

    label("loc_15EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1637")

    ChrTalk(    #28
        0x105,
        (
            "#043F#5PWh-Why would you do something\x01",
            "like this...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1637")


    ChrTalk(    #29
        0x8,
        (
            "#183FHmph. Say whatever you wish.\x02\x03",

            "#185FNow...come on!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1679():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1679)
    Sleep(10)

    def lambda_1693():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1693)
    Sleep(10)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_16E3")
    Sleep(10)

    def lambda_16D1():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16D1)
    Jump("loc_16F8")

    label("loc_16E3")


    def lambda_16E9():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_16E9)

    label("loc_16F8")

    OP_A2(0x6)

    label("loc_16FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1734")
    Sleep(10)

    def lambda_1722():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_1722)
    Jump("loc_1749")

    label("loc_1734")


    def lambda_173A():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_173A)

    label("loc_1749")

    OP_A2(0x6)

    label("loc_174C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_179D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1785")
    Sleep(10)

    def lambda_1773():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_1773)
    Jump("loc_179A")

    label("loc_1785")


    def lambda_178B():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_178B)

    label("loc_179A")

    OP_A2(0x6)

    label("loc_179D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17D6")
    Sleep(10)

    def lambda_17C4():
        OP_92(0xFE, 0xC, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_17C4)
    Jump("loc_17EB")

    label("loc_17D6")


    def lambda_17DC():
        OP_92(0xFE, 0xB, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_17DC)

    label("loc_17EB")

    OP_A2(0x6)

    label("loc_17EE")

    Sleep(50)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 20)

    def lambda_1809():
        OP_8E(0xFE, 0xCC1A, 0x0, 0xFFFFD27E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1809)
    Sleep(10)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 20)

    def lambda_1839():
        OP_8E(0xFE, 0xCC1A, 0x0, 0xFFFFC037, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1839)
    Sleep(10)

    def lambda_1859():
        OP_92(0xFE, 0x0, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1859)
    Sleep(200)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_18A2"),
        (SWITCH_DEFAULT, "loc_18A5"),
    )


    label("loc_18A2")

    OP_B4(0x0)
    Return()

    label("loc_18A5")

    EventBegin(0x0)
    SetChrPos(0x101, 57050, 0, -12660, 132)
    SetChrPos(0x102, 56160, 0, -14450, 88)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_18FC")
    SetChrPos(0x0, 57840, 0, -15280, 27)
    Jump("loc_190D")

    label("loc_18FC")

    SetChrPos(0x0, 56200, 0, -11470, 112)

    label("loc_190D")

    OP_A2(0x6)

    label("loc_1910")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1940")
    SetChrPos(0x1, 57840, 0, -15280, 27)
    Jump("loc_1951")

    label("loc_1940")

    SetChrPos(0x1, 56200, 0, -11470, 112)

    label("loc_1951")

    OP_A2(0x6)

    label("loc_1954")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1998")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1984")
    SetChrPos(0x2, 57840, 0, -15280, 27)
    Jump("loc_1995")

    label("loc_1984")

    SetChrPos(0x2, 56200, 0, -11470, 112)

    label("loc_1995")

    OP_A2(0x6)

    label("loc_1998")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_19C8")
    SetChrPos(0x3, 57840, 0, -15280, 27)
    Jump("loc_19D9")

    label("loc_19C8")

    SetChrPos(0x3, 56200, 0, -11470, 112)

    label("loc_19D9")

    OP_A2(0x6)

    label("loc_19DC")

    SetChrPos(0x8, 59690, 0, -13480, 0)
    SetChrChipByIndex(0x8, 21)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x1)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(57980, 0, -13040, 0)
    OP_67(0, 9150, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #30
        0x101,
        (
            "#007FI think she's really out of it,\x01",
            "this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#010FYeah... I don't think she'll\x01",
            "be moving for a while.\x02\x03",

            "But more importantly...since she\x01",
            "was guarding this area, this is\x01",
            "probably the way we need to go.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C16")

    ChrTalk(    #32
        0x101,
        "#004FYeah, you're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#040FIn that case, I'll have Sieg\x01",
            "call the others here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_8C(0x105, 270, 400)

    def lambda_1BB5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1BB5)

    def lambda_1BC3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1BC3)

    def lambda_1BD1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1BD1)

    def lambda_1BDF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1BDF)
    Sleep(400)

    ChrTalk(    #34
        0x105,
        "#040F#2PSieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        "#2PScreeee. ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE4")

    label("loc_1C16")


    ChrTalk(    #36
        0x101,
        (
            "#004FYeah, you're right...\x02\x03",

            "#006FOkay, I'll get Sieg to call the others.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_8C(0x101, 270, 400)

    def lambda_1C85():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1C85)

    def lambda_1C93():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1C93)

    def lambda_1CA1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1CA1)

    def lambda_1CAF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1CAF)
    Sleep(400)

    ChrTalk(    #37
        0x101,
        "#508F#4PHey, Sieg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        "#2PScreee!\x02",
    )

    CloseMessageWindow()

    label("loc_1CE4")

    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 37300, 5000, -13990, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_1D0A():
        OP_6D(52800, 0, -14030, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1D0A)

    def lambda_1D22():
        OP_8E(0xFE, 0xD8B8, 0x3E8, 0xFFFFCAF4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D22)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DA6")
    SetChrPos(0x0, 53820, 0, -7240, 45)
    Jump("loc_1DB7")

    label("loc_1DA6")

    SetChrPos(0x0, 52900, 0, -6250, 45)

    label("loc_1DB7")

    OP_A2(0x6)

    label("loc_1DBA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DEA")
    SetChrPos(0x1, 53820, 0, -7240, 45)
    Jump("loc_1DFB")

    label("loc_1DEA")

    SetChrPos(0x1, 52900, 0, -6250, 45)

    label("loc_1DFB")

    OP_A2(0x6)

    label("loc_1DFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E2E")
    SetChrPos(0x2, 53820, 0, -7240, 45)
    Jump("loc_1E3F")

    label("loc_1E2E")

    SetChrPos(0x2, 52900, 0, -6250, 45)

    label("loc_1E3F")

    OP_A2(0x6)

    label("loc_1E42")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1E72")
    SetChrPos(0x3, 53820, 0, -7240, 45)
    Jump("loc_1E83")

    label("loc_1E72")

    SetChrPos(0x3, 52900, 0, -6250, 45)

    label("loc_1E83")

    OP_A2(0x6)

    label("loc_1E86")

    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    Call(0, 14)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x1)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #39
        0x9,
        (
            "#102F#5PI was able to use that orbal reaction from\x01",
            "before to calculate the size of these ruins...\x02\x03",

            "...but it looks like we're only\x01",
            "at around the halfway mark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#007FWhew... Well, at least there's\x01",
            "that much covered.\x02\x03",

            "#003FI know we can't just rush ahead,\x01",
            "but I'm getting impatient...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#012FYeah, if we try to rush things,\x01",
            "we'll likely just wind up lost.\x02\x03",

            "We have to take it slow and steady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#104F#5PIndeed...\x01",
            "Just hang in there.\x02\x03",

            "#102FWe want to be as well-prepared\x01",
            "as possible when it comes time\x01",
            "to confront the colonel.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    EventEnd(0x0)
    Return()

    # Function_12_911 end

    def Function_13_2131(): pass

    label("Function_13_2131")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2142")
    RemoveParty(0x2, 0xFF)

    label("loc_2142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2153")
    RemoveParty(0x3, 0xFF)

    label("loc_2153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2164")
    RemoveParty(0x5, 0xFF)

    label("loc_2164")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2175")
    RemoveParty(0x4, 0xFF)

    label("loc_2175")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2186")
    RemoveParty(0x6, 0xFF)

    label("loc_2186")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2197")
    RemoveParty(0x7, 0xFF)

    label("loc_2197")

    Fade(1000)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    Call(0, 14)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #43
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )


    label("loc_2253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B5")

    Menu(
        0,
        10,
        106,
        1,
        (
            " *[Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_22B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230A")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            " *[Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_230A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235F")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            " *[Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_235F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B4")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            " *[Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_23B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2409")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            " *[Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_2409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_245F")

    Menu(
        0,
        10,
        106,
        1,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin] \x01",         # 4
            " *[Kloe]\x01",         # 5
        )
    )

    Jump("loc_24A3")

    label("loc_245F")


    Menu(
        0,
        10,
        106,
        0,
        (
            "  [Schera]\x01",       # 0
            "  [Olivier]\x01",      # 1
            "  [Agate]\x01",        # 2
            "  [Tita]\x01",         # 3
            "  [Zin]\x01",          # 4
            "  [Kloe]\x01",         # 5
        )
    )


    label("loc_24A3")

    MenuEnd(0x0)
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24CA"),
        (1, "loc_24E4"),
        (2, "loc_24FE"),
        (3, "loc_2518"),
        (4, "loc_2532"),
        (5, "loc_254C"),
        (SWITCH_DEFAULT, "loc_2566"),
    )


    label("loc_24CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24DE")
    AddParty(0x2, 0xFF)
    Jump("loc_24E1")

    label("loc_24DE")

    RemoveParty(0x2, 0xFF)

    label("loc_24E1")

    Jump("loc_25DE")

    label("loc_24E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F8")
    AddParty(0x3, 0xFF)
    Jump("loc_24FB")

    label("loc_24F8")

    RemoveParty(0x3, 0xFF)

    label("loc_24FB")

    Jump("loc_25DE")

    label("loc_24FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2512")
    AddParty(0x5, 0xFF)
    Jump("loc_2515")

    label("loc_2512")

    RemoveParty(0x5, 0xFF)

    label("loc_2515")

    Jump("loc_25DE")

    label("loc_2518")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_252C")
    AddParty(0x6, 0xFF)
    Jump("loc_252F")

    label("loc_252C")

    RemoveParty(0x6, 0xFF)

    label("loc_252F")

    Jump("loc_25DE")

    label("loc_2532")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2546")
    AddParty(0x7, 0xFF)
    Jump("loc_2549")

    label("loc_2546")

    RemoveParty(0x7, 0xFF)

    label("loc_2549")

    Jump("loc_25DE")

    label("loc_254C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2560")
    AddParty(0x4, 0xFF)
    Jump("loc_2563")

    label("loc_2560")

    RemoveParty(0x4, 0xFF)

    label("loc_2563")

    Jump("loc_25DE")

    label("loc_2566")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_257A")
    RemoveParty(0x2, 0xFF)
    Jump("loc_25DB")

    label("loc_257A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258E")
    RemoveParty(0x3, 0xFF)
    Jump("loc_25DB")

    label("loc_258E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A2")
    RemoveParty(0x5, 0xFF)
    Jump("loc_25DB")

    label("loc_25A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25B6")
    RemoveParty(0x4, 0xFF)
    Jump("loc_25DB")

    label("loc_25B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25CA")
    RemoveParty(0x6, 0xFF)
    Jump("loc_25DB")

    label("loc_25CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25DB")
    RemoveParty(0x7, 0xFF)

    label("loc_25DB")

    Jump("loc_25DE")

    label("loc_25DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2601")
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x2, 0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_268D")

    label("loc_2601")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2646")

    AnonymousTalk(    #44
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )

    Jump("loc_268D")

    label("loc_2646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268D")
    SetChrFlags(0x2, 0x80)

    AnonymousTalk(    #45
        "\x07\x05Choose two members other than Estelle and Joshua.\x02",
    )


    label("loc_268D")

    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    Jump("loc_2253")

    label("loc_26B2")

    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    Fade(1000)
    SetChrPos(0x101, 54150, 0, -5010, 45)
    SetChrPos(0x102, 55010, 0, -6060, 45)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    SetChrPos(0x2, 54470, 0, -7820, 27)
    SetChrPos(0x3, 56010, 0, -8590, 27)
    Call(0, 14)
    OP_6D(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Return()

    # Function_13_2131 end

    def Function_14_275E(): pass

    label("Function_14_275E")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 55790, 0, -4250, 225)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 60460, 0, 480, 90)
    SetChrChipByIndex(0x8, 21)
    ClearChrFlags(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C0")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 55690, 0, 1000, 180)
    Jump("loc_27C5")

    label("loc_27C0")

    SetChrFlags(0x10, 0x80)

    label("loc_27C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27EC")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 54740, 0, -1560, 180)
    Jump("loc_27F1")

    label("loc_27EC")

    SetChrFlags(0x11, 0x80)

    label("loc_27F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2818")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 57870, 0, -2040, 225)
    Jump("loc_281D")

    label("loc_2818")

    SetChrFlags(0xE, 0x80)

    label("loc_281D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2844")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 57210, 0, -860, 225)
    Jump("loc_2849")

    label("loc_2844")

    SetChrFlags(0xD, 0x80)

    label("loc_2849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2870")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 59350, 0, -3220, 225)
    Jump("loc_2875")

    label("loc_2870")

    SetChrFlags(0x12, 0x80)

    label("loc_2875")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289C")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 56420, 0, -2530, 225)
    Jump("loc_28A1")

    label("loc_289C")

    SetChrFlags(0xF, 0x80)

    label("loc_28A1")

    Return()

    # Function_14_275E end

    def Function_15_28A2(): pass

    label("Function_15_28A2")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)

    def lambda_28DA():

        label("loc_28DA")

        OP_7C(0x0, 0x64, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_28DA")

    QueueWorkItem2(0x9, 3, lambda_28DA)
    OP_22(0x85, 0x1, 0x64)
    LoadEffect(0x1, "map\\\\mp015_00.eff")
    OP_43(0x101, 0x0, 0x0, 0x10)
    OP_6D(55710, 0, -7780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(134000, 0)
    OP_6E(513, 0)
    FadeToBright(2000, 0)
    Sleep(600)
    OP_77(0xC8, 0xC8, 0xC8, 0xBB800, 0x0)

    def lambda_2969():
        OP_6D(-130, 0, -14000, 3500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2969)

    def lambda_2981():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_2981)
    Sleep(400)
    OP_B0(0x3, 0xA)
    OP_B0(0x4, 0xA)
    OP_B0(0x5, 0xA)
    OP_B0(0x6, 0xA)
    OP_B0(0x7, 0xA)
    OP_B0(0x8, 0xA)
    OP_B0(0x9, 0xA)
    OP_B0(0xA, 0xA)
    OP_B0(0xB, 0xA)
    OP_B0(0xC, 0xA)
    OP_B0(0xD, 0xA)
    OP_B0(0xE, 0xA)
    OP_B0(0xF, 0xA)
    OP_B0(0x10, 0xA)
    OP_B0(0x11, 0xA)
    OP_B0(0x12, 0xA)
    OP_B0(0x13, 0xA)
    OP_B0(0x14, 0xA)
    OP_B0(0x15, 0xA)
    OP_B0(0x16, 0xA)
    OP_6F(0x3, 18)
    OP_6F(0x4, 18)
    OP_6F(0x5, 18)
    OP_6F(0x6, 18)
    OP_6F(0x7, 18)
    OP_6F(0x8, 18)
    OP_6F(0x9, 18)
    OP_6F(0xA, 18)
    OP_6F(0xB, 18)
    OP_6F(0xC, 18)
    OP_6F(0xD, 18)
    OP_6F(0xE, 18)
    OP_6F(0xF, 18)
    OP_6F(0x10, 18)
    OP_6F(0x11, 18)
    OP_6F(0x12, 18)
    OP_6F(0x13, 18)
    OP_6F(0x14, 18)
    OP_6F(0x15, 18)
    OP_6F(0x16, 18)
    Sleep(250)
    OP_70(0xF, 0x14)
    OP_70(0x10, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x4, 0x14)
    OP_70(0x3, 0x14)
    Sleep(250)
    OP_70(0x13, 0x14)
    OP_70(0x14, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x16, 0x14)
    OP_70(0x15, 0x14)
    Sleep(250)
    Sleep(250)
    OP_70(0x7, 0x14)
    OP_70(0x5, 0x14)

    def lambda_2AE0():
        OP_6E(665, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2AE0)
    Sleep(250)
    Sleep(500)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 4500, 4500, 4500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x0, 0x1)
    OP_77(0x8C, 0x8C, 0x8C, 0x7D000, 0x0)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_6F(0x0, 4000)
    OP_6F(0x1, 4000)
    OP_6F(0x2, 4000)
    OP_70(0x0, 0xFDC)
    OP_70(0x1, 0xFDC)
    OP_70(0x2, 0xFDC)

    def lambda_2B7B():
        OP_6D(280, 0, 25240, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B7B)
    Sleep(200)
    OP_70(0xE, 0x14)
    OP_70(0x6, 0x14)
    Sleep(200)
    OP_70(0x8, 0x14)
    OP_70(0xD, 0x14)
    Sleep(200)
    OP_70(0xC, 0x14)
    OP_70(0x9, 0x14)
    Sleep(100)
    OP_70(0xB, 0x14)
    OP_70(0x11, 0x14)
    Sleep(100)
    OP_70(0xA, 0x14)
    Sleep(100)
    OP_70(0x12, 0x14)
    Sleep(500)
    Sleep(1000)
    Fade(1000)
    OP_6D(57500, 0, -2650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #46
        0x9,
        "#105F#5PDamn! It's a total orbal shutdown!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_24(0x85, 0x5A)
    Sleep(200)
    OP_24(0x85, 0x50)
    Sleep(200)
    OP_24(0x85, 0x46)
    Sleep(200)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_28A2 end

    def Function_16_2CDA(): pass

    label("Function_16_2CDA")

    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x6, 0x2)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1100)
    OP_22(0x91, 0x0, 0x64)
    PlayEffect(0x1, 0xFF, 0xFF, 67290, 1000, -13940, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sleep(800)
    Sleep(800)
    Sleep(800)
    Sleep(500)
    Return()

    # Function_16_2CDA end

    def Function_17_2DAF(): pass

    label("Function_17_2DAF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #47
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F6D")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_72(0x19, 0x20)
    OP_6F(0x19, 300)
    OP_70(0x19, 0x1F4)
    OP_73(0x19)
    OP_6F(0x19, 500)
    OP_70(0x19, 0x2BC)
    OP_71(0x19, 0x20)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x5, "map\\\\mp027_01.eff")
    PlayEffect(0x5, 0x6, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1500, 0, -1)
    Sleep(1500)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x6, 0x0)
    LoadEffect(0x5, "map\\\\mp027_00.eff")
    PlayEffect(0x5, 0x0, 0xFF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x19, 0)
    OP_70(0x19, 0xFA)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F87")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2F87")

    Return()

    # Function_17_2DAF end

    SaveToFile()

Try(main)
