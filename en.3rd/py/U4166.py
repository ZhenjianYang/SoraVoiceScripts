from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4166   ._SN',
        MapName             = 'gaiden2',
        Location            = 'U4166.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Monster 1',                            # 9
        'Monster 2',                            # 10
        'Monster 3',                            # 11
        'Monster 4',                            # 12
        'Monster 5',                            # 13
        'Monster 6',                            # 14
        'Dark Bringer',                         # 15
        'Sealing Stone 5',                      # 16
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
        'ED6_DT29/CH14500 ._CH',             # 00
        'ED6_DT29/CH14501 ._CH',             # 01
        'ED6_DT29/CH14520 ._CH',             # 02
        'ED6_DT29/CH14521 ._CH',             # 03
        'ED6_DT29/CH14450 ._CH',             # 04
        'ED6_DT29/CH14451 ._CH',             # 05
        'ED6_DT29/CH14510 ._CH',             # 06
        'ED6_DT29/CH14511 ._CH',             # 07
        'ED6_DT26/CH20621 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT29/CH14500P._CP',             # 00
        'ED6_DT29/CH14501P._CP',             # 01
        'ED6_DT29/CH14520P._CP',             # 02
        'ED6_DT29/CH14521P._CP',             # 03
        'ED6_DT29/CH14450P._CP',             # 04
        'ED6_DT29/CH14451P._CP',             # 05
        'ED6_DT29/CH14510P._CP',             # 06
        'ED6_DT29/CH14511P._CP',             # 07
        'ED6_DT26/CH20621P._CP',             # 08
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_214",          # 01, 1
        "Function_2_235",          # 02, 2
        "Function_3_242",          # 03, 3
        "Function_4_F05",          # 04, 4
        "Function_5_F2D",          # 05, 5
        "Function_6_F90",          # 06, 6
        "Function_7_FF3",          # 07, 7
        "Function_8_1056",         # 08, 8
        "Function_9_10B9",         # 09, 9
        "Function_10_111C",        # 0A, 10
        "Function_11_117F",        # 0B, 11
        "Function_12_11E2",        # 0C, 12
        "Function_13_1245",        # 0D, 13
        "Function_14_1284",        # 0E, 14
        "Function_15_12C3",        # 0F, 15
        "Function_16_1302",        # 10, 16
        "Function_17_1341",        # 11, 17
        "Function_18_1BA8",        # 12, 18
        "Function_19_1C02",        # 13, 19
        "Function_20_2542",        # 14, 20
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_213")

    Return()

    # Function_0_1F2 end

    def Function_1_214(): pass

    label("Function_1_214")

    OP_B1("U4166_1")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_1C(0x1, 0x0, 0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_234")
    ClearMapFlags(0x10)

    label("loc_234")

    Return()

    # Function_1_214 end

    def Function_2_235(): pass

    label("Function_2_235")

    Call(0, 3)
    Call(0, 17)
    Call(0, 19)
    Return()

    # Function_2_235 end

    def Function_3_242(): pass

    label("Function_3_242")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    SetChrPos(0x109, 800, 120, 10870, 180)
    SetChrPos(0x10F, 2040, 120, 10870, 180)
    SetChrPos(0xF0, 800, 120, 10870, 180)
    SetChrPos(0xF1, 2040, 120, 10870, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(18700, 3000, -6450, 0)
    OP_67(0, 2340, -10000, 0)
    OP_6B(3570, 0)
    OP_6C(90000, 0)
    OP_6E(520, 0)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    FadeToBright(2000, 0)

    def lambda_357():
        OP_6D(9200, -5400, 950, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_357)

    def lambda_36F():
        OP_67(0, 7700, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_36F)

    def lambda_387():
        OP_6B(4270, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_387)

    def lambda_397():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_397)

    def lambda_3A7():
        OP_6E(665, 7000)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_3A7)
    WaitChrThread(0x109, 0x2)
    Fade(500)
    OP_6D(2060, 150, 9820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0xD)
    Sleep(500)
    OP_43(0x10F, 0x0, 0x0, 0xE)
    Sleep(400)
    OP_43(0xF0, 0x0, 0x0, 0xF)
    Sleep(600)
    OP_43(0xF1, 0x0, 0x0, 0x10)
    Sleep(500)

    def lambda_445():
        OP_6D(1780, 0, -500, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_445)

    def lambda_45D():
        OP_67(0, 7170, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_45D)

    def lambda_475():
        OP_6B(2490, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_475)

    def lambda_485():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_485)

    def lambda_495():
        OP_6E(318, 5500)
        ExitThread()

    QueueWorkItem(0xF0, 2, lambda_495)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    ChrTalk(    #0
        0x109,
        (
            "#1060F#5PWell, we made it to the arena.\x02\x03",

            "#1066FHeh. This is where some enemies show up\x01",
            "outta nowhere for us to fight, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(300)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(3850, -1800, -8490, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(132000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -50, 0, -1860, 180)
    SetChrPos(0x10F, 1780, 0, -1830, 135)
    SetChrPos(0xF0, -190, 0, -250, 270)
    SetChrPos(0xF1, 2210, 0, -220, 45)
    OP_0D()
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 740, 0, -10010, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -1320, 0, -11740, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 3110, 0, -11950, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, 980, 0, -14000, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, 740, -3000, -10010, 0)
    SetChrPos(0x11, -1320, -3000, -11740, 0)
    SetChrPos(0x12, 3110, -3000, -11950, 0)
    SetChrPos(0x13, 980, -3000, -14000, 0)
    SetChrChipByIndex(0x10, 0)
    SetChrChipByIndex(0x11, 4)
    SetChrChipByIndex(0x12, 4)
    SetChrChipByIndex(0x13, 0)
    OP_22(0x85, 0x1, 0x5A)
    OP_43(0x10, 0x0, 0x0, 0x5)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x12, 0x0, 0x0, 0x7)
    OP_43(0x13, 0x0, 0x0, 0x8)

    def lambda_76C():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_76C)
    Sleep(100)

    def lambda_77F():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_77F)
    Sleep(100)
    OP_8C(0xF0, 180, 600)
    OP_21()
    OP_1D(0x97)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85D")

    label("loc_7F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85D")

    label("loc_81E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_846")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_85D")

    label("loc_846")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_85D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8F1")

    label("loc_88A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B2")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8F1")

    label("loc_8B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8F1")

    label("loc_8DA")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8F1")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_23(0x85)

    ChrTalk(    #1
        0x109,
        "#1064F#6PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        "#1801F#5P...Now look what you've done.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #3
        0x109,
        (
            "#1068F#6PIt's just a coincidence, I swear!\x02\x03",

            "#1069FMe and my big mouth... I feel like I've just\x01",
            "been set up or something!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A60")

    ChrTalk(    #4
        0x107,
        "#065F#6PE-Eeek...\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_A60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB6")

    ChrTalk(    #5
        0x10B,
        (
            "#216F#6PWh-Who cares why they're here?!\x01",
            "We've gotta fight them!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF7")

    label("loc_AB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF7")

    ChrTalk(    #6
        0x10E,
        "#172F#6PAssigning blame can wait until later!\x02",
    )

    CloseMessageWindow()

    label("loc_AF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #7
        0x10D,
        "#271F#6PHere they come!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B87")

    label("loc_B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5C")

    ChrTalk(    #8
        0x10E,
        "#177F#6PThey're going to attack!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B87")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B87")

    ChrTalk(    #9
        0x10B,
        "#214F#6PHere they come!\x02",
    )

    CloseMessageWindow()

    label("loc_B87")

    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    Sleep(300)
    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x97)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    OP_6D(3850, -1800, -8490, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(132000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -50, 0, -1860, 180)
    SetChrPos(0x10F, 1780, 0, -1830, 180)
    SetChrPos(0xF0, -190, 0, -250, 180)
    SetChrPos(0xF1, 2210, 0, -220, 180)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, 740, -3000, -10010, 0)
    SetChrPos(0x11, -2020, -3000, -11740, 0)
    SetChrPos(0x12, 3810, -3000, -11950, 0)
    SetChrPos(0x13, 980, -3000, -14500, 0)
    SetChrChipByIndex(0x10, 6)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 6)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 740, 0, -10010, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -2020, 0, -11740, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 3810, 0, -11950, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, 980, 0, -14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_22(0x85, 0x1, 0x5A)
    OP_43(0x10, 0x0, 0x0, 0x9)
    OP_43(0x11, 0x0, 0x0, 0xA)
    OP_43(0x12, 0x0, 0x0, 0xB)
    OP_43(0x13, 0x0, 0x0, 0xC)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    OP_23(0x85)

    ChrTalk(    #10
        0x109,
        "#1063F#6PUgh... More?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        "#1443F#6PWe'll defeat as many as we have to!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_242 end

    def Function_4_F05(): pass

    label("Function_4_F05")


    def lambda_F0B():

        label("loc_F0B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F0B")

    QueueWorkItem2(0xFE, 1, lambda_F0B)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x5DC, 0x0)
    Return()

    # Function_4_F05 end

    def Function_5_F2D(): pass

    label("Function_5_F2D")

    PlayEffect(0x1, 0x4, 0xFF, 740, 0, -10010, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_F68():

        label("loc_F68")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F68")

    QueueWorkItem2(0xFE, 1, lambda_F68)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    Return()

    # Function_5_F2D end

    def Function_6_F90(): pass

    label("Function_6_F90")

    PlayEffect(0x1, 0x5, 0xFF, -1320, 0, -11740, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_FCB():

        label("loc_FCB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FCB")

    QueueWorkItem2(0xFE, 1, lambda_FCB)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_6_F90 end

    def Function_7_FF3(): pass

    label("Function_7_FF3")

    PlayEffect(0x1, 0x6, 0xFF, 3110, 0, -11950, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_102E():

        label("loc_102E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_102E")

    QueueWorkItem2(0xFE, 1, lambda_102E)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    Return()

    # Function_7_FF3 end

    def Function_8_1056(): pass

    label("Function_8_1056")

    PlayEffect(0x1, 0x7, 0xFF, 980, 0, -14000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1091():

        label("loc_1091")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1091")

    QueueWorkItem2(0xFE, 1, lambda_1091)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_8_1056 end

    def Function_9_10B9(): pass

    label("Function_9_10B9")

    PlayEffect(0x1, 0x4, 0xFF, 740, 0, -10010, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_10F4():

        label("loc_10F4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_10F4")

    QueueWorkItem2(0xFE, 1, lambda_10F4)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    Return()

    # Function_9_10B9 end

    def Function_10_111C(): pass

    label("Function_10_111C")

    PlayEffect(0x1, 0x5, 0xFF, -2020, 0, -11740, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1157():

        label("loc_1157")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1157")

    QueueWorkItem2(0xFE, 1, lambda_1157)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_10_111C end

    def Function_11_117F(): pass

    label("Function_11_117F")

    PlayEffect(0x1, 0x6, 0xFF, 3810, 0, -11950, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_11BA():

        label("loc_11BA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_11BA")

    QueueWorkItem2(0xFE, 1, lambda_11BA)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    Return()

    # Function_11_117F end

    def Function_12_11E2(): pass

    label("Function_12_11E2")

    PlayEffect(0x1, 0x7, 0xFF, 980, 0, -14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_121D():

        label("loc_121D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_121D")

    QueueWorkItem2(0xFE, 1, lambda_121D)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_12_11E2 end

    def Function_13_1245(): pass

    label("Function_13_1245")


    def lambda_124B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_124B)
    OP_8E(0xFE, 0x12C, 0x0, 0xFFFFF920, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_13_1245 end

    def Function_14_1284(): pass

    label("Function_14_1284")


    def lambda_128A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_128A)
    OP_8E(0xFE, 0x6F4, 0x0, 0xFFFFF93E, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_1284 end

    def Function_15_12C3(): pass

    label("Function_15_12C3")


    def lambda_12C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12C9)
    OP_8E(0xFE, 0xFFFFFF42, 0x0, 0xFFFFFF06, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_12C3 end

    def Function_16_1302(): pass

    label("Function_16_1302")


    def lambda_1308():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1308)
    OP_8E(0xFE, 0x8A2, 0x0, 0xFFFFFF24, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_16_1302 end

    def Function_17_1341(): pass

    label("Function_17_1341")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    LoadEffect(0x0, "map\\mp251_00.eff")
    LoadEffect(0x1, "map\\mp251_01.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    OP_6D(3850, -1800, -8490, 0)
    OP_67(0, 5490, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(132000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -50, 0, -1860, 180)
    SetChrPos(0x10F, 1780, 0, -1830, 180)
    SetChrPos(0xF0, -190, 0, -250, 180)
    SetChrPos(0xF1, 2210, 0, -220, 180)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 870, -8000, -12290, 0)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_A1(0x16, 0x7)
    OP_71(0x2007, 0x0)
    ExitThread()
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x10)
    SetChrFlags(0x16, 0x1)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 870, 0, -12290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #12
        0x109,
        (
            "#1069F#6PBah... How many of these fights are\x01",
            "we gonna have to do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1441F#6POur next foe seems to be quite large,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)

    def lambda_15AE():

        label("loc_15AE")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_15AE")

    QueueWorkItem2(0x10F, 0, lambda_15AE)
    OP_22(0x85, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 870, 0, -12290, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(500)
    OP_6D(940, 0, -12000, 0)
    OP_67(0, 14280, -10000, 0)
    OP_6B(2090, 0)
    OP_6C(180000, 0)
    OP_6E(410, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_0D()

    def lambda_165F():
        OP_6D(940, 2100, -14340, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_165F)

    def lambda_1677():
        OP_67(0, 1790, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1677)

    def lambda_168F():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_168F)

    def lambda_169F():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_169F)

    def lambda_16AF():
        OP_6E(455, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_16AF)

    def lambda_16BF():
        OP_91(0xFE, 0x0, 0x1F40, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_16BF)
    WaitChrThread(0x16, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_44(0x10F, 0x0)
    OP_23(0x85)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x2)
    Fade(500)
    OP_6D(1420, 1350, -6780, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(134000, 0)
    OP_6E(472, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A7")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_180E")

    label("loc_17A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17CF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_180E")

    label("loc_17CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_180E")

    label("loc_17F7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_180E")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18A2")

    label("loc_183B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1863")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18A2")

    label("loc_1863")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18A2")

    label("loc_188B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18A2")

    Sleep(1000)

    ChrTalk(    #14
        0x10F,
        "#1444F#5PWh-What in...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18ED")

    ChrTalk(    #15
        0x10B,
        "#216F#5PTh-The hell?!\x02",
    )

    CloseMessageWindow()

    label("loc_18ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(    #16
        0x107,
        "#065F#5PI-Is that a mechanical horse?\x02",
    )

    CloseMessageWindow()
    Jump("loc_199C")

    label("loc_1929")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1964")

    ChrTalk(    #17
        0x10E,
        "#173F#5PIs that an armored horseman?\x02",
    )

    CloseMessageWindow()
    Jump("loc_199C")

    label("loc_1964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_199C")

    ChrTalk(    #18
        0x10D,
        "#271F#5PIs that an armored horseman?\x02",
    )

    CloseMessageWindow()

    label("loc_199C")


    ChrTalk(    #19
        0x109,
        (
            "#1065F#5PSeems to be just like the one Estelle's\x01",
            "crew beat under Jenis.\x02\x03",

            "#1069FAnd not to jinx us, but this is probably\x01",
            "going to be the last one!\x02\x03",

            "So let's finish this!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1A55():
        OP_6D(370, 2720, -3670, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A55)

    def lambda_1A6D():
        OP_67(0, 7800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A6D)

    def lambda_1A85():
        OP_6B(2100, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A85)

    def lambda_1A95():
        OP_6C(127000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1A95)

    def lambda_1AA5():
        OP_6E(430, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1AA5)

    def lambda_1AB5():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1AB5)
    OP_D8(0x7, 0x3E8)
    OP_B0(0x7, 0xD)
    OP_6F(0x7, 251)
    OP_70(0x7, 0x10A)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x16, 0x1)

    def lambda_1AFF():
        OP_67(0, 5800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AFF)
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_D8(0x7, 0x3E8)
    OP_B0(0x7, 0x8)
    OP_6F(0x7, 81)
    OP_70(0x7, 0x61)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(1700)

    def lambda_1B3D():
        OP_6D(1140, 1650, -3820, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B3D)

    def lambda_1B55():
        OP_67(0, 5000, -10000, 200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1B55)

    def lambda_1B6D():
        OP_6B(1800, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1B6D)

    def lambda_1B7D():
        OP_6E(380, 200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1B7D)
    OP_73(0x7)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_1341 end

    def Function_18_1BA8(): pass

    label("Function_18_1BA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C01")
    OP_24(0xEC, 0x32)
    OP_B0(0x7, 0xD)
    OP_6F(0x7, 251)
    OP_70(0x7, 0x10A)

    def lambda_1BCD():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1BCD)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x16, 0x1)
    OP_73(0x7)
    Jump("Function_18_1BA8")

    label("loc_1C01")

    Return()

    # Function_18_1BA8 end

    def Function_19_1C02(): pass

    label("Function_19_1C02")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp251_00.eff")
    LoadEffect(0x1, "map\\mp251_01.eff")
    LoadEffect(0x2, "map\\mp253_00.eff")
    LoadEffect(0x3, "map\\mp253_01.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    OP_6D(1220, 1000, -15610, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(180000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -50, 0, -1860, 180)
    SetChrPos(0x10F, 1780, 0, -1830, 180)
    SetChrPos(0xF0, -190, 0, -250, 180)
    SetChrPos(0xF1, 2210, 0, -220, 180)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 10)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 870, 0, -12290, 0)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_A1(0x16, 0x7)
    OP_71(0x2007, 0x0)
    ExitThread()
    OP_B0(0x7, 0xF)
    OP_6F(0x7, 1)
    OP_70(0x7, 0x10)
    SetChrFlags(0x16, 0x1)
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_D8(0x7, 0x1F4)
    OP_B0(0x7, 0xA)
    OP_6F(0x7, 120)
    OP_70(0x7, 0xA0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1DB6():
        OP_67(0, 4230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DB6)

    def lambda_1DCE():
        OP_6D(1220, 0, -13610, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1DCE)
    Sleep(1000)
    OP_7C(0x0, 0x64, 0x1388, 0x12C)
    OP_22(0xEC, 0x0, 0x64)
    OP_22(0x15A, 0x0, 0x64)
    Sleep(500)
    Sleep(300)
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 870, 100, -12290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    def lambda_1E5A():

        label("loc_1E5A")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1E5A")

    QueueWorkItem2(0x10F, 0, lambda_1E5A)
    OP_22(0x85, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 870, 100, -12290, 0, 0, 0, 1600, 1600, 1600, 0xFF, 0, 0, 0, 0)

    def lambda_1EAF():
        OP_91(0xFE, 0x0, 0xFFFFEC78, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1EAF)
    WaitChrThread(0x16, 0x0)
    OP_44(0x10F, 0x0)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    ClearChrFlags(0x17, 0x80)
    OP_9F(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x17, 870, 1200, -12290, 0)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x2, 0x2, 0x17, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x17, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(    #20
        0x109,
        "#1078F#5PWoo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1444F#5PIt left behind a stone.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(3850, -1500, -8490, 0)
    OP_67(0, 8220, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(135000, 0)
    OP_6E(450, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    OP_0D()
    Sleep(300)

    def lambda_2034():
        OP_6D(1280, 0, -11070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2034)

    def lambda_204C():
        OP_67(0, 6490, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_204C)

    def lambda_2064():
        OP_6B(2180, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_2064)

    def lambda_2074():
        OP_6E(382, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2074)

    def lambda_2084():
        OP_8E(0xFE, 0x33E, 0x0, 0xFFFFD526, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2084)
    Sleep(450)

    def lambda_20A4():
        OP_8E(0xFE, 0x28A, 0x0, 0xFFFFDB52, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_20A4)
    Sleep(150)

    def lambda_20C4():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0xFFFFE1D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_20C4)
    Sleep(150)

    def lambda_20E4():
        OP_8E(0xFE, 0x514, 0x0, 0xFFFFE0B6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_20E4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Fade(250)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x17, 0x2EE, 0x4B0, 0xFFFFD314, 0x1F4, 0x0)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Found \x1F\x56\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x356, 1)

    ChrTalk(    #23
        0x10F,
        "#1442F#5PIs this our prize for winning?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1840F#5PHaha. Only the best for the champions.\x02\x03",

            "#1075FWhoever set this up sure put a lot of\x01",
            "effort into making it feel like a proper\x01",
            "tournament.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2281")

    ChrTalk(    #25
        0x10D,
        "#272FHmph. How dedicated of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2309")

    label("loc_2281")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B9")

    ChrTalk(    #26
        0x10E,
        "#176FHow very particular of them.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2309")

    label("loc_22B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2309")

    ChrTalk(    #27
        0x10B,
        (
            "#413FThey must have a whole lot of free\x01",
            "time on their hands.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2309")

    Fade(500)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    SetChrFlags(0x17, 0x80)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #28
        0x109,
        (
            "#1060F#2PWell, congrats, gang. We've found our\x01",
            "fifth sealing stone.\x02\x03",

            "Let's head back and see who's inside.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D4")

    ChrTalk(    #29
        0x107,
        "#560F#6PRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_23D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FA")

    ChrTalk(    #30
        0x10E,
        "#170F#6PIndeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2421")

    label("loc_23FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2421")

    ChrTalk(    #31
        0x10D,
        "#277F#6PUnderstood.\x02",
    )

    CloseMessageWindow()

    label("loc_2421")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2484")

    ChrTalk(    #32
        0x10B,
        (
            "#210F#6PIt's hard to believe there's seriously someone\x01",
            "in that thing, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2484")

    OP_A2(0x2713)
    OP_28(0x2C, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(990, 0, -9290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0xEE, 990, 0, -9290, 0)
    SetChrPos(0xEF, 990, 0, -9290, 0)
    SetChrPos(0xF0, 990, 0, -9290, 0)
    SetChrPos(0xF1, 990, 0, -9290, 0)
    OP_69(0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_A2(0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_19_1C02 end

    def Function_20_2542(): pass

    label("Function_20_2542")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_20_2542 end

    SaveToFile()

Try(main)
