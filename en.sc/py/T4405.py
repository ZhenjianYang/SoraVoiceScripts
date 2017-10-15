from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4405   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4405.x',
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
        'Duncan',                               # 9
        'Phelio',                               # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
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
        'ED6_DT06/CH20042 ._CH',             # 0E
        'ED6_DT07/CH00440 ._CH',             # 0F
        'ED6_DT07/CH00441 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
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
        'ED6_DT06/CH20042P._CP',             # 0E
        'ED6_DT07/CH00440P._CP',             # 0F
        'ED6_DT07/CH00441P._CP',             # 10
    )

    DeclNpc(
        X                   = 1500,
        Z                   = 0,
        Y                   = 10870,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 1050,
        TriggerZ            = 0,
        TriggerY            = 10640,
        TriggerRange        = 800,
        ActorX              = 150,
        ActorZ              = 1700,
        ActorY              = 10640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_2BE",          # 01, 1
        "Function_2_2C4",          # 02, 2
        "Function_3_441",          # 03, 3
        "Function_4_571",          # 04, 4
        "Function_5_5F2",          # 05, 5
        "Function_6_EA3",          # 06, 6
        "Function_7_18F9",         # 07, 7
        "Function_8_193D",         # 08, 8
        "Function_9_1995",         # 09, 9
        "Function_10_19D9",        # 0A, 10
        "Function_11_19F5",        # 0B, 11
        "Function_12_1A11",        # 0C, 12
        "Function_13_1AA9",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_202"),
        (SWITCH_DEFAULT, "loc_216"),
    )


    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_213")

    Jump("loc_216")

    label("loc_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_2BD")
    SetChrPos(0x9, 4840, 0, -2540, 0)
    SetChrPos(0x8, 4250, 0, -210, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrFlags(0xA, 0x800)
    SetChrChipByIndex(0xA, 14)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 5)
    SetChrSubChip(0xB, 6)
    SetChrSubChip(0xC, 0)
    SetChrPos(0xA, 4350, 0, -1320, 90)
    SetChrPos(0xB, 3100, 0, -2250, 90)
    SetChrPos(0xC, 2980, 0, 200, 90)

    label("loc_2BD")

    Return()

    # Function_0_1F6 end

    def Function_1_2BE(): pass

    label("Function_1_2BE")

    OP_71(0x1, 0x4)
    Return()

    # Function_1_2BE end

    def Function_2_2C4(): pass

    label("Function_2_2C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E9")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_42B")

    label("loc_2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_42B")

    label("loc_302")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_42B")

    label("loc_31B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_334")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_42B")

    label("loc_334")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34D")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_42B")

    label("loc_34D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_42B")

    label("loc_366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37F")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_42B")

    label("loc_37F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_398")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_42B")

    label("loc_398")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_42B")

    label("loc_3B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CA")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_42B")

    label("loc_3CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_42B")

    label("loc_3E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_42B")

    label("loc_3FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_42B")

    label("loc_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_42B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_440")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42B")

    label("loc_440")

    Return()

    # Function_2_2C4 end

    def Function_3_441(): pass

    label("Function_3_441")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_56D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4E4")

    ChrTalk(    #0
        0xFE,
        (
            "Th-Those guys were the\x01",
            "Intelligence Division's\x01",
            "Special Ops forces, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I wonder what they plan\x01",
            "on doing with the sample\x01",
            "engine...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56D")

    label("loc_4E4")


    ChrTalk(    #2
        0xFE,
        "W-We've been on watch 24-7.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "These guys suddenly showed\x01",
            "up and busted in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "The engine was gone in the\x01",
            "blink of an eye!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_56D")

    TalkEnd(0xFE)
    Return()

    # Function_3_441 end

    def Function_4_571(): pass

    label("Function_4_571")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 4)), scpexpr(EXPR_END)), "loc_5EE")

    ChrTalk(    #5
        0xFE,
        (
            "Those guys took the engine\x01",
            "towards the wharf!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Damn it all! The queen was\x01",
            "counting on us to keep it safe!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE")

    TalkEnd(0xFE)
    Return()

    # Function_4_571 end

    def Function_5_5F2(): pass

    label("Function_5_5F2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    Call(0, 12)

    label("loc_605")

    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_6D(2320, 0, 13530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 3350, 0, 4000, 180)
    SetChrPos(0x9, 4390, 0, 4000, 180)
    SetChrPos(0xA, 3720, 0, 2280, 0)
    SetChrPos(0xB, 4770, 0, 960, 0)
    SetChrPos(0xC, 3440, 0, 750, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    def lambda_6C3():
        OP_6D(3240, 0, 3110, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C3)

    def lambda_6DB():
        OP_67(0, 7500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6DB)

    def lambda_6F3():
        OP_6B(2740, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6F3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #7
        0x8,
        "#4PYou... What's the meaning of this?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#4PDo you know what the army will do\x01",
            "to you when they--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        "#3PHah. We're ready for the worst!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xB,
        (
            "#5PIf you don't want to get hurt,\x01",
            "then behave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        "#5PWe have no interest in harming civilians.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xC,
        "#1PUnless...they get in the way.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #13
        0x9,
        "#4PAaah! No, no, please, let me live!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_890")
    SetChrChipByIndex(0x106, 7)
    Jump("loc_895")

    label("loc_890")

    SetChrChipByIndex(0x103, 5)

    label("loc_895")

    SetChrChipByIndex(0x109, 9)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF7, 0x80)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x101, 10400, 0, 0, 270)
    SetChrPos(0xF7, 11500, 0, 500, 270)
    SetChrPos(0x109, 11500, 0, -1000, 270)

    ChrTalk(    #14
        0x101,
        (
            "#1PYeah, you really look like you're not\x01",
            "harming civilians there, buddy.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_9A8():
        OP_6D(7050, 0, 1380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A8)

    def lambda_9C0():
        OP_67(0, 7500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9C0)

    def lambda_9D8():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_9D8)

    def lambda_9E8():
        OP_6E(295, 1500)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_9E8)

    def lambda_9F8():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9F8)
    Sleep(50)

    def lambda_A0B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A0B)
    Sleep(50)

    def lambda_A1E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A1E)
    Sleep(50)

    def lambda_A31():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A31)
    Sleep(50)

    def lambda_A44():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A44)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF7, 0x2)
    WaitChrThread(0xF7, 0x3)

    ChrTalk(    #15
        0xA,
        "#4PHm?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        "#6PWhat? BRACERS!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1060F#2POne of us isn't, but...eh, close enough\x01",
            "for Intelligence Division work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBB")

    ChrTalk(    #18
        0x106,
        (
            "#053F#2PSo this is where you idiots are.\x01",
            "Dragging us all over like that...\x02\x03",

            "#054FIn accordance with the laws of the Bracer Guild,\x01",
            "you are hereby under arrest for the\x01",
            "destruction of property and rioting!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8A")

    label("loc_BBB")


    ChrTalk(    #19
        0x103,
        (
            "#027F#2PNaughty, naughty, making us chase you boys\x01",
            "like that. Now then...\x02\x03",

            "#024FIn accordance with the laws of the Bracer Guild,\x01",
            "you are hereby under arrest for the\x01",
            "destruction of property and rioting!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8A")


    ChrTalk(    #20
        0x101,
        (
            "#1006F#2PSurrender now and I promise not to break\x01",
            "your legs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "#3PDamn it all! How'd they find us?!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xB, 11)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        "#6PDoes it matter? Put them in their graves!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 15)
    Sleep(200)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xC, 11)
    Sleep(500)

    ChrTalk(    #23
        0xC,
        "#3P#1KSir!\x02",
    )


    ChrTalk(    #24
        0xA,
        "#4P#1KSir!\x02",
    )

    OP_56(0x1)
    OP_59()

    def lambda_D86():
        OP_6D(7950, 0, 330, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D86)

    def lambda_D9E():
        OP_6B(2200, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D9E)
    SetChrChipByIndex(0xA, 16)
    SetChrChipByIndex(0xB, 12)
    SetChrChipByIndex(0xC, 12)

    def lambda_DBD():
        OP_8F(0xFE, 0x1AB8, 0x0, 0x208, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_DBD)

    def lambda_DD8():
        OP_8F(0xFE, 0x1FCC, 0x0, 0x122, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DD8)
    Sleep(50)

    def lambda_DF8():
        OP_8F(0xFE, 0x184C, 0x0, 0x654, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_DF8)

    def lambda_E13():
        OP_8F(0xFE, 0x23E6, 0x0, 0x316, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_E13)
    Sleep(50)

    def lambda_E33():
        OP_8F(0xFE, 0x168A, 0x0, 0xFFFFFF24, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E33)

    def lambda_E4E():
        OP_8F(0xFE, 0x22A6, 0x0, 0xFFFFFC54, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E4E)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x109, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x45C, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_E99"),
        (SWITCH_DEFAULT, "loc_E9E"),
    )


    label("loc_E99")

    OP_B4(0x0)
    Jump("loc_E9E")

    label("loc_E9E")

    Call(0, 6)
    Return()

    # Function_5_5F2 end

    def Function_6_EA3(): pass

    label("Function_6_EA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_6D(4990, 0, -810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x109, 65535)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0xB, 14)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xA, 3)
    SetChrSubChip(0xB, 6)
    SetChrSubChip(0xC, 0)
    SetChrPos(0x101, 6550, 0, -800, 270)
    SetChrPos(0xF7, 6580, 0, -2100, 270)
    SetChrPos(0x109, 7740, 0, -1420, 270)
    SetChrPos(0x8, 3350, 0, 4000, 180)
    SetChrPos(0x9, 4390, 0, 4000, 180)
    SetChrPos(0xA, 4350, 0, -1320, 90)
    SetChrPos(0xB, 3100, 0, -2250, 90)
    SetChrPos(0xC, 2980, 0, 200, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #25
        0xA,
        "#5PHah...well...we bought the captain some time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        "#5PThe rest is in...her hands...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        "#5PLong live...Colonel Richard's dream!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0xA, 0x800)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 14)
    SetChrSubChip(0xA, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x101,
        "#1020F#2PH-Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1068FHe's out like a light.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1168")

    ChrTalk(    #31
        0x101,
        (
            "#1019F#2PHey, Agate. They said 'captain.'\x01",
            "You...don't think...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #32
        0x106,
        (
            "#552F#5PYeah, it's probably HER.\x01",
            "More lives than a cat, I swear...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1218")

    label("loc_1168")


    ChrTalk(    #33
        0x101,
        (
            "#1019F#2PHey, Schera. They said 'captain.'\x01",
            "You...don't think...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #34
        0x103,
        (
            "#022F#5PYes, it's probably Colonel Richard's aide.\x01",
            "She struck me as the type to never give up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1218")


    def lambda_121E():
        OP_6D(6450, 0, 120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_121E)

    def lambda_1236():
        OP_8E(0xFE, 0x1B58, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1236)
    Sleep(400)

    def lambda_1256():
        OP_8E(0xFE, 0x1770, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1256)
    Sleep(400)

    def lambda_1276():

        label("loc_1276")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1276")

    QueueWorkItem2(0x101, 2, lambda_1276)

    def lambda_1287():

        label("loc_1287")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1287")

    QueueWorkItem2(0xF7, 2, lambda_1287)

    def lambda_1298():

        label("loc_1298")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1298")

    QueueWorkItem2(0x109, 2, lambda_1298)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0x109, 0x2)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #35
        0x8,
        "#4PTh-Thank you SO MUCH, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#4PThank you, thank you!\x01",
            "We owe you our lives!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1016F#6PHaha! All part of the job, folks!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 315, 400)

    ChrTalk(    #38
        0x101,
        "#1004F#6PEr...\x02",
    )

    CloseMessageWindow()

    def lambda_1395():
        OP_6D(-890, 0, 9800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1395)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(6450, 0, 120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    OP_0D()

    ChrTalk(    #39
        0x101,
        "#1020F#6P#3SOh, man!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 600)

    def lambda_141B():

        label("loc_141B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_141B")

    QueueWorkItem2(0x9, 1, lambda_141B)

    def lambda_142C():

        label("loc_142C")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_142C")

    QueueWorkItem2(0x8, 1, lambda_142C)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)

    def lambda_1449():
        OP_6D(3120, 0, 9680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1449)

    def lambda_1461():
        OP_6B(2760, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1461)
    Sleep(2500)
    OP_43(0xF7, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x109, 0x1, 0x0, 0x9)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BE")

    ChrTalk(    #40
        0x106,
        "#052FSomethin' wrong?\x02",
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_14BE")


    ChrTalk(    #41
        0x103,
        "#023FEstelle? What is it?\x02",
    )

    CloseMessageWindow()

    label("loc_14DD")

    WaitChrThread(0x109, 0x1)

    ChrTalk(    #42
        0x109,
        (
            "#1064F#4PWell, THAT'S an orbment.\x01",
            "Good grief!\x02\x03",

            "What the heck do you use somethin'\x01",
            "this big for?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)

    ChrTalk(    #43
        0x101,
        (
            "#1020F#6PThis is the new super-engine for the\x01",
            "Arseille!\x02\x03",

            "But aren't there supposed to be two\x01",
            "of them?!\x02",
        )
    )

    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_43(0x8, 0x1, 0x0, 0xA)
    Sleep(300)
    OP_43(0x9, 0x1, 0x0, 0xB)
    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x1)
    OP_6D(2660, 0, 7880, 1000)

    ChrTalk(    #44
        0x8,
        (
            "#5PYeah... Some of those guys took the other\x01",
            "on a lift.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "#5PThey took it farther in to the harbor.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 180, 500)

    def lambda_1685():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1685)
    OP_8C(0x109, 180, 400)

    ChrTalk(    #46
        0x101,
        "#1005F#6PYOU'RE KIDDING!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175E")

    ChrTalk(    #47
        0x106,
        "#552F#6PDamn it. This can mean nothing good.\x02",
    )

    CloseMessageWindow()

    def lambda_16F8():
        OP_6D(3120, 0, 9680, 1000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_16F8)
    OP_8C(0x106, 315, 400)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #48
        0x106,
        (
            "#054F#5PEstelle, Kevin!\x01",
            "C'mon, we gotta get down to the harbor!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F1")

    label("loc_175E")


    ChrTalk(    #49
        0x103,
        (
            "#522F#6PThat can only mean bad things\x01",
            "for everyone...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_179F():
        OP_6D(3120, 0, 9680, 1000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_179F)
    OP_8C(0x103, 315, 400)
    WaitChrThread(0xF7, 0x1)

    ChrTalk(    #50
        0x103,
        "#024F#5PEstelle, Kevin! We need to give chase!\x02",
    )

    CloseMessageWindow()

    label("loc_17F1")

    OP_8C(0x101, 135, 500)

    ChrTalk(    #51
        0x101,
        "#1005F#6PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        "#1062F#4PRight behind you!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2990, 0, 9730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2990, 0, 9730, 90)
    SetChrPos(0x1, 2990, 0, 9730, 90)
    SetChrPos(0x2, 2990, 0, 9730, 90)
    OP_69(0x0, 0x0)
    SetChrPos(0x9, 4840, 0, -2540, 0)
    SetChrPos(0x8, 4250, 0, -210, 270)
    OP_4B(0x9, 255)
    OP_4B(0x8, 255)
    OP_A2(0x163C)
    OP_28(0x8E, 0x1, 0x4)
    OP_28(0x8E, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_EA3 end

    def Function_7_18F9(): pass

    label("Function_7_18F9")

    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0x8FC, 0x0, 0x2580, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_7_18F9 end

    def Function_8_193D(): pass

    label("Function_8_193D")

    OP_8E(0xFE, 0x1946, 0x0, 0xFFFFFDA8, 0x1388, 0x0)
    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0xDFC, 0x0, 0x21AC, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_193D end

    def Function_9_1995(): pass

    label("Function_9_1995")

    OP_8E(0xFE, 0x292C, 0x0, 0xB36, 0x1388, 0x0)
    OP_8E(0xFE, 0x2990, 0x0, 0x1A72, 0x1388, 0x0)
    OP_8E(0xFE, 0xE2E, 0x0, 0x27BA, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1995 end

    def Function_10_19D9(): pass

    label("Function_10_19D9")

    OP_8E(0xFE, 0xDDE, 0x0, 0xBCC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_19D9 end

    def Function_11_19F5(): pass

    label("Function_11_19F5")

    OP_8E(0xFE, 0x1220, 0x0, 0xAF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_19F5 end

    def Function_12_1A11(): pass

    label("Function_12_1A11")

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
        (0, "loc_1A8A"),
        (1, "loc_1A90"),
        (SWITCH_DEFAULT, "loc_1A96"),
    )


    label("loc_1A8A")

    OP_A2(0x1200)
    Jump("loc_1A96")

    label("loc_1A90")

    OP_A2(0x1201)
    Jump("loc_1A96")

    label("loc_1A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1AA4")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_1AA8")

    label("loc_1AA4")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_1AA8")

    Return()

    # Function_12_1A11 end

    def Function_13_1AA9(): pass

    label("Function_13_1AA9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05The new model engine for the Arseille is here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1AA9 end

    SaveToFile()

Try(main)
