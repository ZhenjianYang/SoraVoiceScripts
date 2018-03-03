from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P7013   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P7013.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60174",
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
        'Rufina',                               # 9
        'Dummy Kevin',                          # 10
        'Dummy Ries',                           # 11
        'Veil',                                 # 12
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
        'ED6_DT07/CH02770 ._CH',             # 00
        'ED6_DT07/CH02930 ._CH',             # 01
        'ED6_DT07/CH02940 ._CH',             # 02
        'ED6_DT07/CH02940 ._CH',             # 03
        'ED6_DT26/CH20716 ._CH',             # 04
        'ED6_DT27/CH03151 ._CH',             # 05
        'ED6_DT27/CH04154 ._CH',             # 06
        'ED6_DT27/CH04158 ._CH',             # 07
        'ED6_DT27/CH04150 ._CH',             # 08
        'ED6_DT27/CH04151 ._CH',             # 09
        'ED6_DT27/CH03081 ._CH',             # 0A
        'ED6_DT26/CH20728 ._CH',             # 0B
        'ED6_DT26/CH20724 ._CH',             # 0C
        'ED6_DT27/CH03085 ._CH',             # 0D
        'ED6_DT27/CH03084 ._CH',             # 0E
        'ED6_DT26/CH20720 ._CH',             # 0F
        'ED6_DT26/CH20812 ._CH',             # 10
        'ED6_DT26/CH20676 ._CH',             # 11
        'ED6_DT26/CH20727 ._CH',             # 12
        'ED6_DT26/CH20719 ._CH',             # 13
        'ED6_DT26/CH20717 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02770P._CP',             # 00
        'ED6_DT07/CH02930P._CP',             # 01
        'ED6_DT07/CH02940P._CP',             # 02
        'ED6_DT07/CH02940P._CP',             # 03
        'ED6_DT26/CH20716P._CP',             # 04
        'ED6_DT27/CH03151P._CP',             # 05
        'ED6_DT27/CH04154P._CP',             # 06
        'ED6_DT27/CH04158P._CP',             # 07
        'ED6_DT27/CH04150P._CP',             # 08
        'ED6_DT27/CH04151P._CP',             # 09
        'ED6_DT27/CH03081P._CP',             # 0A
        'ED6_DT26/CH20728P._CP',             # 0B
        'ED6_DT26/CH20724P._CP',             # 0C
        'ED6_DT27/CH03085P._CP',             # 0D
        'ED6_DT27/CH03084P._CP',             # 0E
        'ED6_DT26/CH20720P._CP',             # 0F
        'ED6_DT26/CH20812P._CP',             # 10
        'ED6_DT26/CH20676P._CP',             # 11
        'ED6_DT26/CH20727P._CP',             # 12
        'ED6_DT26/CH20719P._CP',             # 13
        'ED6_DT26/CH20717P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
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
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1D2",          # 00, 0
        "Function_1_224",          # 01, 1
        "Function_2_225",          # 02, 2
        "Function_3_4788",         # 03, 3
        "Function_4_69CD",         # 04, 4
        "Function_5_69E4",         # 05, 5
        "Function_6_69FB",         # 06, 6
        "Function_7_6A12",         # 07, 7
        "Function_8_6A29",         # 08, 8
        "Function_9_6A60",         # 09, 9
        "Function_10_6A96",        # 0A, 10
        "Function_11_6ACC",        # 0B, 11
        "Function_12_6B02",        # 0C, 12
        "Function_13_6B60",        # 0D, 13
        "Function_14_6B9D",        # 0E, 14
        "Function_15_6E42",        # 0F, 15
        "Function_16_6EAF",        # 10, 16
        "Function_17_6EFE",        # 11, 17
        "Function_18_6F31",        # 12, 18
        "Function_19_762E",        # 13, 19
        "Function_20_7642",        # 14, 20
        "Function_21_7678",        # 15, 21
        "Function_22_778C",        # 16, 22
        "Function_23_784C",        # 17, 23
        "Function_24_7934",        # 18, 24
        "Function_25_7978",        # 19, 25
        "Function_26_79B6",        # 1A, 26
        "Function_27_7A65",        # 1B, 27
        "Function_28_8019",        # 1C, 28
        "Function_29_802D",        # 1D, 29
        "Function_30_805E",        # 1E, 30
        "Function_31_80F4",        # 1F, 31
        "Function_32_815E",        # 20, 32
        "Function_33_81A2",        # 21, 33
        "Function_34_81E0",        # 22, 34
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1F1")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_223")

    label("loc_1F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_210")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 18)
    Jump("loc_223")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_223")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_223")

    Return()

    # Function_0_1D2 end

    def Function_1_224(): pass

    label("Function_1_224")

    Return()

    # Function_1_224 end

    def Function_2_225(): pass

    label("Function_2_225")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x3, "craft\\cr04150.eff")
    LoadEffect(0x4, "craft\\cr04150a.eff")
    LoadEffect(0x5, "craft\\cr04150b.eff")
    LoadEffect(0x6, "monster\\msc0641.eff")
    OP_E0(238, 0x55, 0x2)
    OP_E0(239, 0x56, 0x2)
    OP_E0(240, 0x57, 0x2)
    OP_E0(241, 0x58, 0x2)
    OP_E0(238, 0x59, 0x5)
    OP_E0(239, 0x5A, 0x5)
    OP_E0(240, 0x5B, 0x5)
    OP_E0(241, 0x5C, 0x5)
    SetChrPos(0x109, 110, 0, 1760, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_328")
    SetChrPos(0xEF, 110, 0, 370, 0)
    SetChrPos(0xF0, 800, 0, -920, 0)
    SetChrPos(0xF1, -170, 0, -1560, 0)
    Jump("loc_3AD")

    label("loc_328")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    SetChrPos(0xF0, 110, 0, 370, 0)
    SetChrPos(0xEF, 800, 0, -920, 0)
    SetChrPos(0xF1, -170, 0, -1560, 0)
    Jump("loc_3AD")

    label("loc_36C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    SetChrPos(0xF1, 110, 0, 370, 0)
    SetChrPos(0xEF, 800, 0, -920, 0)
    SetChrPos(0xF0, -170, 0, -1560, 0)

    label("loc_3AD")

    OP_6D(260, -750, 29600, 0)
    OP_67(0, 9620, -10000, 0)
    OP_6B(5130, 0)
    OP_6C(295000, 0)
    OP_6E(355, 0)

    def lambda_3F0():
        OP_6B(5600, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3F0)

    def lambda_400():
        OP_6E(390, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_400)

    def lambda_410():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_410)
    FadeToBright(2000, 0)
    Sleep(4000)

    def lambda_42E():
        OP_8F(0xFE, 0x50, 0xFFFFFD12, 0x65E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42E)
    Sleep(210)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")

    def lambda_45C():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_45C)
    Sleep(230)

    def lambda_47C():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_47C)
    Sleep(150)

    def lambda_49C():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_49C)
    Jump("loc_589")

    label("loc_4B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_520")

    def lambda_4C8():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_4C8)
    Sleep(230)

    def lambda_4E8():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4E8)
    Sleep(150)

    def lambda_508():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_508)
    Jump("loc_589")

    label("loc_520")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589")

    def lambda_534():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5E6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_534)
    Sleep(230)

    def lambda_554():
        OP_8F(0xFE, 0x3D4, 0xFFFFFC18, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_554)
    Sleep(150)

    def lambda_574():
        OP_8F(0xFE, 0xFFFFFDBC, 0xFFFFFC18, 0x580C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_574)

    label("loc_589")

    WaitChrThread(0xEE, 0x3)
    Fade(500)
    OP_6D(1500, -750, 3000, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_5D6():
        OP_6D(-890, -1000, 26300, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5D6)

    def lambda_5EE():
        OP_6B(3500, 11000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5EE)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_644")

    ChrTalk(    #0
        0x101,
        "#1020F#6PWh-Where are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_644")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_674")

    ChrTalk(    #1
        0x102,
        "#1502F#6PWhere are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A6")

    ChrTalk(    #2
        0x10B,
        "#216F#6PWh-Where are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_6A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D8")

    ChrTalk(    #3
        0x107,
        "#065F#6PWh-Where are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_6D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70B")

    ChrTalk(    #4
        0x10A,
        "#1317F#6PWh-Where are we...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_70B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_742")

    ChrTalk(    #5
        0x105,
        "#1164F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #6
        0x103,
        "#1522F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_779")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #7
        0x106,
        "#052F#6PWhat a weird place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_7AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E3")

    ChrTalk(    #8
        0x108,
        "#072F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_7E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819")

    ChrTalk(    #9
        0x10E,
        "#173F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_850")

    ChrTalk(    #10
        0x104,
        "#1543F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_850")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_886")

    ChrTalk(    #11
        0x10D,
        "#276F#6PWhat a strange place...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8B8")

    label("loc_886")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B8")

    ChrTalk(    #12
        0x10C,
        "#112F#6PWhat is this place...?\x02",
    )

    CloseMessageWindow()

    label("loc_8B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91A")

    ChrTalk(    #13
        0x110,
        (
            "#1306F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_91A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97B")

    ChrTalk(    #14
        0x10C,
        (
            "#112F#6PI had no idea there was a place like this under\x01",
            "Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_97B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DC")

    ChrTalk(    #15
        0x10D,
        (
            "#276F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_9DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3E")

    ChrTalk(    #16
        0x104,
        (
            "#1542F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_A3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9F")

    ChrTalk(    #17
        0x10E,
        (
            "#178F#6PI had no idea there was a place like this under\x01",
            "Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_A9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B00")

    ChrTalk(    #18
        0x108,
        (
            "#072F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_B00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B61")

    ChrTalk(    #19
        0x106,
        (
            "#057F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_B61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC3")

    ChrTalk(    #20
        0x103,
        (
            "#1522F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_BC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C25")

    ChrTalk(    #21
        0x105,
        (
            "#1163F#6PI had no idea there was a place like this under\x01",
            "Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C87")

    ChrTalk(    #22
        0x10A,
        (
            "#1317F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_C87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE8")

    ChrTalk(    #23
        0x107,
        (
            "#065F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D49")

    ChrTalk(    #24
        0x10B,
        (
            "#216F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DA8")

    label("loc_D49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA8")

    ChrTalk(    #25
        0x102,
        (
            "#1502F#6PWho would've thought a place like this existed\x01",
            "under an orphanage?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA8")


    ChrTalk(    #26
        0x109,
        (
            "#1067F#5P...\x02\x03",

            "#1065FThis was where I finally caught up to the jaeger\x01",
            "who had you with him.\x02\x03",

            "#1840FHe probably didn't think anyone was gonna come\x01",
            "after him.\x02\x03",

            "The second he saw me, he panicked...and putting\x01",
            "his gun down, he ran over to this pedestal right in\x01",
            "front of us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_EC6():
        OP_6D(-1200, -750, 28500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_EC6)

    def lambda_EDE():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x6D2E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EDE)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #27
        0x109,
        (
            "#1065F#5POn it was the artifact that required sealing away\x01",
            "I mentioned earlier: the Spear of Loa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1802F#6PWhat's the Spear of Loa?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #29
        0x109,
        (
            "#1063F#11PA malignant spear that transforms the body of\x01",
            "its wielder into that of a monster.\x02\x03",

            "It's hard to believe something like that could be\x01",
            "a gift from the Goddess, right?\x02\x03",

            "#1065FIn any case, the cornered jaeger grabbed it and\x01",
            "used it.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_109B():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_109B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_1D(0xAF)
    OP_44(0xEE, 0x0)
    OP_6D(91010, -750, 14010, 0)
    OP_67(0, 5290, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(315000, 0)
    OP_6E(210, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS464._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS465._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS466._CH")
    OP_AD(0x240160, 0x0, 0x0, 0xC8)
    Sleep(2500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #30
        (
            "\x07\x0C#40W...I didn't stand a chance.\x02\x03",

            "Much as I tried, I wasn't any match for the inhuman monster before me.\x02\x03",

            "He knocked me to the ground, and then went to raise the spear against the\x01",
            "still-unconscious you...\x02\x03",

            "That's all it took.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x12C)
    Sleep(2000)
    OP_22(0x1BF, 0x0, 0x64)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    Sleep(1000)
    OP_22(0x2F2, 0x1, 0x64)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(3000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_22(0x334, 0x0, 0x64)
    OP_22(0x2D6, 0x0, 0x64)
    Sleep(1500)
    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_22(0x227, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A2, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B5, 0x0, 0x64)
    Sleep(1000)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    FadeToDark(0, 16777215, -1)
    OP_C6(0x2, 0x3, 16777215, 3000, 0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0x5)
    OP_43(0x109, 0x2, 0x0, 0x6)
    Sleep(500)
    OP_43(0x109, 0x3, 0x0, 0x7)
    Sleep(1500)
    Sleep(1500)
    OP_23(0x2F2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_22(0x271, 0x0, 0x64)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #31
        (
            "\x07\x0C#40WMy Stigma drew all of the spear's power from it into itself...\x02\x03",

            "...and blasted it, magnified countless times over, into the jaeger's body.\x02\x03",

            "The result wasn't even a battle; our precious home became a slaughterhouse.\x02\x03",

            "By the end, he wasn't even recognizable. Just thousands of lumps of flesh\x01",
            "strewn all over the floor.\x02\x03",

            "After defeating him, my Stigma's power was still coursing through my body...\x02\x03",

            "I'd never experienced anything like that before. I lost complete control of\x01",
            "myself. \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240164, 0x0, 0x0, 0xC8)
    Sleep(2500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #32
        (
            "\x07\x0C#40WAt this point, Rufina arrived, and she seemed to understand exactly what had\x01",
            "happened.\x02\x03",

            "Using her bowgun and templar sword, she was able to separate me from you\x01",
            "and prevent me from doing you any harm.\x02\x03",

            "And then...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x12C)
    Sleep(2000)
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS468._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS469._CH")
    OP_C6(0x3, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(1000)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_22(0x2F2, 0x1, 0x64)
    OP_22(0x227, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1A2, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B5, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(0, 16777215, -1)
    OP_C6(0x4, 0x3, 16777215, 3000, 0)
    OP_43(0x109, 0x0, 0x0, 0x4)
    Sleep(100)
    OP_43(0x109, 0x1, 0x0, 0x5)
    OP_43(0x109, 0x2, 0x0, 0x6)
    Sleep(500)
    OP_43(0x109, 0x3, 0x0, 0x7)
    Sleep(1500)
    Sleep(1500)
    OP_23(0x2F2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_22(0x271, 0x0, 0x64)
    Sleep(2000)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(2000)
    OP_AD(0x240167, 0x0, 0x0, 0x64)
    Sleep(4000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Kevin")

    AnonymousTalk(    #33
        (
            "\x07\x0C#40WWhen I returned to my senses, I was in her arms, dumfounded.\x02\x03",

            "Her body was full of holes all over, but she hugged me as tightly as she\x01",
            "could...\x02\x03",

            "That's when she drew her last breath.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_AE(0x64)
    Sleep(3000)
    OP_6D(-1200, -750, 27200, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(210, 0)
    Sleep(1000)

    def lambda_1926():
        OP_6B(4300, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1926)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #34
        0x10F,
        "#1809F#6P#60W...No...\x02",
    )

    CloseMessageWindow()

    def lambda_1960():

        label("loc_1960")

        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0xBB8)
        OP_48()
        Jump("loc_1960")

    QueueWorkItem2(0x10F, 3, lambda_1960)

    def lambda_197D():
        OP_8F(0xFE, 0xB4, 0xFFFFFD12, 0x5D5C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_197D)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x10F, 0x3)
    Sleep(1000)

    ChrTalk(    #35
        0x109,
        (
            "#1846F#11PThere it is. The truth you wanted.\x02\x03",

            "#1845FIt wasn't that I couldn't save Rufina...\x02\x03",

            "#1844FI was the one who killed her.\x02\x03",

            "With my own hands. Right in front of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        (
            "#1960F#6PB-But...\x02\x03",

            "#1449FB-But you didn't...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1843F#11PI didn't want to? Maybe not, but that's just an\x01",
            "excuse.\x02\x03",

            "If I'd been able to control my Stigma's power\x01",
            "instead of letting it consume me and fill me\x01",
            "with bloodlust, it wouldn't have happened.\x02\x03",

            "#1844FIf I wasn't so weak, she'd still be alive today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10F,
        "#1809F#6P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1076F#11P#40WThat's not all, either.\x02\x03",

            "Looking at her standing before me at that\x01",
            "moment, she reminded me of my mother.\x02\x03",

            "She reminded me of Mom when she came to\x01",
            "strangle me.\x02\x03",

            "#1065FSuddenly, this feeling of betrayal welled up inside me,\x01",
            "this desire for revenge...so I filled her full of spears.\x02\x03",

            "I loved them both. I wanted to protect them both...\x02\x03",

            "#1845FHeh... And what did I do? I killed them both.\x01",
            "Me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10F,
        "#1445F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrChipByIndex(0x10F, 4)
    SetChrSubChip(0x10F, 16)
    SetChrFlags(0x10F, 0x2)
    OP_0D()
    OP_9E(0x10F, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #41
        0x10F,
        "#1960F#6P...Why? Why...did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        "#1074F#11PWhy did I what?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_99(0x10F, 0x11, 0x13, 0x5DC)
    OP_0D()
    Sleep(500)

    ChrTalk(    #43
        0x10F,
        "#1964F#6P#3SWhy didn't you tell me this before?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #44
        0x10F,
        (
            "#1963F#6PFive years apart, and THIS is the first time\x01",
            "you're telling me this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1076F#11PSorry... I know I should've done it earlier.\x02\x03",

            "#1065FBut now I have. And I'm ready for the consequences.\x02\x03",

            "#1844FSo go on. If you want to avenge her, do it. If anything,\x01",
            "it'd make me happy if you did.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #46
        0x10F,
        "#1961F#4S#6PYOU'RE SO STUPID!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearChrFlags(0x10F, 0x2)
    SetChrFlags(0x10F, 0x20)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)

    def lambda_1FA7():
        OP_8F(0xFE, 0xFA, 0xFFFFFD12, 0x6F54, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1FA7)

    def lambda_1FC2():
        OP_99(0xFE, 0x0, 0x7, 0x960)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1FC2)
    Sleep(100)
    Fade(500)
    OP_6D(-650, -750, 28650, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(250, 0)
    WaitChrThread(0x10F, 0x1)

    def lambda_201E():
        OP_99(0xFE, 0x0, 0x1, 0x960)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_201E)
    Sleep(30)
    OP_44(0x10F, 0x0)
    ClearChrFlags(0x10F, 0x20)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 20)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0x10F, 0x8)
    OP_99(0x109, 0x15, 0x16, 0x3E8)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x109, 4)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x10F, 200, -750, 27300, 0)
    WaitChrThread(0x10F, 0x0)
    Sleep(800)

    ChrTalk(    #47
        0x109,
        "#1079F#11PWh-What're you...?\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(300)

    ChrTalk(    #48
        0x10F,
        (
            "#1964F#6PYou think I want to avenge her?!\x02\x03",

            "That's not why I'm angry at all!\x02\x03",

            "Why have you shouldered a burden that\x01",
            "great all this time all on your own?!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #49
        0x10F,
        (
            "#1960F#6PWe're FAMILY, Kevin!\x02\x03",

            "Why didn't you ever talk to me?! Why didn't you\x01",
            "ever let me hug you?! Why didn't you let me do\x01",
            "ANYTHING to help you?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2273")

    ChrTalk(    #50
        0x101,
        "#1026F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_2273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229B")

    ChrTalk(    #51
        0x107,
        "#063F#5PR-Ries...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_229B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C2")

    ChrTalk(    #52
        0x105,
        "#1163F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_22C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E8")

    ChrTalk(    #53
        0x10A,
        "#813F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_22E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_230E")

    ChrTalk(    #54
        0x10B,
        "#215F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_230E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2334")

    ChrTalk(    #55
        0x10E,
        "#175F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_2334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_235B")

    ChrTalk(    #56
        0x102,
        "#1503F#5PRies...\x02",
    )

    CloseMessageWindow()
    Jump("loc_237F")

    label("loc_235B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_237F")

    ChrTalk(    #57
        0x104,
        "#1542F#5PRies...\x02",
    )

    CloseMessageWindow()

    label("loc_237F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A3")

    ChrTalk(    #58
        0x110,
        "#1307F#5PRies...\x02",
    )

    CloseMessageWindow()

    label("loc_23A3")

    WaitChrThread(0xEE, 0x3)
    OP_99(0x109, 0x7, 0xB, 0x3E8)
    Sleep(300)

    ChrTalk(    #59
        0x109,
        "#1067F#11P...I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        (
            "#1960F#6P#40WI finally understand...\x02\x03",

            "I always thought you were hunting down heretics\x01",
            "as some kind of atonement for letting Rufina die.\x02\x03",

            "#1962FBut that's not it at all, is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x109, 0)
    OP_0D()

    ChrTalk(    #61
        0x109,
        "#1847F#11PC-Come on, Ries...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10F,
        (
            "#1960F#6P#40WI finally, finally understand.\x02\x03",

            "You don't want to atone for anything.\x02\x03",

            "You don't want to get rid of your sense\x01",
            "of guilt at all...\x02\x03",

            "#1963FYou... You...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    OP_20(0x7D0)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x07\x02That's right. He wants to be punished\x01",
            "for what he did.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_261E")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2685")

    label("loc_261E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2646")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2685")

    label("loc_2646")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266E")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2685")

    label("loc_266E")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2685")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B2")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2719")

    label("loc_26B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26DA")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2719")

    label("loc_26DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2702")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2719")

    label("loc_2702")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2719")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2746")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_27AD")

    label("loc_2746")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_276E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_27AD")

    label("loc_276E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2796")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_27AD")

    label("loc_2796")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_27AD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DA")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2841")

    label("loc_27DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2802")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2841")

    label("loc_2802")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_282A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2841")

    label("loc_282A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2841")

    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -9900, -1000, 27300, 90)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 11)
    OP_1D(0xE0)
    Fade(1000)
    OP_6D(-10970, -1000, 28100, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(171, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(240)

    def lambda_28DE():
        OP_6B(4300, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_28DE)
    Sleep(500)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_296C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_296C)
    OP_22(0x59, 0x0, 0x64)
    WaitChrThread(0x10, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29AF")
    OP_8C(0xF0, 270, 0)
    OP_8C(0xF1, 270, 0)
    Jump("loc_29EA")

    label("loc_29AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CE")
    OP_8C(0xEF, 270, 0)
    OP_8C(0xF1, 270, 0)
    Jump("loc_29EA")

    label("loc_29CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29EA")
    OP_8C(0xEF, 270, 0)
    OP_8C(0xF0, 270, 0)

    label("loc_29EA")

    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-4700, -750, 27500, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #64
        0x10F,
        "#1444F#6POh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A84")

    ChrTalk(    #65
        0x10D,
        "#271F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2A84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AB9")

    ChrTalk(    #66
        0x108,
        "#076F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AEE")

    ChrTalk(    #67
        0x106,
        "#054F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2AEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B24")

    ChrTalk(    #68
        0x103,
        "#1524F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2B24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B5A")

    ChrTalk(    #69
        0x102,
        "#1506F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_2B5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B8C")

    ChrTalk(    #70
        0x10E,
        "#177F#5PThe Lord of Phantasma!\x02",
    )

    CloseMessageWindow()

    label("loc_2B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BC6")

    ChrTalk(    #71
        0x104,
        "#1542F#5PSo you finally show yourself!\x02",
    )

    CloseMessageWindow()

    label("loc_2BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF3")

    ChrTalk(    #72
        0x10B,
        "#216F#5PTh-There you are!\x02",
    )

    CloseMessageWindow()

    label("loc_2BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C2C")

    ChrTalk(    #73
        0x10A,
        "#1317F#5PWh-Where did you come from?!\x02",
    )

    CloseMessageWindow()

    label("loc_2C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4D")

    ChrTalk(    #74
        0x107,
        "#065F#5PEeek!\x02",
    )

    CloseMessageWindow()

    label("loc_2C4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C87")

    ChrTalk(    #75
        0x101,
        "#1002F#5PWh-Why now, of all times?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CBE")

    label("loc_2C87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CBE")

    ChrTalk(    #76
        0x105,
        "#1163F#5PWh-Why now, of all times?!\x02",
    )

    CloseMessageWindow()

    label("loc_2CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CFB")

    ChrTalk(    #77
        0x10C,
        "#112F#5PSo this is the Lord of Phantasma?\x02",
    )

    CloseMessageWindow()

    label("loc_2CFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D3B")

    ChrTalk(    #78
        0x110,
        "#1305F#5PSo that's what they look like, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_2D3B")

    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x10F, 0x8)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10F, 0x0, 0x0, 0x8)

    def lambda_2D6A():
        OP_6D(-4900, -750, 27700, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2D6A)

    def lambda_2D82():
        OP_67(0, 4500, -10000, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D82)

    def lambda_2D9A():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2D9A)

    def lambda_2DAA():
        OP_6C(307000, 500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2DAA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DE5")
    OP_43(0xF0, 0x0, 0x0, 0x9)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    WaitChrThread(0xF0, 0x0)
    Jump("loc_2E44")

    label("loc_2DE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E16")
    OP_43(0xEF, 0x0, 0x0, 0xA)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    WaitChrThread(0xEF, 0x0)
    Jump("loc_2E44")

    label("loc_2E16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E44")
    OP_43(0xEF, 0x0, 0x0, 0xB)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 23)
    SetChrSubChip(0xF0, 0)
    WaitChrThread(0xEF, 0x0)

    label("loc_2E44")

    WaitChrThread(0x10F, 0x0)
    OP_8C(0x109, 270, 400)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(800)

    NpcTalk(    #79
        0x10,
        "Lord of Phantasma",
        (
            "\x07\x02#1580F#5PHaha... You have my congratulations on making\x01",
            "it this far.\x02\x03",

            "Beyond here lies the seventh plane.\x02\x03",

            "The place of my birth, and the foundation\x01",
            "of all planes hereafter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        (
            "#1065F#12PThought so.\x02\x03",

            "#1067FAnd judging by how we have to go\x01",
            "through here to get there...\x02\x03",

            "#1840F...I was right, wasn't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10F,
        "#1444F#6PRight about what...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x10,
        "Lord of Phantasma",
        (
            "\x07\x02#1580F#5PAllow me to ask you once again.\x02\x03",

            "So, Kevin Graham...\x02\x03",

            "Do you really want to see the face\x01",
            "underneath this mask?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x109,
        (
            "#1075F#12PDamn right, I do.\x02\x03",

            "#1063FIt's time to take that creepy mask thing\x01",
            "and show us who you really are...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #84
        0x109,
        "#1069F#12P#3S...Rufina Argent!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3132")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3199")

    label("loc_3132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3199")

    label("loc_315A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3182")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3199")

    label("loc_3182")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3199")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_322D")

    label("loc_31C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31EE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_322D")

    label("loc_31EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3216")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_322D")

    label("loc_3216")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_322D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32C1")

    label("loc_325A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3282")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32C1")

    label("loc_3282")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32AA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_32C1")

    label("loc_32AA")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_32C1")

    Sleep(1300)

    NpcTalk(    #85
        0x10,
        "Lord of Phantasma",
        "\x07\x02#1580F#5P#3SHahaha. With pleasure!\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3318():
        OP_6D(-11500, -1000, 29200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3318)

    def lambda_3330():
        OP_67(0, 3590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3330)

    def lambda_3348():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3348)

    def lambda_3358():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3358)

    def lambda_3368():
        OP_6E(281, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3368)
    WaitChrThread(0xEE, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 0, -1000, 23000, 270)
    Sleep(300)
    OP_99(0x10, 0x0, 0x2, 0x4B0)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_33B0():
        OP_6B(2850, 500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_33B0)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x10, 0x3, 0x7, 0x3E8)
    OP_0D()
    Sleep(500)
    OP_99(0x10, 0x7, 0xA, 0x4B0)
    Sleep(500)

    NpcTalk(    #86
        0x109,
        "Ries",
        "#1809F#1PR-Rufina...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS471._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Rufina")

    AnonymousTalk(    #87
        (
            "\x07\x02I've missed you dearly, Ries.\x02\x03",

            "And as for you, Kevin...I'm impressed you were able to work out my real\x01",
            "identity.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #88
        0x109,
        (
            "#1065F#1PIt wasn't hard. I had a feeling from the start.\x02\x03",

            "#1067FThe answer was right in front of my face the \x01",
            "whole time, and your every taunt should have\x01",
            "made me that much more sure.\x02\x03",

            "#1840FThe only reason I couldn't be until now was\x01",
            "because I didn't want to accept the truth.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-4800, -750, 27500, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 180, -750, 27950, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #89
        0x10,
        (
            "\x07\x02#1586F#5PQuite. You always were a weakling.\x02\x03",

            "#1587FYou can imagine how surprised I was when you\x01",
            "were able to defeat my strongest knight.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1065F#12PYou talking about the Bladelord?\x02\x03",

            "#1063FWhat connection does he even have to you,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "\x07\x02#1581F#5PI met him through my work, oh...about six years\x01",
            "ago.\x02\x03",

            "#1586FWe were enemies at the time, but we managed\x01",
            "to reach a compromise of sorts.\x02\x03",

            "#1582FAnd he felt he owed me a debt for as much.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        (
            "#1075F#12PAll right. So you ended up summoning him\x01",
            "in order to have him repay it?\x02\x03",

            "#1840FIt's a crafty move, but that's not so out of\x01",
            "character for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "\x07\x02#1586F#5PHaha... Flattery won't get you anywhere with me.\x02\x03",

            "#1587FStill, now that you've made it this far...I assume\x01",
            "you understand what I'm trying to do?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1840F#12PYeah...and I'm ready.\x02\x03",

            "#1075FTake me away.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #95
        0x10F,
        (
            "#1809F#6PW-Wait!\x02\x03",

            "What are you two talking about?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        "#1067F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10,
        (
            "\x07\x02#1586F#5PI would have thought you worked the answer to\x01",
            "that out already, Ries.\x02\x03",

            "#1582FDo you recall what I said before? Kevin wants to\x01",
            "be punished.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ADF")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3B46")

    label("loc_3ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B07")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3B46")

    label("loc_3B07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3B46")

    label("loc_3B2F")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3B46")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B73")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BDA")

    label("loc_3B73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B9B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BDA")

    label("loc_3B9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BC3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3BDA")

    label("loc_3BC3")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3BDA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C07")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6E")

    label("loc_3C07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C2F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6E")

    label("loc_3C2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C57")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6E")

    label("loc_3C57")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3C6E")

    Sleep(1200)

    ChrTalk(    #98
        0x10F,
        "#1444F#6PTh-Then you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "\x07\x02#1586F#5PI was born here in order to give him the punishment\x01",
            "he strives for with his every breath.\x02\x03",

            "It was to that end that I recreated Phantasma into\x01",
            "its current form and welcomed all of you here.\x02\x03",

            "#1587FAll of this was a result of Kevin's desires. He wanted\x01",
            "this to happen.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10F,
        "#1449F#6PY-You're lying!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        (
            "#1065F#11P...Sorry. She isn't.\x02\x03",

            "#1067FI couldn't tell you why it all actually happened...\x02\x03",

            "#1840F...but what she says is true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10F,
        "#1445F#6PN-No...\x02",
    )

    CloseMessageWindow()

    def lambda_3E6B():
        OP_6D(-5700, -750, 27600, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3E6B)
    OP_8F(0x109, 0xFFFFFA92, 0xFFFFFC18, 0x6E32, 0x3E8, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #103
        0x109,
        (
            "#1846F#12PThe seventh plane is likely somewhere made for the\x01",
            "express purpose of punishing me over and over.\x02\x03",

            "A fitting hell for someone who let his own mother die\x01",
            "and killed Rufina to suffer and rot.\x02\x03",

            "#1844F...And once I'm dropped down there, this'll all be over.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FD6")

    ChrTalk(    #104
        0x10E,
        "#172F#5PI-Impossible...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4027")

    label("loc_3FD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4000")

    ChrTalk(    #105
        0x108,
        "#077F#5PImpossible!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4027")

    label("loc_4000")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4027")

    ChrTalk(    #106
        0x10C,
        "#117F#5PImpossible!\x02",
    )

    CloseMessageWindow()

    label("loc_4027")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_405D")

    ChrTalk(    #107
        0x107,
        "#566F#5PB-But that's not right!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4091")

    label("loc_405D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4091")

    ChrTalk(    #108
        0x105,
        "#1163F#5PB-But that's not right!\x02",
    )

    CloseMessageWindow()

    label("loc_4091")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E0")

    ChrTalk(    #109
        0x101,
        "#1020F#5PWait a second! Why should you have to do that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4179")

    label("loc_40E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_412E")

    ChrTalk(    #110
        0x10B,
        "#214F#5PWait a second! Why should you have to do that?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4179")

    label("loc_412E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4179")

    ChrTalk(    #111
        0x10A,
        "#815F#5PWait a second! Why should you have to do that?!\x02",
    )

    CloseMessageWindow()

    label("loc_4179")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41B5")

    ChrTalk(    #112
        0x102,
        "#1502F#5PYou can't be serious, Kevin!\x02",
    )

    CloseMessageWindow()
    Jump("loc_425D")

    label("loc_41B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41EC")

    ChrTalk(    #113
        0x103,
        "#1522F#5PY-You can't be serious!\x02",
    )

    CloseMessageWindow()
    Jump("loc_425D")

    label("loc_41EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_422C")

    ChrTalk(    #114
        0x106,
        "#057F#5PWhat the hell is wrong with you?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_425D")

    label("loc_422C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_425D")

    ChrTalk(    #115
        0x10D,
        "#270F#5PYou can't be serious!\x02",
    )

    CloseMessageWindow()

    label("loc_425D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42E5")

    ChrTalk(    #116
        0x104,
        (
            "#1544F#5PI can't believe what I'm hearing...\x02\x03",

            "#1542FI think that might be a little hasty\x01",
            "of a conclusion, don't you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4350")

    ChrTalk(    #117
        0x110,
        (
            "#268F#6PI mean...I suppose it makes sense...\x02\x03",

            "#262F...but I still can't understand why.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4350")


    ChrTalk(    #118
        0x10F,
        "#1960F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4376():
        OP_6D(-10110, -1000, 28290, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4376)

    def lambda_438E():
        OP_67(0, 4300, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_438E)

    def lambda_43A6():
        OP_6B(2750, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_43A6)

    def lambda_43B6():
        OP_6E(280, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_43B6)
    SetChrFlags(0x10F, 0x1000)
    OP_7D(0x0, 0x10F, 0x32, 0x1F4)
    SetChrChipByIndex(0x10F, 9)

    def lambda_43D8():
        OP_8F(0xFE, 0xFFFFEDB8, 0xFFFFFC18, 0x6702, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_43D8)
    WaitChrThread(0x10F, 0x1)
    OP_7D(0x1, 0x10F, 0x0, 0x0)
    OP_22(0x19A, 0x0, 0x64)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 4)
    PlayEffect(0x4, 0x4, 0x10F, 0, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0x0, 0x10F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_23(0xC9)
    PlayEffect(0x0, 0x5, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_460B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_460B)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0x2CE, 0x0, 0x64)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_82(0x5, 0x2)
    OP_82(0x7, 0x2)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Fade(250)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #119
        0xF0,
        "Kevin",
        "#1847F#1PRies?!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(0, 3)
    Return()

    # Function_2_225 end

    def Function_3_4788(): pass

    label("Function_3_4788")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    OP_E0(238, 0x55, 0x2)
    OP_E0(239, 0x56, 0x2)
    OP_E0(240, 0x57, 0x2)
    OP_E0(241, 0x58, 0x2)
    OP_E0(238, 0x59, 0x5)
    OP_E0(239, 0x5A, 0x5)
    OP_E0(240, 0x5B, 0x5)
    OP_E0(241, 0x5C, 0x5)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7770, 1350, 28370, 0)
    OP_67(0, 4410, -10000, 0)
    OP_6B(3280, 0)
    OP_6C(254000, 0)
    OP_6E(385, 0)
    SetChrPos(0x109, -1870, -1000, 28340, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4878")
    SetChrPos(0xEF, -8400, -1000, 28050, 270)
    SetChrPos(0xF0, -1000, -1000, 24910, 315)
    SetChrPos(0xF1, -1770, -1000, 23520, 315)
    Jump("loc_48FD")

    label("loc_4878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48BC")
    SetChrPos(0xF0, -8400, -1000, 28050, 270)
    SetChrPos(0xEF, -1000, -1000, 24910, 315)
    SetChrPos(0xF1, -1770, -1000, 23520, 315)
    Jump("loc_48FD")

    label("loc_48BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48FD")
    SetChrPos(0xF1, -8400, -1000, 28050, 270)
    SetChrPos(0xEF, -1000, -1000, 24910, 315)
    SetChrPos(0xF0, -1770, -1000, 23520, 315)

    label("loc_48FD")

    SetChrChipByIndex(0xEF, 22)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 23)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 24)
    SetChrSubChip(0xF1, 0)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -13610, 1300, 31690, 135)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)

    def lambda_4946():

        label("loc_4946")

        OP_99(0xFE, 0x0, 0x7, 0x4B0)
        OP_48()
        Jump("loc_4946")

    QueueWorkItem2(0x10, 2, lambda_4946)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_498E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_498E)
    OP_22(0x59, 0x0, 0x64)
    OP_82(0x1, 0x2)
    OP_0D()
    Sleep(300)

    def lambda_49AE():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_49AE)

    def lambda_49BC():
        OP_6D(-16640, -1000, 28090, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_49BC)

    def lambda_49D4():
        OP_67(0, 3950, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_49D4)

    def lambda_49EC():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_49EC)

    def lambda_49FC():
        OP_6C(254000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_49FC)

    def lambda_4A0C():
        OP_6E(364, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4A0C)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    NpcTalk(    #120
        0x10,
        "Rufina",
        (
            "\x07\x02#1582F#11PWhat do you think you're doing, Ries?\x02\x03",

            "That's not a very nice thing to do to your\x01",
            "sister.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10F,
        (
            "#1961F#6PShut up!\x02\x03",

            "#1449FYou're not my sister!\x02\x03",

            "My sister would never do something like this!\x01",
            "Never!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x109,
        "#1063F#5PR-Ries...\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #123
        0x10F,
        (
            "#1445F#5PYou promised me, Kevin!\x02\x03",

            "You promised me that you'd never do anything\x01",
            "that would make Rufina sad!\x02\x03",

            "#1446FSo what do you think you're doing?!\x02\x03",

            "#1449FHow can you believe sacrificing yourself for\x01",
            "everyone would make her happy?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x109,
        "#1063F#5P#3SRies...stop...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #125
        0x10,
        "Rufina",
        (
            "\x07\x02#1586F#11PHeehee. Who are you to say it wouldn't?\x02\x03",

            "#1587FI might not be the real Rufina, but I'm a very\x01",
            "close copy of her.\x02\x03",

            "If Kevin wants to be punished, why wouldn't\x01",
            "I want to give him his wish?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #126
        0x10F,
        "#1961F#6P#3SBecause that's not how Rufina was at all!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #127
        0x10F,
        (
            "#1964F#6PShe'd never indulge something like that.\x01",
            "Not in a thousand years!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #128
        0x109,
        "#1079F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x10,
        "\x07\x02#1583F#11P...\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10F,
        (
            "#1960F#5PThink back to when you first met us, Kevin!\x02\x03",

            "You'd given up on the world, like you just wanted to\x01",
            "disappear...but did she let you do that? No!\x02\x03",

            "#1963FShe forced chocolate down your throat and dragged\x01",
            "you right back into the real world, even when you\x01",
            "didn't want to! Whether you liked it or not!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x109,
        "#1847F#5P...She...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24010D, 0x0, 0x0, 0x12C)
    Sleep(3000)
    SetChrPos(0x109, -2510, -1000, 229370, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FAB")
    SetChrPos(0xEF, -8950, -1000, 228090, 315)
    SetChrPos(0xF0, -1680, -1000, 224520, 315)
    SetChrPos(0xF1, -3130, -1000, 223400, 315)
    Jump("loc_5030")

    label("loc_4FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FEF")
    SetChrPos(0xF0, -8950, -1000, 228090, 315)
    SetChrPos(0xEF, -1680, -1000, 224520, 315)
    SetChrPos(0xF1, -3130, -1000, 223400, 315)
    Jump("loc_5030")

    label("loc_4FEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5030")
    SetChrPos(0xF1, -8950, -1000, 228090, 315)
    SetChrPos(0xEF, -1680, -1000, 224520, 315)
    SetChrPos(0xF0, -3130, -1000, 223400, 315)

    label("loc_5030")

    SetChrPos(0x10, -10000, 1800, 235260, 135)
    OP_6D(-1690, -1000, 227040, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(155000, 0)
    OP_6E(457, 0)
    OP_AE(0x12C)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)

    ChrTalk(    #132
        0x109,
        (
            "#1067F#5P#40W...\x02\x03",

            "...I... I...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-6710, -100, 228480, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2150, 0)
    OP_6C(155000, 0)
    OP_6E(486, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #133
        0x10,
        "Rufina",
        (
            "\x07\x02#1586F#6PHaha... Well, this is a surprise.\x02\x03",

            "#1582FYou've grown a lot more than I was expecting\x01",
            "if you're able to talk back to me.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10F,
        (
            "#1964F#5PStop talking to me as if you're my sister!\x02\x03",

            "You are not, and I won't stand for you defiling\x01",
            "her any further!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #135
        0x10,
        "Rufina",
        (
            "\x07\x02#1586F#6PHmm... Well, if that's how you want to do things...\x02\x03",

            "#1587F...perhaps I should invite you in Kevin's place?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10F,
        "#1809F#5PMe...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    LoadEffect(0x0, "map\\mp300_00.eff")
    LoadEffect(0x1, "map\\mp300_01.eff")
    LoadEffect(0x2, "map\\mp300_02.eff")
    LoadEffect(0x3, "map\\mp307_00.eff")
    LoadEffect(0x4, "map\\mp262_02.eff")
    LoadEffect(0x5, "monster\\msc1000.eff")
    PlayEffect(0x5, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x1, 0x50)
    OP_22(0x32E, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x25D, 0x0, 0x64)
    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x2A5, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -9050, -950, 27500, -45, 0, 0, 850, 850, 850, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -9150, -950, 228000, -45, 0, 0, 850, 850, 850, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5436")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_549D")

    label("loc_5436")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_545E")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_549D")

    label("loc_545E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5486")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_549D")

    label("loc_5486")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_549D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54CA")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5531")

    label("loc_54CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54F2")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5531")

    label("loc_54F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_551A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5531")

    label("loc_551A")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5531")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_555E")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_55C5")

    label("loc_555E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5586")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_55C5")

    label("loc_5586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_55C5")

    label("loc_55AE")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_55C5")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F2")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5659")

    label("loc_55F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_561A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5659")

    label("loc_561A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5642")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5659")

    label("loc_5642")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5659")

    Sleep(1000)
    OP_44(0x109, 0x3)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x10F, 0x20)
    SetChrFlags(0x10F, 0x4)
    SetChrChipByIndex(0x10F, 6)

    def lambda_5686():
        OP_8F(0xFE, 0xFFFFDD0A, 0xFFFFFBB4, 0x37AFA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5686)
    OP_99(0x10F, 0x0, 0x3, 0x5DC)
    OP_43(0x10F, 0x3, 0x0, 0xD)
    Fade(1000)
    SetChrPos(0x109, -1560, -1000, 28800, 270)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570F")
    SetChrPos(0xEF, -8600, -1100, 27600, 0)
    SetChrPos(0xF0, -770, -1000, 24740, 315)
    SetChrPos(0xF1, -1400, -1000, 23310, 315)
    Jump("loc_5794")

    label("loc_570F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5753")
    SetChrPos(0xF0, -8600, -1100, 27600, 0)
    SetChrPos(0xEF, -770, -1000, 24740, 315)
    SetChrPos(0xF1, -1400, -1000, 23310, 315)
    Jump("loc_5794")

    label("loc_5753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5794")
    SetChrPos(0xF1, -8600, -1100, 27600, 0)
    SetChrPos(0xEF, -770, -1000, 24740, 315)
    SetChrPos(0xF0, -1400, -1000, 23310, 315)

    label("loc_5794")

    SetChrPos(0x10, -10000, 1800, 32500, 135)
    OP_6D(-6410, -1000, 27820, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(318000, 0)
    OP_6E(314, 0)
    OP_82(0x2, 0x2)
    OP_23(0x32E)
    OP_23(0x137)
    OP_0D()

    ChrTalk(    #137
        0x109,
        "#1069F#6PNo...\x02",
    )

    CloseMessageWindow()

    def lambda_5806():
        OP_6D(-3580, 1550, 25440, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5806)

    def lambda_581E():
        OP_67(0, 3500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_581E)

    def lambda_5836():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5836)

    def lambda_5846():
        OP_6C(318000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5846)

    def lambda_5856():
        OP_6E(331, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5856)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    NpcTalk(    #138
        0x10,
        "Rufina",
        "\x07\x02#1582F#6PThe rest of you can stand by and watch.\x07\x00\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x3, 0x1, 0xFF, -3800, 2000, 26680, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(1000)
    PlayEffect(0x4, 0x2, 0xFF, -2000, -1000, 29020, 0, 0, 0, 500, 700, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x3, 0xFF, -1200, -1000, 24060, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0x1B9, 0x0, 0x64)
    OP_22(0x3DC, 0x1, 0x50)
    OP_0D()
    Fade(500)

    def lambda_596A():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_596A)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 4)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59FF")

    def lambda_59AB():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_59AB)
    SetChrChipByIndex(0xF0, 27)
    SetChrSubChip(0xF0, 3)
    SetChrFlags(0xF0, 0x800)
    Sleep(30)

    def lambda_59D9():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_59D9)
    SetChrChipByIndex(0xF1, 28)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xF1, 0x800)
    Jump("loc_5ACC")

    label("loc_59FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A67")

    def lambda_5A13():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5A13)
    SetChrChipByIndex(0xEF, 26)
    SetChrSubChip(0xEF, 3)
    SetChrFlags(0xEF, 0x800)
    Sleep(30)

    def lambda_5A41():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_5A41)
    SetChrChipByIndex(0xF1, 28)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xF1, 0x800)
    Jump("loc_5ACC")

    label("loc_5A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ACC")

    def lambda_5A7B():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5A7B)
    SetChrChipByIndex(0xEF, 26)
    SetChrSubChip(0xEF, 3)
    SetChrFlags(0xEF, 0x800)
    Sleep(30)

    def lambda_5AA9():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_5AA9)
    SetChrChipByIndex(0xF0, 27)
    SetChrSubChip(0xF0, 3)
    SetChrFlags(0xF0, 0x800)

    label("loc_5ACC")

    OP_0D()
    OP_82(0x1, 0x0)
    Sleep(300)

    ChrTalk(    #139
        0x109,
        "#1070F#5PGuh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B14")

    ChrTalk(    #140
        0x101,
        "#1021F#5PW-Wha...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B63")

    label("loc_5B14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B3D")

    ChrTalk(    #141
        0x104,
        "#1549F#5PWhat...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B63")

    label("loc_5B3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B63")

    ChrTalk(    #142
        0x10E,
        "#172F#5PW-Wha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_5B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B91")

    ChrTalk(    #143
        0x10B,
        "#216F#5PI-I can't move!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5BBD")

    label("loc_5B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BBD")

    ChrTalk(    #144
        0x103,
        "#1533F#5PI-I can't move!\x02",
    )

    CloseMessageWindow()

    label("loc_5BBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(    #145
        0x107,
        "#562F#5PA-Aaah!\x02",
    )

    CloseMessageWindow()

    label("loc_5BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C0D")

    ChrTalk(    #146
        0x10A,
        "#1312F#5PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    label("loc_5C0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C32")

    ChrTalk(    #147
        0x105,
        "#1381F#5PN-No...!\x02",
    )

    CloseMessageWindow()

    label("loc_5C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C56")

    ChrTalk(    #148
        0x106,
        "#057F#5PDamn it!\x02",
    )

    CloseMessageWindow()

    label("loc_5C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C7E")

    ChrTalk(    #149
        0x108,
        "#077F#5PWhat...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CCB")

    label("loc_5C7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA6")

    ChrTalk(    #150
        0x10D,
        "#271F#5PWhat...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CCB")

    label("loc_5CA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CCB")

    ChrTalk(    #151
        0x10C,
        "#117F#5PWhat...?!\x02",
    )

    CloseMessageWindow()

    label("loc_5CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CFA")

    ChrTalk(    #152
        0x110,
        "#1301F#5PIt's the Evil Eye!\x02",
    )

    CloseMessageWindow()

    label("loc_5CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3E")

    ChrTalk(    #153
        0x102,
        "#1507F#5PIt's just like the one that devil used!\x02",
    )

    CloseMessageWindow()

    label("loc_5D3E")

    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, -9050, -950, 27740, -45, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrFlags(0x10F, 0x4)
    SetChrFlags(0x10F, 0x2)
    SetChrChipByIndex(0x10F, 16)
    SetChrSubChip(0x10F, 2)
    SetChrFlags(0x10F, 0x20)
    SetChrFlags(0x10F, 0x1000)

    def lambda_5DA6():
        OP_67(0, 3200, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5DA6)

    def lambda_5DBE():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFF9C0, 0x6BD0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_5DBE)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #154
        0x10F,
        "#1804F#6P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x109,
        (
            "#1067F#12PRies!\x02\x03",

            "#1069FStop this, Rufina! She's got nothing to do with\x01",
            "any of this!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #156
        0x10,
        "Rufina",
        (
            "\x07\x02#1581F#6POh, but she has! Consider this another part of your\x01",
            "punishment.\x02\x03",

            "#1586FAfter all, if she suffers for all eternity in your place...\x02\x03",

            "#1587F...that's going to make your suffering all the more\x01",
            "potent, isn't it?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x109,
        "#1079F#12PPlease...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #158
        0x10F,
        "#1961F#6P#4SGo ahead and do your worst!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0xFFFFFEA2, 1600, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    NpcTalk(    #159
        0x10,
        "Rufina",
        "\x07\x02#1583F#6P...Oh?\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x109,
        "#1847F#12PRies...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10F,
        (
            "#1445F#6P#40WDrop me wherever you like. I'll live!\x02\x03",

            "#1446FI'm never going to let Kevin be alone again...\x02\x03",

            "#1806FI WILL come back to him!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #162
        0x109,
        "#1079F#12P...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #163
        0x10,
        "Rufina",
        (
            "\x07\x02#1586F#6PHaha. Fighting words, my sweet sister.\x02\x03",

            "#1582FWe shall see whether you can make good on them.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x25E, 0x0, 0x64)
    OP_22(0x339, 0x0, 0x64)
    PlayEffect(0x2, 0x0, 0xFF, -9050, -950, 27740, -45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_616B():
        OP_67(0, 2800, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_616B)
    Sleep(1000)
    Fade(500)
    OP_82(0x1, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #164 op#A op#5
        0x10F,
        "#1809F#5P#40W#10AAh...\x05\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x10F, 3)

    def lambda_61C1():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_61C1)
    Sleep(200)

    def lambda_61E1():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_61E1)
    Sleep(200)

    def lambda_6201():
        OP_8F(0xFE, 0xFFFFDE68, 0xFFFFEC78, 0x6BD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6201)
    WaitChrThread(0x10F, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x1, "map\\mp283_00.eff")
    LoadEffect(0x3, "map\\mp284_00.eff")
    LoadEffect(0x5, "map\\mp262_01.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x85, 0x1, 0x64)

    def lambda_6284():

        label("loc_6284")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_6284")

    QueueWorkItem2(0x10F, 3, lambda_6284)
    OP_22(0x34F, 0x0, 0x64)

    def lambda_62A4():
        OP_6D(-2830, -1000, 29900, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_62A4)

    def lambda_62BC():
        OP_67(0, 4500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62BC)

    def lambda_62D4():
        OP_6B(2470, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_62D4)

    def lambda_62E4():
        OP_6E(331, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_62E4)
    OP_43(0x109, 0x0, 0x0, 0x10)
    Sleep(1000)

    ChrTalk(    #165 op#A op#5
        0x109,
        "#1847F#4S#20A#11PHraaaaaaaaah!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x109, 0, 1300, -700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    OP_22(0x353, 0x0, 0x64)
    OP_22(0x34F, 0x0, 0x64)
    PlayEffect(0x3, 0x5, 0x109, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_63C0():

        label("loc_63C0")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_63C0")

    QueueWorkItem2(0x10F, 3, lambda_63C0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_22(0x139, 0x0, 0x64)
    OP_9E(0x109, 0xF, 0x0, 0x1F4, 0xFA0)
    Sleep(300)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)
    OP_22(0x1B3, 0x0, 0x64)
    OP_82(0x1, 0x2)
    PlayEffect(0x5, 0x7, 0xFF, -2000, -1000, 29020, 0, 0, 0, 500, 700, 500, 0xFF, 0, 0, 0, 0)
    OP_82(0x2, 0x2)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    OP_23(0x3DC)

    def lambda_645F():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_645F)

    def lambda_6477():
        OP_6B(2600, 300)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_6477)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65D6")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D3")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_653A")

    label("loc_64D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64FB")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_653A")

    label("loc_64FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6523")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_653A")

    label("loc_6523")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_653A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6567")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65CE")

    label("loc_6567")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_658F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65CE")

    label("loc_658F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65B7")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65CE")

    label("loc_65B7")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_65CE")

    Sleep(1000)
    Jump("loc_687D")

    label("loc_65D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_672B")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6628")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_668F")

    label("loc_6628")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6650")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_668F")

    label("loc_6650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6678")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_668F")

    label("loc_6678")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_668F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66BC")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6723")

    label("loc_66BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6723")

    label("loc_66E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_670C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6723")

    label("loc_670C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6723")

    Sleep(1000)
    Jump("loc_687D")

    label("loc_672B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_687D")
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_67E4")

    label("loc_677D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67A5")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_67E4")

    label("loc_67A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67CD")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_67E4")

    label("loc_67CD")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_67E4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6811")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6878")

    label("loc_6811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6839")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6878")

    label("loc_6839")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6861")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6878")

    label("loc_6861")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6878")

    Sleep(1000)

    label("loc_687D")

    OP_82(0x5, 0x2)
    Sleep(500)

    ChrTalk(    #166 op#A op#5
        0x10,
        "\x07\x02#1584F#6P#15AKevin...?\x05\x07\x00\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_43(0x109, 0x0, 0x0, 0x11)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_68D0():
        OP_6D(-8020, -1000, 27820, 500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_68D0)

    def lambda_68E8():
        OP_67(0, 5870, -10000, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_68E8)

    def lambda_6900():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_6900)
    OP_82(0x6, 0x2)
    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 10)
    OP_7D(0x0, 0x109, 0x32, 0x1F4)

    def lambda_6925():
        OP_8E(0xFE, 0xFFFFE7F0, 0xFFFFFC18, 0x6DBA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6925)
    WaitChrThread(0x109, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 6)

    def lambda_695E():
        OP_96(0xFE, 0xFFFFDE54, 0xFFFFD8F0, 0x6C70, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_695E)
    Sleep(300)
    SetChrSubChip(0x109, 7)
    WaitChrThread(0x109, 0x1)
    OP_7D(0x1, 0x109, 0x0, 0x0)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x10F, 0x3)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P7013   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_4788 end

    def Function_4_69CD(): pass

    label("Function_4_69CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69E3")
    OP_22(0xCB, 0x0, 0x64)
    Sleep(100)
    Jump("Function_4_69CD")

    label("loc_69E3")

    Return()

    # Function_4_69CD end

    def Function_5_69E4(): pass

    label("Function_5_69E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69FA")
    OP_22(0x38F, 0x0, 0x64)
    Sleep(150)
    Jump("Function_5_69E4")

    label("loc_69FA")

    Return()

    # Function_5_69E4 end

    def Function_6_69FB(): pass

    label("Function_6_69FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A11")
    OP_22(0x2F0, 0x0, 0x64)
    Sleep(100)
    Jump("Function_6_69FB")

    label("loc_6A11")

    Return()

    # Function_6_69FB end

    def Function_7_6A12(): pass

    label("Function_7_6A12")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A28")
    Sleep(300)
    OP_22(0x271, 0x0, 0x64)
    Jump("Function_7_6A12")

    label("loc_6A28")

    Return()

    # Function_7_6A12 end

    def Function_8_6A29(): pass

    label("Function_8_6A29")


    def lambda_6A2F():
        OP_8F(0xFE, 0x1C2, 0xFFFFFD12, 0x661C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_6A2F)
    OP_8C(0x10F, 270, 400)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 8)
    SetChrSubChip(0x10F, 0)
    WaitChrThread(0x10F, 0x1)
    Return()

    # Function_8_6A29 end

    def Function_9_6A60(): pass

    label("Function_9_6A60")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_9_6A60 end

    def Function_10_6A96(): pass

    label("Function_10_6A96")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_10_6A96 end

    def Function_11_6ACC(): pass

    label("Function_11_6ACC")

    OP_8E(0xFE, 0x168, 0xFFFFFD12, 0x5E56, 0x1770, 0x0)
    OP_8C(0xFE, 270, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_11_6ACC end

    def Function_12_6B02(): pass

    label("Function_12_6B02")

    OP_22(0x228, 0x0, 0x64)

    def lambda_6B0D():

        label("loc_6B0D")

        TurnDirection(0xFE, 0x10F, 400)
        OP_48()
        Jump("loc_6B0D")

    QueueWorkItem2(0xFE, 3, lambda_6B0D)

    def lambda_6B1E():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B1E)
    SetChrSubChip(0xFE, 2)

    def lambda_6B3D():
        OP_96(0xFE, 0xFFFFF704, 0xFFFFFD12, 0x6EF0, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B3D)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_6B02 end

    def Function_13_6B60(): pass

    label("Function_13_6B60")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B9C")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_13_6B60")

    label("loc_6B9C")

    Return()

    # Function_13_6B60 end

    def Function_14_6B9D(): pass

    label("Function_14_6B9D")

    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 2)

    def lambda_6BC4():
        OP_8F(0xFE, 0xFFFFEDB8, 0xFFFFFC18, 0x6702, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BC4)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_6BE9():
        OP_96(0xFE, 0xFFFFDF94, 0xFFFFFC18, 0x6B6C, 0x6A4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BE9)
    OP_51(0xFE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 2)
    Sleep(200)

    def lambda_6CC6():
        OP_99(0xFE, 0x3, 0x5, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6CC6)
    PlayEffect(0x0, 0x0, 0x10, 0, 100, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6D40():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6D40)
    OP_22(0x59, 0x0, 0x64)
    Sleep(100)
    OP_22(0x389, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    OP_51(0xFE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_14_6B9D end

    def Function_15_6E42(): pass

    label("Function_15_6E42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EAE")
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(2000)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(2500)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    OP_99(0x109, 0x0, 0x2, 0x5DC)
    Sleep(3000)
    Jump("Function_15_6E42")

    label("loc_6EAE")

    Return()

    # Function_15_6E42 end

    def Function_16_6EAF(): pass

    label("Function_16_6EAF")

    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 4)
    Sleep(500)
    OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xFA0)
    SetChrFlags(0x109, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 5)
    OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xFA0)
    Sleep(500)
    Return()

    # Function_16_6EAF end

    def Function_17_6EFE(): pass

    label("Function_17_6EFE")


    ChrTalk(    #167 op#A op#5
        0x109,
        "#1069F#3S#10A#11PHaaaaaah!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Return()

    # Function_17_6EFE end

    def Function_18_6F31(): pass

    label("Function_18_6F31")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp205_05.eff")
    LoadEffect(0x1, "map\\mp205_06.eff")
    OP_C4(0x0, 0x20000)
    SetChrFlags(0x11, 0x2000)
    SetChrFlags(0x12, 0x2000)
    SetChrFlags(0x13, 0x2000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 64)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 33)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(313500, 75500, -117060, 0)
    OP_67(0, -1500, -10000, 0)
    OP_6B(100, 0)
    OP_6C(0, 0)
    OP_6E(572, 0)
    OP_D0(-30140, 0)
    PlayEffect(0x0, 0x0, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 1594360, 50000, -12280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x17A, 0x1, 0x64)
    OP_22(0x85, 0x1, 0x64)
    OP_22(0x96, 0x0, 0x64)

    def lambda_70E9():

        label("loc_70E9")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_70E9")

    QueueWorkItem2(0x10, 3, lambda_70E9)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, 314130, 65000, -114660, 0)
    SetChrPos(0x12, 314130, 75500, -114660, 0)
    SetChrPos(0x13, 313030, 75000, -113700, 0)
    SetChrFlags(0x11, 0x8)
    OP_43(0x12, 0x0, 0x0, 0x17)
    FadeToBright(1000, 0)

    def lambda_7151():
        OP_6D(313080, 74500, -110560, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7151)

    def lambda_7169():
        OP_67(0, -500, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7169)

    def lambda_7181():
        OP_6B(4000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7181)

    def lambda_7191():
        OP_6E(600, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7191)
    WaitChrThread(0x12, 0x0)

    def lambda_71A6():

        label("loc_71A6")

        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        OP_48()
        Jump("loc_71A6")

    QueueWorkItem2(0x12, 1, lambda_71A6)
    OP_82(0x2, 0x2)

    def lambda_71BC():
        OP_6E(600, 2800)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_71BC)

    def lambda_71CC():
        OP_D0(-40110, 2800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_71CC)

    def lambda_71DC():
        OP_67(0, 4000, -10000, 2800)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71DC)

    def lambda_71F4():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_71F4)
    Sleep(500)

    def lambda_7209():
        OP_99(0xFE, 0x0, 0x1D, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7209)
    WaitChrThread(0x12, 0x1)

    def lambda_721E():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_721E)

    def lambda_7236():
        OP_D0(-50110, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7236)

    def lambda_7246():
        OP_99(0xFE, 0x1E, 0x20, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7246)
    WaitChrThread(0x12, 0x1)

    def lambda_725B():
        OP_8F(0xFE, 0x4BB72, 0x2710, 0xFFFE401C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_725B)

    def lambda_7276():
        OP_99(0xFE, 0x21, 0x2C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7276)
    OP_43(0x13, 0x0, 0x0, 0x19)
    WaitChrThread(0x12, 0x1)

    def lambda_7292():

        label("loc_7292")

        OP_99(0xFE, 0x39, 0x3C, 0x9C4)
        OP_48()
        Jump("loc_7292")

    QueueWorkItem2(0x12, 1, lambda_7292)

    def lambda_72A5():
        OP_6D(313080, 75500, -111560, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_72A5)

    def lambda_72BD():
        OP_6E(650, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_72BD)

    def lambda_72CD():
        OP_6B(6000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_72CD)
    Sleep(4000)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x0)
    OP_6D(1593280, 50000, 72610, 0)
    OP_67(0, -200, -10000, 0)
    OP_6B(11000, 0)
    OP_6C(180000, 0)
    OP_6E(850, 0)
    OP_D0(0, 0)
    ClearChrFlags(0x11, 0x8)
    SetChrPos(0x11, 1593370, 47100, 100140, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 45)

    def lambda_7380():

        label("loc_7380")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_7380")

    QueueWorkItem2(0x11, 0, lambda_7380)
    ClearChrFlags(0x13, 0x8)
    SetChrPos(0x13, 1592700, 46500, 184800, 0)
    SetChrFlags(0x13, 0x40)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)

    def lambda_73B8():
        OP_8F(0xFE, 0x184CB4, 0xB3B0, 0x28514, 0xF3C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_73B8)

    def lambda_73D3():
        OP_6E(924, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_73D3)

    def lambda_73E3():
        OP_D0(-25600, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_73E3)

    def lambda_73F3():
        OP_6B(8000, 10000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_73F3)

    def lambda_7403():
        OP_8F(0xFE, 0x18522C, 0xB7FC, 0x24A7C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7403)
    Sleep(2500)
    OP_43(0x13, 0x0, 0x0, 0x14)
    OP_43(0x11, 0x0, 0x0, 0x15)
    Sleep(3500)

    def lambda_7436():
        OP_8F(0xFE, 0x18522C, 0xB7FC, 0x2989C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7436)

    def lambda_7451():
        OP_6B(7000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7451)
    Sleep(1000)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_6D(305250, 30000, -6140, 0)
    OP_67(0, 9950, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(42000, 0)
    OP_6E(761, 0)
    OP_D0(10000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290520, 60000, -30450, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 48)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290520, 10000, 500, 0)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 45)
    SetChrFlags(0x13, 0x80)
    OP_82(0x1, 0x0)

    def lambda_7508():
        OP_6D(300250, 30000, -5140, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7508)

    def lambda_7520():
        OP_67(0, 17620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7520)

    def lambda_7538():
        OP_6B(4300, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7538)

    def lambda_7548():
        OP_6E(777, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7548)

    def lambda_7558():
        OP_D0(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_7558)
    OP_43(0x11, 0x0, 0x0, 0x13)

    def lambda_756F():

        label("loc_756F")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_756F")

    QueueWorkItem2(0x12, 0, lambda_756F)

    def lambda_7582():
        OP_8F(0xFE, 0x44C14, 0x2904, 0x27D8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7582)

    def lambda_759D():
        OP_8F(0xFE, 0x447C8, 0x2710, 0x251C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_759D)
    Sleep(3000)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_43(0x109, 0x1, 0x0, 0x1A)
    WaitChrThread(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_C4(0x1, 0x20000)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_6F31 end

    def Function_19_762E(): pass

    label("Function_19_762E")


    def lambda_7634():

        label("loc_7634")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_7634")

    QueueWorkItem2(0xFE, 1, lambda_7634)
    Return()

    # Function_19_762E end

    def Function_20_7642(): pass

    label("Function_20_7642")

    SetChrSubChip(0x13, 0)

    def lambda_764D():
        OP_99(0xFE, 0x0, 0x1F, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_764D)

    def lambda_765D():
        OP_8F(0xFE, 0x184BEC, 0xBC48, 0x1D4C0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_765D)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_20_7642 end

    def Function_21_7678(): pass

    label("Function_21_7678")


    def lambda_767E():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_767E)
    WaitChrThread(0xFE, 0x1)

    def lambda_7693():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7693)
    WaitChrThread(0xFE, 0x1)

    def lambda_76A8():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76A8)
    WaitChrThread(0xFE, 0x1)

    def lambda_76BD():
        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76BD)
    WaitChrThread(0xFE, 0x1)

    def lambda_76D2():
        OP_99(0xFE, 0x3C, 0x3E, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76D2)
    WaitChrThread(0xFE, 0x1)

    def lambda_76E7():
        OP_99(0xFE, 0x3D, 0x3C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76E7)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_7700():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7700)
    WaitChrThread(0xFE, 0x1)

    def lambda_7715():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7715)
    WaitChrThread(0xFE, 0x1)

    def lambda_772A():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_772A)
    WaitChrThread(0xFE, 0x1)

    def lambda_773F():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_773F)
    WaitChrThread(0xFE, 0x1)

    def lambda_7754():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7754)
    WaitChrThread(0xFE, 0x1)

    def lambda_7769():
        OP_99(0xFE, 0x42, 0x44, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7769)
    WaitChrThread(0xFE, 0x1)

    def lambda_777E():

        label("loc_777E")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_777E")

    QueueWorkItem2(0xFE, 1, lambda_777E)
    Return()

    # Function_21_7678 end

    def Function_22_778C(): pass

    label("Function_22_778C")


    def lambda_7792():
        OP_99(0xFE, 0x3C, 0x3E, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7792)
    WaitChrThread(0xFE, 0x1)

    def lambda_77A7():
        OP_99(0xFE, 0x3D, 0x3C, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77A7)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_77C0():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77C0)
    WaitChrThread(0xFE, 0x1)

    def lambda_77D5():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77D5)
    WaitChrThread(0xFE, 0x1)

    def lambda_77EA():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77EA)
    WaitChrThread(0xFE, 0x1)

    def lambda_77FF():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77FF)
    WaitChrThread(0xFE, 0x1)

    def lambda_7814():
        OP_99(0xFE, 0x41, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7814)
    WaitChrThread(0xFE, 0x1)

    def lambda_7829():
        OP_99(0xFE, 0x42, 0x44, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7829)
    WaitChrThread(0xFE, 0x1)

    def lambda_783E():

        label("loc_783E")

        OP_99(0xFE, 0x2D, 0x2F, 0x9C4)
        OP_48()
        Jump("loc_783E")

    QueueWorkItem2(0xFE, 1, lambda_783E)
    Return()

    # Function_22_778C end

    def Function_23_784C(): pass

    label("Function_23_784C")


    def lambda_7852():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7852)
    WaitChrThread(0xFE, 0x1)

    def lambda_7867():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7867)
    WaitChrThread(0xFE, 0x1)

    def lambda_787C():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_787C)
    WaitChrThread(0xFE, 0x1)

    def lambda_7891():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7891)
    WaitChrThread(0xFE, 0x1)

    def lambda_78A6():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78A6)
    WaitChrThread(0xFE, 0x1)

    def lambda_78BB():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78BB)
    WaitChrThread(0xFE, 0x1)

    def lambda_78D0():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78D0)
    WaitChrThread(0xFE, 0x1)

    def lambda_78E5():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78E5)
    WaitChrThread(0xFE, 0x1)

    def lambda_78FA():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78FA)
    WaitChrThread(0xFE, 0x1)

    def lambda_790F():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_790F)
    WaitChrThread(0xFE, 0x1)

    def lambda_7924():
        OP_99(0xFE, 0x40, 0x43, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7924)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_23_784C end

    def Function_24_7934(): pass

    label("Function_24_7934")


    def lambda_793A():
        OP_8F(0xFE, 0x4CEFA, 0xFDE8, 0xFFFDE25C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_793A)

    def lambda_7955():
        OP_99(0xFE, 0x0, 0x2C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7955)
    WaitChrThread(0xFE, 0x1)

    def lambda_796A():

        label("loc_796A")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_796A")

    QueueWorkItem2(0xFE, 1, lambda_796A)
    Return()

    # Function_24_7934 end

    def Function_25_7978(): pass

    label("Function_25_7978")

    Sleep(350)
    ClearChrFlags(0xFE, 0x80)

    def lambda_7988():
        OP_8F(0xFE, 0x4C72A, 0x186A0, 0xFFFDCED4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7988)

    def lambda_79A3():

        label("loc_79A3")

        OP_99(0xFE, 0x21, 0x3F, 0x9C4)
        OP_48()
        Jump("loc_79A3")

    QueueWorkItem2(0xFE, 1, lambda_79A3)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_25_7978 end

    def Function_26_79B6(): pass

    label("Function_26_79B6")

    OP_24(0x17A, 0x5A)
    OP_24(0x85, 0x5A)
    OP_24(0x96, 0x5A)
    Sleep(300)
    OP_24(0x17A, 0x50)
    OP_24(0x85, 0x50)
    OP_24(0x96, 0x50)
    Sleep(300)
    OP_24(0x17A, 0x46)
    OP_24(0x85, 0x46)
    OP_24(0x96, 0x46)
    Sleep(300)
    OP_24(0x17A, 0x3C)
    OP_24(0x85, 0x3C)
    OP_24(0x96, 0x3C)
    Sleep(300)
    OP_24(0x17A, 0x32)
    OP_24(0x85, 0x32)
    OP_24(0x96, 0x32)
    Sleep(300)
    OP_24(0x17A, 0x28)
    OP_24(0x85, 0x28)
    OP_24(0x96, 0x28)
    Sleep(300)
    OP_24(0x17A, 0x1E)
    OP_24(0x85, 0x1E)
    OP_24(0x96, 0x1E)
    Sleep(300)
    OP_24(0x17A, 0x14)
    OP_24(0x85, 0x14)
    OP_24(0x96, 0x14)
    Sleep(300)
    OP_24(0x17A, 0xA)
    OP_24(0x85, 0xA)
    OP_24(0x96, 0xA)
    Sleep(300)
    OP_24(0x17A, 0x0)
    OP_24(0x85, 0x0)
    OP_24(0x96, 0x0)
    OP_23(0x17A)
    OP_23(0x85)
    OP_23(0x96)
    Return()

    # Function_26_79B6 end

    def Function_27_7A65(): pass

    label("Function_27_7A65")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp205_05.eff")
    LoadEffect(0x1, "map\\mp205_06.eff")
    OP_C4(0x0, 0x20000)
    SetChrFlags(0x11, 0x2000)
    SetChrFlags(0x12, 0x2000)
    SetChrFlags(0x13, 0x2000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrFlags(0x13, 0x1000)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x12, 0x2)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 64)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 33)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(313500, 47500, -117060, 0)
    OP_67(0, -1840, -10000, 0)
    OP_6B(50, 0)
    OP_6C(0, 0)
    OP_6E(572, 0)
    OP_D0(-30140, 0)
    PlayEffect(0x0, 0x0, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 300350, -1000, 0, 0, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, 594360, 50000, -12280, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x32E, 0x1, 0x64)
    OP_22(0x85, 0x1, 0x64)
    OP_22(0x96, 0x0, 0x64)

    def lambda_7C1D():

        label("loc_7C1D")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_7C1D")

    QueueWorkItem2(0x10, 3, lambda_7C1D)
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, 314130, 65000, -114660, 0)
    SetChrPos(0x12, 314130, 47500, -114660, 0)
    SetChrPos(0x13, 314130, 48000, -114660, 0)
    OP_43(0x11, 0x0, 0x0, 0x20)
    OP_43(0x12, 0x0, 0x0, 0x1F)
    FadeToBright(1000, 0)

    def lambda_7C87():
        OP_6D(314080, 57500, -118060, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7C87)

    def lambda_7C9F():
        OP_6B(5000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7C9F)

    def lambda_7CAF():
        OP_6E(523, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7CAF)

    def lambda_7CBF():
        OP_D0(-50860, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7CBF)

    def lambda_7CCF():
        OP_67(0, 4200, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7CCF)
    Sleep(1000)
    WaitChrThread(0x12, 0x0)

    def lambda_7CF1():
        OP_67(0, 4200, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7CF1)
    OP_43(0x13, 0x0, 0x0, 0x21)

    def lambda_7D10():
        OP_99(0xFE, 0x21, 0x2C, 0xDAC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7D10)
    WaitChrThread(0x12, 0x1)

    def lambda_7D25():

        label("loc_7D25")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_7D25")

    QueueWorkItem2(0x12, 1, lambda_7D25)
    Sleep(500)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x0)
    OP_6D(593280, 50000, 72610, 0)
    OP_67(0, -200, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(180000, 0)
    OP_6E(729, 0)
    OP_D0(0, 0)
    SetChrPos(0x11, 594370, 47100, 154140, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 45)
    SetChrPos(0x13, 592370, 47300, 160140, 0)
    SetChrChipByIndex(0x13, 19)
    SetChrSubChip(0x13, 0)

    def lambda_7DF1():
        OP_6E(924, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7DF1)

    def lambda_7E01():
        OP_D0(-25600, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7E01)
    OP_43(0x11, 0x0, 0x0, 0x1E)
    OP_43(0x13, 0x0, 0x0, 0x1D)
    Sleep(700)

    def lambda_7E24():
        OP_6E(924, 500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7E24)
    Sleep(500)

    def lambda_7E39():
        OP_6B(8000, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7E39)
    Sleep(500)
    OP_82(0x2, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_6D(305250, 30000, -6140, 0)
    OP_67(0, 9950, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(42000, 0)
    OP_6E(761, 0)
    OP_D0(10000, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 290520, 60000, -30450, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 48)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 290520, 10000, 500, 0)
    SetChrChipByIndex(0x12, 17)
    SetChrSubChip(0x12, 45)
    SetChrFlags(0x13, 0x80)
    OP_82(0x1, 0x0)

    def lambda_7EF3():
        OP_6D(300250, 30000, -5140, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7EF3)

    def lambda_7F0B():
        OP_67(0, 17620, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7F0B)

    def lambda_7F23():
        OP_6B(4300, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7F23)

    def lambda_7F33():
        OP_6E(777, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_7F33)

    def lambda_7F43():
        OP_D0(3000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_7F43)
    OP_43(0x11, 0x0, 0x0, 0x1C)

    def lambda_7F5A():

        label("loc_7F5A")

        OP_99(0xFE, 0x39, 0x3C, 0xDAC)
        OP_48()
        Jump("loc_7F5A")

    QueueWorkItem2(0x12, 0, lambda_7F5A)

    def lambda_7F6D():
        OP_8F(0xFE, 0x44C14, 0x2904, 0x27D8, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7F6D)

    def lambda_7F88():
        OP_8F(0xFE, 0x447C8, 0x2710, 0x251C, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7F88)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_43(0x109, 0x1, 0x0, 0x22)
    WaitChrThread(0x109, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x12, 0x2)
    Sleep(2000)
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_C4(0x1, 0x20000)
    Sleep(3000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_7A65 end

    def Function_28_8019(): pass

    label("Function_28_8019")


    def lambda_801F():

        label("loc_801F")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_801F")

    QueueWorkItem2(0xFE, 1, lambda_801F)
    Return()

    # Function_28_8019 end

    def Function_29_802D(): pass

    label("Function_29_802D")


    def lambda_8033():
        OP_99(0xFE, 0x0, 0x1F, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8033)

    def lambda_8043():
        OP_8F(0xFE, 0x909F2, 0xBCAC, 0x1D54C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8043)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_29_802D end

    def Function_30_805E(): pass

    label("Function_30_805E")


    def lambda_8064():
        OP_99(0xFE, 0x3C, 0x3E, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8064)
    WaitChrThread(0xFE, 0x1)

    def lambda_8079():
        OP_99(0xFE, 0x3D, 0x3C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8079)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x1)

    def lambda_8092():
        OP_99(0xFE, 0x40, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8092)
    WaitChrThread(0xFE, 0x1)

    def lambda_80A7():
        OP_99(0xFE, 0x41, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80A7)
    WaitChrThread(0xFE, 0x1)

    def lambda_80BC():
        OP_99(0xFE, 0x41, 0x43, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80BC)
    WaitChrThread(0xFE, 0x1)

    def lambda_80D1():
        OP_99(0xFE, 0x42, 0x44, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80D1)
    WaitChrThread(0xFE, 0x1)

    def lambda_80E6():

        label("loc_80E6")

        OP_99(0xFE, 0x2D, 0x2F, 0xDAC)
        OP_48()
        Jump("loc_80E6")

    QueueWorkItem2(0xFE, 1, lambda_80E6)
    Return()

    # Function_30_805E end

    def Function_31_80F4(): pass

    label("Function_31_80F4")


    def lambda_80FA():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_80FA)
    WaitChrThread(0xFE, 0x1)

    def lambda_810F():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_810F)
    WaitChrThread(0xFE, 0x1)

    def lambda_8124():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8124)
    WaitChrThread(0xFE, 0x1)

    def lambda_8139():
        OP_99(0xFE, 0x6, 0x7, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8139)
    WaitChrThread(0xFE, 0x1)

    def lambda_814E():
        OP_99(0xFE, 0x8, 0x20, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_814E)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_31_80F4 end

    def Function_32_815E(): pass

    label("Function_32_815E")


    def lambda_8164():
        OP_8F(0xFE, 0x4CEFA, 0xFDE8, 0xFFFDE25C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8164)

    def lambda_817F():
        OP_99(0xFE, 0x0, 0x2C, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_817F)
    WaitChrThread(0xFE, 0x1)

    def lambda_8194():

        label("loc_8194")

        OP_99(0xFE, 0x39, 0x3B, 0xDAC)
        OP_48()
        Jump("loc_8194")

    QueueWorkItem2(0xFE, 1, lambda_8194)
    Return()

    # Function_32_815E end

    def Function_33_81A2(): pass

    label("Function_33_81A2")

    Sleep(400)
    ClearChrFlags(0xFE, 0x80)

    def lambda_81B2():
        OP_8F(0xFE, 0x4CB12, 0x186A0, 0xFFFDDA8C, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_81B2)

    def lambda_81CD():

        label("loc_81CD")

        OP_99(0xFE, 0x21, 0x3F, 0xDAC)
        OP_48()
        Jump("loc_81CD")

    QueueWorkItem2(0xFE, 1, lambda_81CD)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_33_81A2 end

    def Function_34_81E0(): pass

    label("Function_34_81E0")

    OP_24(0x32E, 0x5A)
    OP_24(0x85, 0x5A)
    OP_24(0x96, 0x5A)
    Sleep(300)
    OP_24(0x32E, 0x50)
    OP_24(0x85, 0x50)
    OP_24(0x96, 0x50)
    Sleep(300)
    OP_24(0x32E, 0x46)
    OP_24(0x85, 0x46)
    OP_24(0x96, 0x46)
    Sleep(300)
    OP_24(0x32E, 0x3C)
    OP_24(0x85, 0x3C)
    OP_24(0x96, 0x3C)
    Sleep(300)
    OP_24(0x32E, 0x32)
    OP_24(0x85, 0x32)
    OP_24(0x96, 0x32)
    Sleep(300)
    OP_24(0x32E, 0x28)
    OP_24(0x85, 0x28)
    OP_24(0x96, 0x28)
    Sleep(300)
    OP_24(0x32E, 0x1E)
    OP_24(0x85, 0x1E)
    OP_24(0x96, 0x1E)
    Sleep(300)
    OP_24(0x32E, 0x14)
    OP_24(0x85, 0x14)
    OP_24(0x96, 0x14)
    Sleep(300)
    OP_24(0x32E, 0xA)
    OP_24(0x85, 0xA)
    OP_24(0x96, 0xA)
    Sleep(300)
    OP_24(0x32E, 0x0)
    OP_24(0x85, 0x0)
    OP_24(0x96, 0x0)
    OP_23(0x32E)
    OP_23(0x85)
    OP_23(0x96)
    Return()

    # Function_34_81E0 end

    SaveToFile()

Try(main)
