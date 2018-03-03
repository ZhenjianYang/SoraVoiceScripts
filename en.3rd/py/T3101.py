from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3101   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Priam',                                # 9
        'Irene',                                # 10
        'Rehmann',                              # 11
        'Elise',                                # 12
        'Vince',                                # 13
        'Muriel',                               # 14
        'Erika',                                # 15
        'Dan',                                  # 16
        'Professor Russell',                    # 17
        'Factory Chief Murdock',                # 18
        'Agate',                                # 19
        ' ',                                    # 20
        'Landing Craft',                        # 21
        'Landing Craft',                        # 22
        'Landing Craft Shadow',                 # 23
        'Landing Craft Shadow',                 # 24
        'Target Camera',                        # 25
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT27/CH03970 ._CH',             # 02
        'ED6_DT27/CH03980 ._CH',             # 03
        'ED6_DT07/CH02020 ._CH',             # 04
        'ED6_DT07/CH02620 ._CH',             # 05
        'ED6_DT06/CH20141 ._CH',             # 06
        'ED6_DT06/CH20053 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01050 ._CH',             # 09
        'ED6_DT07/CH01130 ._CH',             # 0A
        'ED6_DT07/CH01470 ._CH',             # 0B
        'ED6_DT26/CH20751 ._CH',             # 0C
        'ED6_DT26/CH20752 ._CH',             # 0D
        'ED6_DT26/CH20758 ._CH',             # 0E
        'ED6_DT26/CH20759 ._CH',             # 0F
        'ED6_DT26/CH20698 ._CH',             # 10
        'ED6_DT26/CH20699 ._CH',             # 11
        'ED6_DT26/CH20753 ._CH',             # 12
        'ED6_DT26/CH20754 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT27/CH03970P._CP',             # 02
        'ED6_DT27/CH03980P._CP',             # 03
        'ED6_DT07/CH02020P._CP',             # 04
        'ED6_DT07/CH02620P._CP',             # 05
        'ED6_DT06/CH20141P._CP',             # 06
        'ED6_DT06/CH20053P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01050P._CP',             # 09
        'ED6_DT07/CH01130P._CP',             # 0A
        'ED6_DT07/CH01470P._CP',             # 0B
        'ED6_DT26/CH20751P._CP',             # 0C
        'ED6_DT26/CH20752P._CP',             # 0D
        'ED6_DT26/CH20758P._CP',             # 0E
        'ED6_DT26/CH20759P._CP',             # 0F
        'ED6_DT26/CH20698P._CP',             # 10
        'ED6_DT26/CH20699P._CP',             # 11
        'ED6_DT26/CH20753P._CP',             # 12
        'ED6_DT26/CH20754P._CP',             # 13
    )

    DeclNpc(
        X                   = -26340,
        Z                   = 8000,
        Y                   = 65489,
        Direction           = 74,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -18800,
        Z                   = 8000,
        Y                   = 64430,
        Direction           = 164,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24430,
        Z                   = 8000,
        Y                   = 68160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -14900,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -16239,
        Z                   = 8000,
        Y                   = 63190,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -104390,
        Z                   = 0,
        Y                   = 8560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0xE6,
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
        NpcIndex            = 0xE6,
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
        NpcIndex            = 0xE6,
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
        NpcIndex            = 0xE6,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_3FA",          # 01, 1
        "Function_2_4BB",          # 02, 2
        "Function_3_4F3",          # 03, 3
        "Function_4_509",          # 04, 4
        "Function_5_679",          # 05, 5
        "Function_6_807",          # 06, 6
        "Function_7_927",          # 07, 7
        "Function_8_2847",         # 08, 8
        "Function_9_569D",         # 09, 9
        "Function_10_56D3",        # 0A, 10
        "Function_11_5719",        # 0B, 11
        "Function_12_5838",        # 0C, 12
        "Function_13_5880",        # 0D, 13
        "Function_14_58C8",        # 0E, 14
        "Function_15_5904",        # 0F, 15
        "Function_16_5915",        # 10, 16
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3A2")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -38800, 25000, 59000, 90)

    label("loc_3A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_3BE"),
        (105, "loc_3BE"),
        (SWITCH_DEFAULT, "loc_3D1"),
    )


    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3CE")
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_3CE")

    Jump("loc_3D1")

    label("loc_3D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3F9")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_3F9")

    Return()

    # Function_0_36A end

    def Function_1_3FA(): pass

    label("Function_1_3FA")

    OP_16(0x2, 0xFA0, 0xFFFDB228, 0xFFFEF278, 0x230052)
    OP_6F(0x3, 0)
    OP_72(0x1003, 0x0)
    ExitThread()
    SoundDistance(0xA0, 0xFFFFEDF4, 0x14C8, 0xE790, 0x2710, 0x7530, 0x64, 0x0)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_71(0x9, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0xA, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0xB, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0xC, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493")
    OP_10(0x9, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()

    label("loc_493")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")
    OP_10(0x9, 0x0)
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x7, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x8, 0x0)
    ExitThread()

    label("loc_4BA")

    Return()

    # Function_1_3FA end

    def Function_2_4BB(): pass

    label("Function_2_4BB")

    OP_72(0x2005, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()

    label("loc_4C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F2")
    OP_6F(0x5, 40)
    OP_70(0x5, 0x0)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x28)
    OP_73(0x5)
    Jump("loc_4C7")

    label("loc_4F2")

    Return()

    # Function_2_4BB end

    def Function_3_4F3(): pass

    label("Function_3_4F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_508")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_3_4F3")

    label("loc_508")

    Return()

    # Function_3_4F3 end

    def Function_4_509(): pass

    label("Function_4_509")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5B1")

    ChrTalk(    #0
        0xFE,
        (
            "Wait! I need to stop wasting time talking and\x01",
            "get back to doing business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Up for an ice-cold soda, my friend? I've got\x01",
            "other drinks, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_675")

    label("loc_5B1")


    ChrTalk(    #2
        0xFE,
        (
            "The factory ship's in the landing port for the\x01",
            "first time in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It's been going all over the place helping to get\x01",
            "the country back in order, so it hasn't been here\x01",
            "much lately.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_675")

    TalkEnd(0xFE)
    Return()

    # Function_4_509 end

    def Function_5_679(): pass

    label("Function_5_679")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_803")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_735")

    ChrTalk(    #4
        0xFE,
        (
            "I was so shocked I went into hiding, so I didn't\x01",
            "see what happened after that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "...b-but I still can't help but wonder who they\x01",
            "were and what they wanted...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_803")

    label("loc_735")


    ChrTalk(    #6
        0xFE,
        "I saw something absolutely crazy the other day.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I was here selling flowers like I usually do,\x01",
            "when all of a sudden, people started raining\x01",
            "down from the sky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I-I couldn't believe my eyes!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_803")

    TalkEnd(0xFE)
    Return()

    # Function_5_679 end

    def Function_6_807(): pass

    label("Function_6_807")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8A0")

    ChrTalk(    #9
        0xFE,
        (
            "This rest isn't gonna last for long, though.\x01",
            "I've gotta take off again real soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Hmm... Where were we going next, anyway?\x02",
    )

    CloseMessageWindow()
    Jump("loc_923")

    label("loc_8A0")


    ChrTalk(    #11
        0xFE,
        "Whew... It feels good to finally take a breather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I've been so busy lately, it feels like I've never\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_923")

    TalkEnd(0xFE)
    Return()

    # Function_6_807 end

    def Function_7_927(): pass

    label("Function_7_927")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(-49000, 25140, 59860, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x106, 0x80)
    FadeToBright(2000, 0)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_999"),
        (105, "loc_A1B"),
        (SWITCH_DEFAULT, "loc_AA4"),
    )


    label("loc_999")

    SetChrPos(0x106, -50970, 25000, 54170, 90)
    ClearChrFlags(0x106, 0x80)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(300)

    def lambda_9CB():
        OP_8E(0xFE, 0xFFFF452A, 0x61A8, 0xD37C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9CB)
    Sleep(800)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    WaitChrThread(0x106, 0x1)

    def lambda_9FE():
        OP_8E(0xFE, 0xFFFF4642, 0x625C, 0xE632, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_9FE)
    WaitChrThread(0x106, 0x1)
    Jump("loc_AA4")

    label("loc_A1B")

    SetChrPos(0x106, -51070, 25000, 63810, 180)
    ClearChrFlags(0x106, 0x80)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3B)
    OP_73(0x3)
    Sleep(300)

    def lambda_A4D():
        OP_8E(0xFE, 0xFFFF3940, 0x61A8, 0xF032, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A4D)
    WaitChrThread(0x106, 0x1)
    OP_6F(0x2, 59)
    OP_70(0x2, 0x0)

    def lambda_A7B():
        OP_8E(0xFE, 0xFFFF4642, 0x625C, 0xE632, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A7B)
    WaitChrThread(0x106, 0x1)
    Sleep(300)
    OP_8C(0x106, 180, 400)
    Jump("loc_AA4")

    label("loc_AA4")

    Sleep(300)

    ChrTalk(    #13
        0x106,
        (
            "#552F#5PBah... Just where have those two gone?\x02\x03",

            "I can't find 'em anywhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_51(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0xBB8)

    def lambda_B52():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_B52)

    def lambda_B60():
        OP_6D(-41660, 25180, 59860, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_B60)
    WaitChrThread(0x20, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_11(0xA4, 0xB7, 0xFF, 0x9470, 0x249F0, 0x0)
    OP_6D(-46180, 25180, 59000, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_BD4():
        OP_6D(-38510, 25000, 59800, 5000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_BD4)

    def lambda_BEC():
        OP_6C(65000, 5000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_BEC)

    def lambda_BFC():
        OP_6B(2650, 5000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_BFC)

    def lambda_C0C():
        OP_8F(0xFE, 0xFFFF60DC, 0x61A8, 0xE8EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C0C)
    WaitChrThread(0x106, 0x1)
    Sleep(500)

    NpcTalk(    #14
        0x17,
        "Engineer",
        (
            "#1464F#5PHey there.\x02\x03",

            "#1460FYou must be Agate.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #15
        0x106,
        (
            "#057F#6P(Who's this guy? He doesn't seem like any\x01",
            "ordinary engineer...)\x02\x03",

            "...\x02\x03",

            "#053FOh, I get it now. You're Dan, right?\x02\x03",

            "#051FSeem to remember hearing you were a bracer\x01",
            "at one point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x17,
        "#1463F#5POh? Was it Cassius who told you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        (
            "#052F#6PO-Oh. No...\x02\x03",

            "#050FI've just heard some stuff about you from\x01",
            "Tita and her grandpa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        (
            "#1464F#5P...\x02\x03",

            "#1460FHaha. Right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x106,
        (
            "#555F#6P(Actually, he quit the whole bracer thing\x01",
            "about ten years back, didn't he?)\x02\x03",

            "(Makes it right around with Cassius joined.)\x02\x03",

            "#552F...\x02\x03",

            "(I can't imagine him being as much of a\x01",
            "lunatic...but who knows?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #20
        0x106,
        (
            "#053F#6PYou guys're developing a new weapon, right?\x02\x03",

            "#050FI heard you've got Tita helping you out with it.\x01",
            "That true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x17,
        (
            "#1463F#5POh... Yeah.\x02\x03",

            "#1464FShe's not just a simple assistant, however--\x01",
            "she's a formal member of its development\x01",
            "team.\x02\x03",

            "#1465FTita's become so much more capable over\x01",
            "these past couple years.\x02\x03",

            "I don't even feel like there's all that much\x01",
            "I can teach to her anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x106,
        "#552F#6P(Ugh... I was right.)\x02",
    )

    CloseMessageWindow()

    def lambda_109C():
        OP_6D(-38220, 25000, 59930, 1200)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_109C)

    def lambda_10B4():
        OP_8F(0xFE, 0xFFFF630C, 0x61A8, 0xE8EE, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_10B4)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x106, 0x2)
    Sleep(500)

    ChrTalk(    #23
        0x106,
        (
            "#057F#6PWhat the hell have you guys got your\x01",
            "own kid doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x17,
        "#1460F#5PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#053F#6PI know you're busy and that you can't afford to be\x01",
            "back home here that often.\x02\x03",

            "And I know the little squirt loves orbal tech, so part\x01",
            "of me gets why you'd want her to help with whatever\x01",
            "new stuff you've got in the works...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #26
        0x106,
        (
            "#054F#6P...but that doesn't make it okay to let someone that\x01",
            "young work on developing a new weapon!\x02\x03",

            "Use some common goddamn sense, man!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_1D(0x75)
    Sleep(500)

    ChrTalk(    #27
        0x17,
        "#1461F#5PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        "#057F#6PWhat's so funny?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 270, 400)
    Sleep(300)

    ChrTalk(    #29
        0x17,
        (
            "#1464F#11PAgate, do you...\x02\x03",

            "#1462FDo you trust her?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #30
        0x106,
        (
            "#055F#6PWhat's trust got to do with this?\x02\x03",

            "#054FAnd don't go tryin' to change the subject on me!\x01",
            "What you've got her doing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x17,
        (
            "#1465F#11PI've heard a lot about you since coming back\x01",
            "here.\x02\x03",

            "And with that, there's just one question I want\x01",
            "to hear the answer to from you directly.\x02\x03",

            "#1464FNow, it's my understanding that you've\x01",
            "been keeping her company quite often\x01",
            "while my wife and I were away.\x02\x03",

            "Is that because you feel she's unreliable?\x01",
            "Or maybe just a coincidence? Or is there\x01",
            "some other reason?\x02\x03",

            "#1462F...Just what have you been trying to achieve\x01",
            "by being with her so much?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#055F#6PWh-Wha...? I wasn't trying to 'achieve' anything.\x02\x03",

            "#552FGuess if I had to give an answer...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0xFFFF)
    Sleep(500)

    ChrTalk(    #33
        0x106,
        (
            "#053F#6PThere's no denying how much she's helped me.\x02\x03",

            "I'll admit, at the start she seemed like she could\x01",
            "do jack all, and I stuck around to protect her.\x02\x03",

            "#556F...But she never actually needed it--she's ended\x01",
            "up doing way more for me than I ever did for her\x01",
            "in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        "#1463F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        (
            "#051F#6PSo yeah. I guess when I put it that way,\x01",
            "I do trust her.\x02\x03",

            "Your daughter's pretty damn amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x17,
        "#1464F#11PI see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #37
        0x106,
        (
            "#555F#6P(Okay, so he doesn't seem to have as\x01",
            "many screws loose as his wife...)\x02\x03",

            "(I can probably give him a pass, right?)\x02\x03",

            "#053F...\x02\x03",

            "#050F...Look. I'm guessing there's some special reason\x01",
            "Tita ended up involved in developing that weapon\x01",
            "of yours, right?\x02\x03",

            "You mind telling me what it is?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #38
        0x17,
        (
            "#1464F#11PYeah, there is...\x02\x03",

            "#1465FWell, I suppose it couldn't hurt to tell you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1993():
        OP_8E(0xFE, 0xFFFF5E0C, 0x61A8, 0xE678, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1993)
    Sleep(1000)
    Fade(1000)
    OP_6D(-41900, 25000, 60320, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(306000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x17, 0x1)
    Sleep(300)

    ChrTalk(    #39
        0x17,
        (
            "#1462F#11PYou're familiar with Renne from Ouroboros,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x106,
        (
            "#052F#6PY-Yeah...\x02\x03",

            "#551FThe crazy-strong little girl with the huge robot.\x01",
            "Couldn't forget her if I tried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x17,
        (
            "#1464F#11PTita told us that she's friends with that girl.\x02\x03",

            "#1462FWhich sounds insane, I know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x106,
        (
            "#552F#6P...Nah, it's not.\x02\x03",

            "She doesn't talk about it, but I know she is.\x02\x03",

            "#053FFeels like she's going to unnatural lengths to\x01",
            "avoid the issue even coming up, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x17,
        (
            "#1464F#11PThat makes explaining this a little simpler.\x02\x03",

            "#1462FThe Orbal Gear Project was begun with the aim of \x01",
            "developing a new kind of weapon that could compete\x01",
            "with the society's advanced military technology.\x02\x03",

            "Eventually, we hope to end up with something that \x01",
            "can even go head to head with Pater-Mater.\x02\x03",

            "#1464FAs soon as she heard about what we were planning\x01",
            "to do, Tita told us that she wanted to be part it--\x01",
            "of her own volition.\x02\x03",

            "At first, Erika and I were strongly opposed to the idea.\x02\x03",

            "It was Tita who insisted she wanted to do whatever\x01",
            "she could to keep the connection she had with Renne.\x01",
            "She wouldn't take no for an answer.\x02\x03",

            "#1465FShe insisted this was something she could do for her.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #44
        0x17,
        (
            "#1465F#11PFrom my perspective, her intention isn't actually\x01",
            "to talk Renne down or anything along those lines...\x02\x03",

            "She just thinks that by participating in the Orbal\x01",
            "Gear's development, she'll be able to keep thinking\x01",
            "about her.\x02\x03",

            "The project connects them in a tiny way even if\x01",
            "they can't meet, and even if Tita can't do anything\x01",
            "more substantial for her.\x02\x03",

            "#1464FIt really is a tiny connection...\x02\x03",

            "...and yet that's probably the best she can do for \x01",
            "Renne right now, and she's determined to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        (
            "#552F#6P#40W...\x02\x03",

            "...She...\x01",
            "I had no idea...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 19)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #46
        0x106,
        (
            "#551F#6P(She's such an idiot...)\x02\x03",

            "#556F(How am I supposed to know you're\x01",
            "shouldering somethin' that heavy if\x01",
            "you don't tell me?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x17,
        (
            "#1464F#11PShe's working on the project formally as an\x01",
            "engineer, no different to Erika or me.\x02\x03",

            "My wife was the one who gave her permission.\x02\x03",

            "#1460FAfter she showed as much resolve as she did,\x01",
            "it wouldn't have been fair of us to treat her like\x01",
            "a child.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x106, 270, 400)
    Sleep(300)

    ChrTalk(    #48
        0x106,
        (
            "#053F#12PYou mind if I ask somethin'?\x02\x03",

            "#051FWhere is that Orbal Gear thing now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x17,
        "#1465F#11PDoes that mean you're up for the job?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        (
            "#551F#12PWell, I can't walk the hell away.\x02\x03",

            "#556FShe might go doing something crazy again\x01",
            "if I leave her alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#1465F#11PI see.\x02\x03",

            "#1461FHaha. Albert was right about you, Agate.\x02\x03",

            "You do seem to have some promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #52
        0x106,
        (
            "#055F#12PWh-What're you talkin' about?\x02\x03",

            "What'd Gramps say?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x17, 90, 500)
    Sleep(500)

    ChrTalk(    #53
        0x17,
        "#1460F#5PYou'll need this, incidentally.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #54
        "\x07\x05Agate received an identification card from Dan.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #55
        0x17,
        (
            "#1464F#5PUsing this in the elevator will let you get to\x01",
            "B5F of the building where the tests will take\x01",
            "place.\x02\x03",

            "Tita and Erika should be there.\x02\x03",

            "#1465FYou're going to want to make sure you're\x01",
            "ready if you do go, though.\x02\x03",

            "Erika's been dead set on testing you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        (
            "#053F#12PI couldn't care less what she wants.\x02\x03",

            "#051FI'm just gonna go help Tita with the tests.\x01",
            "What anyone else does is none of my business.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26A6():
        OP_6D(-43630, 25000, 60640, 2500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_26A6)

    def lambda_26BE():
        OP_8E(0xFE, 0xFFFF54C0, 0x61A8, 0xE95C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_26BE)
    WaitChrThread(0x106, 0x1)
    OP_62(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x106, 0x17, 400)
    Sleep(300)

    ChrTalk(    #57
        0x106,
        (
            "#052F#5PWhat about you, Dan?\x02\x03",

            "You ain't coming?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x17,
        (
            "#1464F#6PDon't mind me. I'll be there.\x02\x03",

            "#1465FAnd just so we're clear, I haven't decided to\x01",
            "accept you myself yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x106,
        "#551F#5P(...Accept me as what?)\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x106, 270, 400)
    Sleep(300)
    FadeToDark(2000, 0, -1)

    def lambda_2806():
        OP_6D(-47630, 25000, 60640, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2806)

    def lambda_281E():
        OP_8E(0xFE, 0xFFFF44E4, 0x6270, 0xE95C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_281E)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_927 end

    def Function_8_2847(): pass

    label("Function_8_2847")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-27760, 8000, 59500, 0)
    OP_67(0, 9200, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(298000, 0)
    OP_6E(862, 0)
    SetChrPos(0x107, 9040, -40, 56920, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SoundLoad(121)
    SoundLoad(124)
    SoundLoad(143)
    SoundLoad(276)
    SoundLoad(524)
    SoundLoad(275)
    SoundLoad(200)
    SoundLoad(209)
    SoundLoad(26)
    OP_AD(0x2400CD, 0x0, 0x0, 0x3E8)
    OP_22(0x79, 0x0, 0x64)

    def lambda_28ED():
        OP_6B(3620, 5000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_28ED)
    FadeToBright(2000, 0)
    OP_0D()
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #60
        "\x07\x05Approaching location...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #61
        "\x07\x05320... 310... 300...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x7C, 0x0, 0x64)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x20, 0xFF)
    OP_6D(-2500, 4260, 56860, 0)
    OP_67(0, 11640, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(302000, 0)
    OP_6E(352, 0)
    SetChrPos(0x107, 1620, 3500, 56700, 270)
    Sleep(300)
    FadeToBright(0, 0)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(40, 80, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #62
        "\x07\x05Target in sight...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 300, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #63
        "\x07\x05Commencing operation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice")

    AnonymousTalk(    #64
        (
            "\x07\x05Coordinate adjustment complete.\x01",
            "Activating boosters.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x114, 0x0, 0x46)
    Sleep(1000)

    def lambda_2A86():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2A86)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_AE(0x3E8)
    OP_23(0x79)
    Sleep(1500)
    OP_44(0x20, 0xFF)
    OP_6D(-22600, 8000, 59500, 0)
    OP_67(0, 5440, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(295000, 0)
    OP_6E(282, 0)

    def lambda_2AEF():
        OP_6D(-26600, 8000, 59500, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2AEF)

    def lambda_2B07():
        OP_6C(315000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2B07)
    SetChrPos(0x107, -14640, 8000, 59000, 270)

    def lambda_2B28():
        OP_8E(0xFE, 0xFFFF99F8, 0x1F40, 0xE678, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2B28)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x113, 0x1, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    OP_20(0xBB8)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x107,
        (
            "#064F#0C...Huh?\x02\x03",

            "What's that sound?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BE0():
        OP_8C(0xFE, 135, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2BE0)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x107, 0x2)
    OP_1D(0x56)

    def lambda_2C03():
        OP_6D(-26000, 9000, 58940, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2C03)

    def lambda_2C1B():
        OP_67(0, 24980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2C1B)

    def lambda_2C33():
        OP_6B(1700, 2000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_2C33)

    def lambda_2C43():
        OP_6E(490, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2C43)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x20, 0x0)
    Sleep(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_6D(-23000, 8500, 54280, 0)
    OP_67(0, 6480, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(180000, 0)
    OP_6E(278, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x20)
    ClearChrFlags(0x16, 0x1)
    SetChrFlags(0x16, 0x2)
    SetChrChipByIndex(0x16, 14)
    SetChrSubChip(0x16, 5)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 15)
    SetChrSubChip(0x17, 5)
    SetChrPos(0x107, -23000, 8000, 57300, 180)
    SetChrPos(0x16, -23880, 14120, 54340, 0)
    SetChrPos(0x17, -21300, 14200, 53800, 0)
    OP_A1(0x1C, 0x9)
    OP_72(0x409, 0x0)
    ExitThread()
    OP_72(0x9, 0x0)
    ExitThread()
    SetChrPos(0x1C, -23840, 14000, 54700, 0)
    OP_A1(0x1D, 0xA)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_72(0xA, 0x0)
    ExitThread()
    SetChrPos(0x1D, -21340, 14000, 54100, 0)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    LoadEffect(0x1, "map\\\\mp065_01.eff")

    def lambda_2DA2():
        OP_6D(-23780, 8000, 54440, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_2DA2)

    def lambda_2DBA():
        OP_6C(225000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2DBA)
    PlayEffect(0x1, 0x2, 0x1C, 0, -200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x1D, 0, -200, -200, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)

    def lambda_2E3D():
        OP_8F(0xFE, 0xFFFFA2B8, 0x1FB7, 0xD444, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2E3D)

    def lambda_2E58():
        OP_8F(0xFE, 0xFFFFA2E0, 0x1F40, 0xD5AC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2E58)
    Sleep(500)

    def lambda_2E78():
        OP_8F(0xFE, 0xFFFFACCC, 0x2008, 0xD228, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2E78)

    def lambda_2E93():
        OP_8F(0xFE, 0xFFFFACA4, 0x1F40, 0xD354, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2E93)
    OP_43(0x107, 0x3, 0x0, 0xE)
    Sleep(500)
    PlayEffect(0x0, 0x0, 0xFF, -23840, 8000, 54700, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x0, 0x1, 0xFF, -21340, 8000, 54100, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2F40():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE290, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F40)
    WaitChrThread(0x107, 0x1)
    OP_43(0x107, 0x2, 0x0, 0xF)
    WaitChrThread(0x16, 0x1)
    OP_82(0x0, 0x2)
    OP_22(0xC8, 0x0, 0x46)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_A1(0x1E, 0xB)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0xB, 0x0)
    ExitThread()
    SetChrPos(0x1E, -23840, 8100, 54700, 0)
    WaitChrThread(0x17, 0x1)
    OP_82(0x1, 0x2)
    OP_22(0xC8, 0x0, 0x46)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_A1(0x1F, 0xC)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_72(0xC, 0x0)
    ExitThread()
    SetChrPos(0x1F, -21340, 8100, 54100, 0)
    OP_23(0x113)
    OP_23(0xCC)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(500)
    OP_22(0x1A, 0x0, 0x64)
    ClearChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x1)
    ClearChrFlags(0x16, 0x2)
    SetChrPos(0x16, -22920, 8000, 54840, 0)
    SetChrChipByIndex(0x16, 12)
    SetChrSubChip(0x16, 0)
    Sleep(600)
    Sleep(500)

    ChrTalk(    #66
        0x107,
        (
            "#065F#0C#3SWhaaat?! #2S\x02\x03",

            "Umm... Erm...\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_22(0x1A, 0x0, 0x64)
    ClearChrFlags(0x17, 0x20)
    SetChrFlags(0x17, 0x1)
    ClearChrFlags(0x17, 0x2)
    SetChrPos(0x17, -22560, 8000, 54020, 0)
    SetChrChipByIndex(0x17, 13)
    SetChrSubChip(0x17, 0)
    Sleep(800)

    NpcTalk(    #67
        0x16,
        "Mysterious Mechanic",
        "#5C#5PFrnnn...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #68
        0x17,
        "Mysterious Mechanic",
        "#5C#5PFrnnn...\x02",
    )

    CloseMessageWindow()

    def lambda_3105():
        OP_8E(0xFE, 0xFFFFA678, 0x1F40, 0xD96C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3105)
    Sleep(200)

    def lambda_3125():
        OP_8E(0xFE, 0xFFFFA970, 0x1F40, 0xD868, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3125)
    Sleep(1000)

    def lambda_3145():
        OP_6D(-23780, 8000, 54840, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_3145)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_316F():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE420, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_316F)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)

    ChrTalk(    #69
        0x107,
        (
            "#065F#0C#12PUmm...\x02\x03",

            "#062FD-Do I know you?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    def lambda_31CE():
        OP_8E(0xFE, 0xFFFFA628, 0x1F40, 0xDCF0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_31CE)
    Sleep(200)

    def lambda_31EE():
        OP_8E(0xFE, 0xFFFFA9AC, 0x1F40, 0xDB60, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_31EE)
    Sleep(800)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)

    NpcTalk(    #70
        0x16,
        "Mysterious Mechanic",
        "#5C#5PFrrrnnn...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #71
        0x107,
        "#065F#0C#12PUh-oh...\x02",
    )

    CloseMessageWindow()

    def lambda_326E():
        OP_6D(-23780, 8000, 55240, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_326E)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3298():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE5B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3298)
    WaitChrThread(0x107, 0x1)

    def lambda_32B8():
        OP_6D(-23780, 8000, 55640, 500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_32B8)

    def lambda_32D0():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE740, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_32D0)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    WaitChrThread(0x107, 0x1)
    Sleep(1000)
    OP_20(0x7D0)
    Sleep(500)

    NpcTalk(    #72
        0x17,
        "Mysterious Mechanic",
        (
            "#5C#5PHahaha.\x02\x03",

            "#5CWe've really missed you, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x107,
        "#064F#0C#12PHuh?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #74
        0x16,
        "Mysterious Mechanic",
        "#5C#5P...Oh, my.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #75
        0x16,
        "Mysterious Mechanic",
        (
            "#5C#5PDon't tell me you forgot the sound\x01",
            "of our voices while we were away?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 16)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 17)
    SetChrSubChip(0x17, 0)
    OP_6B(2700, 0)
    OP_67(0, 5580, -10000, 0)
    OP_0D()
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #76
        0x107,
        (
            "#064F#0C#12POh!\x02\x03",

            "#061F#3SMom! Dad! #2S\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xD)
    Sleep(1000)

    ChrTalk(    #77
        0x16,
        "#1976F#5PHeehee. That's our girl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x17,
        (
            "#1625F#5PSorry for surprising you. We just wanted\x01",
            "to have a little fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        (
            "#562F#12PI was scared stiff!\x02\x03",

            "Just flying in all of a sudden like that and\x01",
            "walking up to me without saying a word...\x02\x03",

            "Plus you had those goggles on, so I couldn't\x01",
            "tell WHO you were!\x02\x03",

            "#560FYou could've told me you were planning on\x01",
            "coming back!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x16,
        "#1972F#5P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x107,
        (
            "#064F#12P...Mom?\x02\x03",

            "Are you okay? Why're you so quiet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x16,
        "#1972F#5PTita...\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x16)
    Sleep(500)
    SetChrFlags(0x16, 0x40)

    def lambda_3699():
        OP_8E(0xFE, 0xFFFFA628, 0x1F40, 0xE5B0, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3699)

    def lambda_36B4():
        OP_6D(-24020, 8000, 58480, 3000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_36B4)

    def lambda_36CC():
        OP_67(0, 5580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_36CC)

    def lambda_36E4():
        OP_6C(235000, 3000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_36E4)

    def lambda_36F4():
        OP_6B(2640, 3000)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_36F4)
    WaitChrThread(0x16, 0x1)
    Fade(100)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 18)
    SetChrSubChip(0x107, 0)
    OP_0D()
    OP_43(0x107, 0x3, 0x0, 0x10)
    Sleep(300)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(1000)

    ChrTalk(    #83
        0x16,
        (
            "#1981F#5PWHY are you so cute?!\x02\x03",

            "Oh, Aidios! Thank you for gracing our unworthy\x01",
            "world with this miracle of a child!\x02\x03",

            "I'm never going to let you go agaaain!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37EA():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_37EA)
    Sleep(1000)

    ChrTalk(    #84
        0x107,
        "#562F#12PM-Mom...you're starting to hurt me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x16,
        (
            "#1981F#5PAhhh... Giving birth to this bundle of sugar\x01",
            "was the best thing we ever did.\x02\x03",

            "How did I manage all this time without her?\x01",
            "I'm so happy to finally be back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x17,
        (
            "#1621F#5PI can tell.\x02\x03",

            "#1620FI'd kind of like the chance to greet her,\x01",
            "too, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x16,
        (
            "#1974F#5PO-Oh. Sure. Knock yourself out.\x02\x03",

            "#1976FI suppose you do have the right and all.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_59()
    OP_44(0x107, 0xFF)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x16, 0x8)
    SetChrPos(0x16, -23000, 8000, 58600, 0)
    ClearChrFlags(0x107, 0x2)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    Sleep(800)

    def lambda_39DA():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE2F4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_39DA)
    WaitChrThread(0x16, 0x1)

    def lambda_39FA():

        label("loc_39FA")

        TurnDirection(0xFE, 0x107, 500)
        OP_48()
        Jump("loc_39FA")

    QueueWorkItem2(0x16, 2, lambda_39FA)

    def lambda_3A0B():
        OP_8F(0xFE, 0xFFFFA178, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3A0B)

    def lambda_3A26():
        OP_6D(-24860, 8000, 56540, 1500)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_3A26)

    def lambda_3A3E():
        OP_67(0, 5580, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A3E)

    def lambda_3A56():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_3A56)

    def lambda_3A66():
        OP_6B(2740, 1500)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_3A66)

    def lambda_3A76():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xE150, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A76)
    WaitChrThread(0x17, 0x1)
    OP_44(0x16, 0x2)
    Sleep(300)

    ChrTalk(    #88
        0x17,
        (
            "#1625F#5PHey, Tita.\x02\x03",

            "#1621FLooks like you've grown a bit while\x01",
            "we were away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x107,
        (
            "#560F#12PI sure have!\x02\x03",

            "#061FI've missed you both so much.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #90
        0x16,
        (
            "#1981F#5PAhhh... Everything you do just melts my heart...\x02\x03",

            "Let me hug you again! C'mere! ㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BAD():
        OP_8E(0xFE, 0xFFFFA308, 0x1F40, 0xE420, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3BAD)
    WaitChrThread(0x16, 0x1)
    TurnDirection(0x107, 0x16, 500)
    Sleep(300)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #91
        0x107,
        "#562F#6PM-Mom, please...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 400)
    Sleep(300)

    ChrTalk(    #92
        0x17,
        (
            "#1625F#5PErika, I think that should probably wait until\x01",
            "you've changed.\x02\x03",

            "That maintenance uniform is full of sensors,\x01",
            "as you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x16,
        (
            "#1974F#5PO-Oh, yeah. Slipped my mind.\x02\x03",

            "#1977FIn that case...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CDF():
        OP_8F(0xFE, 0xFFFFA178, 0x1F40, 0xE290, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3CDF)
    WaitChrThread(0x16, 0x1)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 12)
    SetChrSubChip(0x16, 0)
    OP_0D()
    OP_8C(0x16, 100, 400)
    Sleep(300)

    ChrTalk(    #94
        0x16,
        (
            "#1977F#11P...shall we take care of...business first,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_3D7C():

        label("loc_3D7C")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_3D7C")

    QueueWorkItem2(0x107, 2, lambda_3D7C)

    def lambda_3D8D():

        label("loc_3D8D")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_3D8D")

    QueueWorkItem2(0x17, 2, lambda_3D8D)

    def lambda_3D9E():
        OP_8E(0xFE, 0xFFFFAF24, 0x1F40, 0xE290, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3D9E)

    def lambda_3DB9():
        OP_8F(0xFE, 0xFFFFA628, 0x1F40, 0xDF0C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3DB9)
    WaitChrThread(0x16, 0x1)
    OP_44(0x107, 0x2)

    def lambda_3DDD():
        OP_8C(0xFE, 90, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3DDD)
    OP_44(0x17, 0x2)

    ChrTalk(    #95
        0x16,
        (
            "#1978F#5PWhere IS the red-haired...man I've heard\x01",
            "so much about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x107,
        (
            "#064F#11PUmm?\x02\x03",

            "Are you talking about Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        (
            "#1971F#5PThat's the one.\x02\x03",

            "I was so hoping I'd be able to meet him.\x02\x03",

            "#1985FNow, where is he? \x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(1500)

    ChrTalk(    #98
        0x107,
        (
            "#560F#11PHe's actually in Bose at the moment.\x02\x03",

            "Mom? You're acting kinda weird all of\x01",
            "a sudden...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x16,
        (
            "#1977F#5PBah. Talk about lousy timing.\x02\x03",

            "#1982FNot that I'd be happy if he WERE here given that\x01",
            "would indicate him being in close proximity to my\x01",
            "angel. AGAIN.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x17,
        (
            "#1624F#11PWell, it's okay.\x02\x03",

            "#1620FWe can always go meet him over in Bose\x01",
            "next month if it comes to it.\x02\x03",

            "I'd like to meet him, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x16,
        "#1977F#5PTrue enough.\x02",
    )

    CloseMessageWindow()
    Sleep(1200)
    OP_44(0x16, 0xFF)
    OP_8C(0x16, 100, 500)
    Fade(300)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x16, 16)
    SetChrSubChip(0x16, 0)
    Sleep(800)

    ChrTalk(    #102
        0x16,
        (
            "#1977F#5PWord has it that a lot has been happening\x01",
            "here in our absence...\x02\x03",

            "I'll bet we have a LOT to thank him for.\x02\x03",

            "#1985FHeheheh... We'll have to go and give him\x01",
            "a thank you that he'll neeever forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x107,
        (
            "#061F#11PI'll have to go with you and introduce you\x01",
            "to him, then!\x02\x03",

            "His house is real nice, too! It's pretty small,\x01",
            "but it's all warm and cozy.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_4241():
        OP_8C(0xFE, 290, 500)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_4241)

    def lambda_424F():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_424F)
    WaitChrThread(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #104
        0x17,
        "#1623F#5P...You've been to his house?\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x16)
    OP_63(0x17)
    Sleep(500)

    ChrTalk(    #105
        0x16,
        "#1980F#6PGaaaaaah!\x02",
    )

    OP_7C(0x0, 0x190, 0xFA0, 0x12C)
    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)
    Sleep(300)

    ChrTalk(    #106
        0x17,
        "#1621F#11PHahaha. Now, now. Calm down, Erika.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x107, 400)
    Sleep(300)

    ChrTalk(    #107
        0x17,
        (
            "#1625F#5PTita, try not to provoke your mother too\x01",
            "much, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        "#064F#11PWas I...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x16, 100, 500)

    def lambda_43A1():
        OP_8E(0xFE, 0xFFFFB6F4, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_43A1)
    WaitChrThread(0x16, 0x1)

    ChrTalk(    #109
        0x16,
        (
            "#1980F#11PAgaaate! AGAAAAAATE!\x02\x03",

            "You are going to pay DEARLY for corrupting\x01",
            "my darling daughter!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4426():
        OP_8E(0xFE, 0xFFFFC2AC, 0x1F40, 0xE290, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4426)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x107, 190, 500)
    Sleep(600)
    OP_8C(0x107, 100, 500)
    Sleep(600)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(700)
    OP_22(0x6D, 0x0, 0x64)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -35780, 10000, 58300, 270)

    def lambda_44A0():
        OP_8E(0xFE, 0xFFFF9174, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_44A0)
    WaitChrThread(0x18, 0x1)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #110
        0x18,
        "#103F#11PAre my eyes playing tricks on me?\x02",
    )

    CloseMessageWindow()

    def lambda_450C():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_450C)
    Sleep(100)

    def lambda_451F():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_451F)
    WaitChrThread(0x17, 0x2)
    Sleep(300)

    ChrTalk(    #111
        0x107,
        "#560F#6PUmm... Grandpa...\x02",
    )

    CloseMessageWindow()

    def lambda_4556():
        OP_6D(-25380, 8000, 57540, 2000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_4556)

    def lambda_456E():
        OP_6C(240000, 2000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_456E)

    def lambda_457E():
        OP_8E(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_457E)
    Sleep(1500)

    def lambda_459E():
        OP_8F(0xFE, 0xFFFFA498, 0x1F40, 0xE164, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_459E)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #112
        0x17,
        (
            "#1624F#6PAlways a pleasure, Albert.\x02\x03",

            "#1625FSorry for not giving you a heads up\x01",
            "on our return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x18,
        (
            "#101F#11POh, nonsense! Don't you worry about that.\x02\x03",

            "#102FWhat are those things, if I might ask?\x02\x03",

            "They look like a vehicle with boosters\x01",
            "attached, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x16, -13600, 8000, 56240, 270)

    NpcTalk(    #114
        0x16,
        "Female Voice",
        (
            "#2PThey're called landing crafts, and they\x01",
            "were developed by yours truly.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4752():

        label("loc_4752")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_4752")

    QueueWorkItem2(0x107, 2, lambda_4752)
    Sleep(100)

    def lambda_4768():

        label("loc_4768")

        TurnDirection(0xFE, 0x16, 500)
        OP_48()
        Jump("loc_4768")

    QueueWorkItem2(0x17, 2, lambda_4768)
    Sleep(300)
    SetChrPos(0x16, -13600, 8000, 58300, 270)

    def lambda_478F():
        OP_6D(-25980, 8000, 57400, 6000)
        ExitThread()

    QueueWorkItem(0x20, 0, lambda_478F)

    def lambda_47A7():
        OP_67(0, 4880, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_47A7)

    def lambda_47BF():
        OP_6B(2700, 6000)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_47BF)

    def lambda_47CF():
        OP_8E(0xFE, 0xFFFFAA10, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_47CF)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Sleep(1000)

    def lambda_47FA():
        OP_8F(0xFE, 0xFFFFA308, 0x1F40, 0xE9FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_47FA)

    def lambda_4815():
        OP_8F(0xFE, 0xFFFFA308, 0x1F40, 0xDE94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4815)
    WaitChrThread(0x16, 0x1)
    OP_8C(0x16, 150, 400)
    Sleep(300)

    ChrTalk(    #115
        0x16,
        (
            "#1978F#6PMost of the places we go to don't have\x01",
            "the space to land an airship or any kind\x01",
            "of landing port.\x02\x03",

            "And there's not much point in an airship\x01",
            "if you can't land it, is there?\x02\x03",

            "Which is where these two beauties come in.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x16, 285, 400)

    def lambda_492D():
        OP_8E(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_492D)
    WaitChrThread(0x16, 0x1)
    OP_44(0x107, 0x2)
    OP_44(0x17, 0x2)
    OP_8C(0x107, 195, 500)
    Sleep(300)

    ChrTalk(    #116
        0x16,
        (
            "#1976F#6PHeh. Anyway, long time no see, Albert.\x02\x03",

            "It's a small comfort knowing you haven't\x01",
            "kicked the bucket yet.\x02\x03",

            "I mean, how could I have been able to gloat\x01",
            "if you were already six arge under?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x18,
        (
            "#102F#11PHmph. You really think a pathetic contraption\x01",
            "like that is good enough to beat me?\x02\x03",

            "You must have forgotten who I am when you\x01",
            "were out and about.\x02\x03",

            "#104FOne close look and the cracks start to show--\x01",
            "just look at them! I doubt they even manage\x01",
            "five minutes.\x02\x03",

            "#101FA fat load of good they'll be for anything other\x01",
            "than trying to show off to me. They won't be\x01",
            "getting any real-world use any time soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x16,
        (
            "#1971F#6PHeh! Oh, how wrong you are.\x02\x03",

            "I'll have you know that we came all the way\x01",
            "from the border with Calvard on these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x18,
        "#102F#11PFrom CALVARD?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x16,
        (
            "#1978F#6POh, did that catch your attention? I'll give you\x01",
            "that the crafts' flight time is somewhat limited.\x02\x03",

            "#1976FBut that's an issue where I can find an easy\x01",
            "workaround!\x02\x03",

            "By firing them from an orbal catapult attached\x01",
            "to an airship, they can fly a distance of roughly\x01",
            "120 selge!\x02\x03",

            "#1984FAfter modifying the orbal circuits, we were able\x01",
            "to record an operation time of 382.2 seconds,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x18,
        "#103F#11P120 selge? 382.2 seconds?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x16,
        (
            "#1971F#6PHAHAHA! Surprised? That stupid look on your\x01",
            "face says it all!\x02\x03",

            "Not to worry. I'll give you as much time as you\x01",
            "need for that shriveled old brain of yours to\x01",
            "comprehend my brilliance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x18,
        (
            "#102F#11PBrilliance?! Pah! Don't make me laugh!\x02\x03",

            "You're talking to the man who developed the \x01",
            "Capel! These are child's play by comparison!\x02\x03",

            "#101FI don't even need to ask how you made them.\x01",
            "I could probably develop a better version in\x01",
            "my sleep!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x16,
        "#1980F#6PSay that again, you stubborn old fart!\x02",
    )

    CloseMessageWindow()

    def lambda_503C():
        OP_8E(0xFE, 0xFFFFA2A4, 0x1F40, 0xE3BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_503C)

    def lambda_5057():
        OP_8E(0xFE, 0xFFFF9F84, 0x1F40, 0xE3BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5057)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x17, 0x1)
    OP_43(0x18, 0x3, 0x0, 0xA)
    Sleep(300)

    ChrTalk(    #125
        0x16,
        "#1980F#3PGrrrrrr!\x02",
    )


    ChrTalk(    #126
        0x18,
        "#102F#2PGrrrrrr!\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #127
        0x107,
        "#562F#12P*sigh* Here they go again...\x02",
    )

    CloseMessageWindow()

    def lambda_50FD():
        OP_8E(0xFE, 0xFFFFA1DC, 0x1F40, 0xE7CC, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_50FD)
    WaitChrThread(0x107, 0x1)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 190, 500)
    Sleep(500)

    ChrTalk(    #128
        0x107,
        "#62F#12PWill you two please stop fighting?! Please!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #129
        0x16,
        (
            "#1979F#6POh, and I read those files you sent me!\x02\x03",

            "You've got some nerve showing your face to me \x01",
            "after exposing MY daughter to so much danger!\x02\x03",

            "#1980FTo say nothing of letting that vermin like that\x01",
            "'A'-word near her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x18,
        (
            "#102F#11POh, get over yourself!\x02\x03",

            "I'm getting lectured on looking after people\x01",
            "from the mother who ditched her daughter\x01",
            "to wander the continent, am I?\x02\x03",

            "#105FHow about you look in a mirror before you\x01",
            "go criticizing others, huh?!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x18, 0xFF)
    OP_44(0x16, 0xFF)
    OP_A3(0x0)
    OP_43(0x18, 0x3, 0x0, 0xB)
    Sleep(3000)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #131
        0x107,
        "#065F#12PD-Dad, can't you stop them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        (
            "#1621F#5PHaha. It'll be fine. Let them have their fun.\x02\x03",

            "They're secretly happy to see one another\x01",
            "again, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        (
            "#63F#12PBut we're taking up a lot of space in the middle\x01",
            "of the town here. How are people going to get\x01",
            "past us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        (
            "#1625F#5P...Yeah, that's a good point. We can't leave\x01",
            "these two landing crafts out here forever.\x02\x03",

            "I guess we're just going to have to drag our\x01",
            "quarreling father and daughter back home.\x02\x03",

            "#1621FMind giving me a hand, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        "#067F#12PSure thing!\x02",
    )

    CloseMessageWindow()
    OP_43(0x107, 0x3, 0x0, 0xC)
    OP_43(0x17, 0x3, 0x0, 0xD)
    WaitChrThread(0x107, 0x3)
    WaitChrThread(0x17, 0x3)
    OP_A2(0x0)
    WaitChrThread(0x18, 0x3)
    OP_43(0x18, 0x3, 0x0, 0xA)
    Sleep(1000)
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x16, 0x20)

    def lambda_55B6():

        label("loc_55B6")

        TurnDirection(0xFE, 0x16, 800)
        OP_48()
        Jump("loc_55B6")

    QueueWorkItem2(0x17, 2, lambda_55B6)

    def lambda_55C7():
        OP_8F(0xFE, 0xFFFFA754, 0x1F40, 0xE678, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_55C7)
    WaitChrThread(0x16, 0x1)

    def lambda_55E7():
        OP_8F(0xFE, 0xFFFFAA10, 0x1F40, 0xE3BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_55E7)
    WaitChrThread(0x16, 0x1)
    OP_44(0x17, 0x2)
    Sleep(1000)

    def lambda_5610():
        OP_8F(0xFE, 0xFFFFD0BC, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5610)

    def lambda_562B():
        OP_8F(0xFE, 0xFFFFCEB4, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_562B)
    Sleep(600)

    def lambda_564B():
        OP_8F(0xFE, 0xFFFFD0BC, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_564B)

    def lambda_5666():
        OP_8F(0xFE, 0xFFFFCEB4, 0x1F40, 0xE3BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5666)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3133   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2847 end

    def Function_9_569D(): pass

    label("Function_9_569D")

    Sleep(600)

    label("loc_56A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56D2")
    OP_8C(0x16, 145, 500)
    Sleep(600)
    OP_8C(0x16, 45, 500)
    Sleep(600)
    OP_8C(0x16, 100, 500)
    Sleep(800)
    Jump("loc_56A2")

    label("loc_56D2")

    Return()

    # Function_9_569D end

    def Function_10_56D3(): pass

    label("Function_10_56D3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5718")

    def lambda_56E2():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_56E2)

    def lambda_56FC():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_56FC)
    Sleep(2000)
    Jump("Function_10_56D3")

    label("loc_5718")

    Return()

    # Function_10_56D3 end

    def Function_11_5719(): pass

    label("Function_11_5719")


    def lambda_571F():
        OP_8F(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_571F)

    def lambda_573A():
        OP_8F(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_573A)
    WaitChrThread(0x16, 0x1)
    WaitChrThread(0x18, 0x1)

    label("loc_5759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5837")

    def lambda_5768():
        OP_8F(0xFE, 0xFFFF9FE8, 0x1F40, 0xE3BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5768)
    WaitChrThread(0x16, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_578D():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_578D)

    def lambda_57A7():
        OP_8F(0xFE, 0xFFFFA4FC, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_57A7)
    WaitChrThread(0x16, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_57CB")
    Jump("loc_5837")

    label("loc_57CB")


    def lambda_57D1():
        OP_8F(0xFE, 0xFFFFA240, 0x1F40, 0xE3BC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_57D1)
    WaitChrThread(0x18, 0x1)
    OP_22(0xD1, 0x0, 0x64)

    def lambda_57F6():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_57F6)

    def lambda_5810():
        OP_8F(0xFE, 0xFFFF9D2C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5810)
    WaitChrThread(0x18, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5834")
    Jump("loc_5837")

    label("loc_5834")

    Jump("loc_5759")

    label("loc_5837")

    Return()

    # Function_11_5719 end

    def Function_12_5838(): pass

    label("Function_12_5838")


    def lambda_583E():
        OP_8E(0xFE, 0xFFFF9A0C, 0x1F40, 0xE7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_583E)
    WaitChrThread(0x107, 0x1)

    def lambda_585E():
        OP_8E(0xFE, 0xFFFF9A0C, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_585E)
    WaitChrThread(0x107, 0x1)
    TurnDirection(0x107, 0x18, 500)
    Return()

    # Function_12_5838 end

    def Function_13_5880(): pass

    label("Function_13_5880")


    def lambda_5886():
        OP_8E(0xFE, 0xFFFFA754, 0x1F40, 0xDE94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5886)
    WaitChrThread(0x17, 0x1)

    def lambda_58A6():
        OP_8E(0xFE, 0xFFFFA754, 0x1F40, 0xE3BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_58A6)
    WaitChrThread(0x17, 0x1)
    TurnDirection(0x17, 0x16, 500)
    Return()

    # Function_13_5880 end

    def Function_14_58C8(): pass

    label("Function_14_58C8")

    OP_22(0xCC, 0x1, 0x28)
    Sleep(200)
    OP_24(0xCC, 0x32)
    Sleep(200)
    OP_24(0xCC, 0x3C)
    Sleep(200)
    OP_24(0xCC, 0x46)
    Sleep(200)
    OP_24(0xCC, 0x50)
    Sleep(200)
    OP_24(0xCC, 0x5A)
    Sleep(200)
    OP_24(0xCC, 0x64)
    Return()

    # Function_14_58C8 end

    def Function_15_5904(): pass

    label("Function_15_5904")

    Sleep(1500)
    OP_82(0x2, 0x2)
    Sleep(500)
    OP_82(0x3, 0x2)
    Return()

    # Function_15_5904 end

    def Function_16_5915(): pass

    label("Function_16_5915")


    def lambda_591B():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_591B)
    WaitChrThread(0xFE, 0x2)
    Sleep(400)

    label("loc_592F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5950")

    def lambda_593E():
        OP_99(0xFE, 0x4, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_593E)
    WaitChrThread(0xFE, 0x2)
    Jump("loc_592F")

    label("loc_5950")

    Return()

    # Function_16_5915 end

    SaveToFile()

Try(main)
