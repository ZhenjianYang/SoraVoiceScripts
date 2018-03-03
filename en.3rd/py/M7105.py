from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7105   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60222",
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
        'Death Slugger',                        # 9
        'Death Slugger',                        # 10
        'Death Slugger',                        # 11
        'Death Slugger',                        # 12
        'Death Slugger',                        # 13
        'Kevin',                                # 14
        'Sealing Stone 8',                      # 15
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
        'ED6_DT29/CH14120 ._CH',             # 00
        'ED6_DT29/CH14120 ._CH',             # 01
        'ED6_DT27/CH04080 ._CH',             # 02
        'ED6_DT27/CH04081 ._CH',             # 03
        'ED6_DT27/CH04085 ._CH',             # 04
        'ED6_DT27/CH03154 ._CH',             # 05
        'ED6_DT26/CH20668 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH14120P._CP',             # 00
        'ED6_DT29/CH14120P._CP',             # 01
        'ED6_DT27/CH04080P._CP',             # 02
        'ED6_DT27/CH04081P._CP',             # 03
        'ED6_DT27/CH04085P._CP',             # 04
        'ED6_DT27/CH03154P._CP',             # 05
        'ED6_DT26/CH20668P._CP',             # 06
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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


    DeclEvent(
        X                   = -8600,
        Y                   = 7000,
        Z                   = 52220,
        Range               = 8189,
        Unknown_10          = 0x2AF8,
        Unknown_14          = 0xDB60,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_1E3",          # 01, 1
        "Function_2_210",          # 02, 2
        "Function_3_221",          # 03, 3
        "Function_4_139D",         # 04, 4
        "Function_5_13F7",         # 05, 5
        "Function_6_1457",         # 06, 6
        "Function_7_14B7",         # 07, 7
        "Function_8_1517",         # 08, 8
        "Function_9_1577",         # 09, 9
        "Function_10_15D7",        # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Return()

    # Function_0_1E2 end

    def Function_1_1E3(): pass

    label("Function_1_1E3")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF1D70, 0x230088)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_20F")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 120)

    label("loc_20F")

    Return()

    # Function_1_1E3 end

    def Function_2_210(): pass

    label("Function_2_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x501, 2)), scpexpr(EXPR_END)), "loc_218")
    Return()

    label("loc_218")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_210 end

    def Function_3_221(): pass

    label("Function_3_221")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(242, 0x47, 0x2)
    OP_E0(243, 0x48, 0x2)
    OP_E0(244, 0x49, 0x2)
    OP_E0(245, 0x4A, 0x2)
    Fade(1000)
    OP_6D(1650, 10000, 76160, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(57000, 0)
    OP_6E(382, 0)

    def lambda_2BB():
        OP_6D(1650, 10000, 66310, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2BB)

    def lambda_2D3():
        OP_67(0, 8850, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xF3, 0, lambda_2D3)

    def lambda_2EB():
        OP_6B(6140, 6000)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2EB)

    def lambda_2FB():
        OP_6E(382, 6000)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2FB)
    SetChrPos(0x10F, 0, 8000, 54580, 0)
    SetChrPos(0xF3, 330, 8000, 53450, 0)
    SetChrPos(0xF4, -1200, 8000, 52990, 0)
    SetChrPos(0xF5, -220, 8000, 51620, 0)
    Sleep(1000)

    def lambda_354():
        OP_8E(0xFE, 0x0, 0x1F72, 0x1022A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_354)
    Sleep(50)

    def lambda_374():
        OP_8E(0xFE, 0x4B0, 0x1F72, 0xFEB9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_374)
    Sleep(150)

    def lambda_394():
        OP_8E(0xFE, 0xFFFFFAEC, 0x1F72, 0xFC8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_394)
    Sleep(50)

    def lambda_3B4():
        OP_8E(0xFE, 0xFFFFFF42, 0x1F72, 0xF898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3B4)
    WaitChrThread(0x10F, 0x0)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    OP_0D()
    WaitChrThread(0x10F, 0x1)
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_43D():
        OP_6D(910, 11600, 106980, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_43D)

    def lambda_455():
        OP_67(0, 2670, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_455)

    def lambda_46D():
        OP_6B(4580, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_46D)

    def lambda_47D():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_47D)

    def lambda_48D():
        OP_6E(276, 4000)
        ExitThread()

    QueueWorkItem(0xF3, 1, lambda_48D)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        "#1444F#1POh!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 5930, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53F")

    ChrTalk(    #1
        0x10D,
        "#277F#6PCould that be the exit, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_53F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57E")

    ChrTalk(    #2
        0x10E,
        "#170F#6PCould that be the exit, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_57E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C2")

    ChrTalk(    #3
        0x105,
        "#1382F#6PDo you think that could be the exit?\x02",
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_5C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_603")

    ChrTalk(    #4
        0x102,
        "#1500FThat looks like it must be the exit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_603")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_640")

    ChrTalk(    #5
        0x107,
        "#560FDo you think that could be the exit?\x02",
    )

    CloseMessageWindow()

    label("loc_640")


    ChrTalk(    #6
        0x10F,
        (
            "#1447F#5PIt certainly seems to be.\x02\x03",

            "#1448FI wonder if Kevin and his group are\x01",
            "on the other side already.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_20(0x3E8)
    OP_6D(680, 8050, 70000, 0)
    OP_67(0, 6020, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(45000, 0)
    OP_6E(258, 0)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75D")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C4")

    label("loc_75D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C4")

    label("loc_785")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_7C4")

    label("loc_7AD")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_7C4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_858")

    label("loc_7F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_858")

    label("loc_819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_841")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_858")

    label("loc_841")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_858")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8EC")

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AD")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8EC")

    label("loc_8AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D5")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8EC")

    label("loc_8D5")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8EC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_980")

    label("loc_919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_941")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_980")

    label("loc_941")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_980")

    label("loc_969")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_980")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF3, 8)
    SetChrSubChip(0xF3, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF4, 9)
    SetChrSubChip(0xF4, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF5, 10)
    SetChrSubChip(0xF5, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #7
        0x10F,
        "#1441F#6P...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A52")
    OP_A2(0x3)

    ChrTalk(    #8
        0x10B,
        (
            "#212F#6PHeh. Looks like they're not gonna let us\x01",
            "reach it without a fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_A52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB1")
    OP_A2(0x0)

    ChrTalk(    #9
        0x107,
        (
            "#062F#6PI think we're going to have to fight\x01",
            "our way to it, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B15")
    OP_A2(0x4)

    ChrTalk(    #10
        0x102,
        (
            "#1502F#6PIt looks like we're going to have to fight\x01",
            "our way to it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_B15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B85")
    OP_A2(0x5)

    ChrTalk(    #11
        0x105,
        (
            "#1162F#6PI think we'll have another battle ahead\x01",
            "of us before we can reach it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_B85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF0")
    OP_A2(0x1)

    ChrTalk(    #12
        0x10E,
        (
            "#178F#6PIt seems we have another battle ahead\x01",
            "of us before we can reach it, however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF0")

    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)

    def lambda_BFD():

        label("loc_BFD")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_BFD")

    QueueWorkItem2(0xF3, 0, lambda_BFD)

    def lambda_C18():
        OP_6D(1200, 8050, 71600, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_C18)

    def lambda_C30():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_C30)

    def lambda_C48():
        OP_6B(3510, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_C48)

    def lambda_C58():
        OP_6E(258, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_C58)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 0, 5050, 73750, 180)
    OP_43(0x15, 0x0, 0x0, 0x4)
    WaitChrThread(0x15, 0x0)
    OP_44(0xF3, 0x0)
    OP_23(0x85)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBD")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D24")

    label("loc_CBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE5")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D24")

    label("loc_CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0D")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D24")

    label("loc_D0D")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D24")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D51")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DB8")

    label("loc_D51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D79")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DB8")

    label("loc_D79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA1")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DB8")

    label("loc_DA1")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DB8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E4C")

    label("loc_DE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0D")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E4C")

    label("loc_E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E35")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E4C")

    label("loc_E35")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E4C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E79")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EE0")

    label("loc_E79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA1")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EE0")

    label("loc_EA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC9")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EE0")

    label("loc_EC9")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EE0")

    Sleep(1000)

    ChrTalk(    #13
        0x10F,
        "#1444F#6P...What?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F29")

    ChrTalk(    #14
        0x107,
        "#065F#6PK-Kevin?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB4")

    label("loc_F29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5D")

    ChrTalk(    #15
        0x10E,
        "#173F#6PF-Father Kevin?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB4")

    label("loc_F5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F89")

    ChrTalk(    #16
        0x102,
        "#1504F#6PKevin?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB4")

    label("loc_F89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB4")

    ChrTalk(    #17
        0x105,
        "#1164F#6PK-Kevin?!\x02",
    )

    CloseMessageWindow()

    label("loc_FB4")


    ChrTalk(    #18
        0x15,
        "#1842F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 4)
    SetChrSubChip(0x15, 0)

    def lambda_FE5():

        label("loc_FE5")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_FE5")

    QueueWorkItem2(0x15, 2, lambda_FE5)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 0, 8050, 73750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 0, 8050, 77000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, -2200, 8050, 75500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, 2200, 8050, 75500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -4500, 8050, 74000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0xFF, 4500, 8050, 74000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(0, 8800, 69800, 0)
    OP_67(0, 4019, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(0, 0)
    OP_6E(254, 0)
    SetChrPos(0x10F, 0, 8050, 66090, 0)
    SetChrPos(0xF3, 1200, 8050, 65209, 0)
    SetChrPos(0xF4, -1300, 8050, 64650, 0)
    SetChrPos(0xF5, 0, 8050, 63640, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1207():

        label("loc_1207")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1207")

    QueueWorkItem2(0xF3, 0, lambda_1207)

    def lambda_1222():
        OP_6D(0, 8800, 70100, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1222)

    def lambda_123A():
        OP_67(0, 2310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_123A)

    def lambda_1252():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1252)

    def lambda_1262():
        OP_6E(230, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1262)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, 0, 5050, 77000, 180)
    SetChrPos(0x11, -2200, 5050, 75500, 180)
    SetChrPos(0x12, 2200, 5050, 75500, 180)
    SetChrPos(0x13, -4500, 5050, 74000, 180)
    SetChrPos(0x14, 4500, 5050, 74000, 180)
    OP_43(0x10, 0x0, 0x0, 0x5)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x12, 0x0, 0x0, 0x7)
    OP_43(0x13, 0x0, 0x0, 0x8)
    OP_43(0x14, 0x0, 0x0, 0x9)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x0, 0x2)
    WaitChrThread(0x10F, 0x0)
    OP_44(0xF3, 0x0)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x15, 2)
    SetChrSubChip(0x15, 0)
    OP_44(0x15, 0x2)
    OP_0D()
    Sleep(800)

    ChrTalk(    #19
        0x10F,
        "#1449F#6P#3SKevin!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Battle(0x13C, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_221 end

    def Function_4_139D(): pass

    label("Function_4_139D")

    SetChrFlags(0xFE, 0x20)
    PlayEffect(0x1, 0x4, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_139D end

    def Function_5_13F7(): pass

    label("Function_5_13F7")

    PlayEffect(0x1, 0xFF, 0xFF, 0, 8050, 77000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1432():

        label("loc_1432")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1432")

    QueueWorkItem2(0xFE, 1, lambda_1432)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x1, 0x2)
    Return()

    # Function_5_13F7 end

    def Function_6_1457(): pass

    label("Function_6_1457")

    PlayEffect(0x1, 0xFF, 0xFF, -2200, 8150, 75500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1492():

        label("loc_1492")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1492")

    QueueWorkItem2(0xFE, 1, lambda_1492)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x2, 0x2)
    Return()

    # Function_6_1457 end

    def Function_7_14B7(): pass

    label("Function_7_14B7")

    PlayEffect(0x1, 0xFF, 0xFF, 2200, 8150, 75500, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14F2():

        label("loc_14F2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14F2")

    QueueWorkItem2(0xFE, 1, lambda_14F2)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x3, 0x2)
    Return()

    # Function_7_14B7 end

    def Function_8_1517(): pass

    label("Function_8_1517")

    PlayEffect(0x1, 0xFF, 0xFF, -4500, 8050, 74000, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1552():

        label("loc_1552")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1552")

    QueueWorkItem2(0xFE, 1, lambda_1552)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x4, 0x2)
    Return()

    # Function_8_1517 end

    def Function_9_1577(): pass

    label("Function_9_1577")

    PlayEffect(0x1, 0xFF, 0xFF, 4500, 8050, 74000, 1, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_15B2():

        label("loc_15B2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_15B2")

    QueueWorkItem2(0xFE, 1, lambda_15B2)
    OP_91(0xFE, 0x0, 0xDAC, 0x0, 0x320, 0x0)
    OP_82(0x5, 0x2)
    Return()

    # Function_9_1577 end

    def Function_10_15D7(): pass

    label("Function_10_15D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    OP_E0(242, 0x47, 0x2)
    OP_E0(243, 0x48, 0x2)
    OP_E0(244, 0x49, 0x2)
    OP_E0(245, 0x4A, 0x2)
    SetChrPos(0x10F, -240, 8050, 67870, 0)
    SetChrPos(0xF3, 1330, 8050, 66380, 0)
    SetChrPos(0xF4, -1330, 8050, 66880, 0)
    SetChrPos(0xF5, 40, 8050, 65430, 0)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0xF3, 8)
    SetChrSubChip(0xF3, 0)
    SetChrChipByIndex(0xF4, 9)
    SetChrSubChip(0xF4, 0)
    SetChrChipByIndex(0xF5, 10)
    SetChrSubChip(0xF5, 0)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_6D(1220, 8050, 65800, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(135000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x16, 0x80)
    OP_9F(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x16, -260, 9300, 69960, 0)
    PlayEffect(0x1, 0x7, 0x16, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x16, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C8")
    OP_62(0xF2, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_182F")

    label("loc_17C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_182F")

    label("loc_17F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF2)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1818")
    OP_62(0xF2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_182F")

    label("loc_1818")

    OP_62(0xF2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_182F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185C")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18C3")

    label("loc_185C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1884")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18C3")

    label("loc_1884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AC")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18C3")

    label("loc_18AC")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18C3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F0")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1957")

    label("loc_18F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1918")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1957")

    label("loc_1918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1957")

    label("loc_1940")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1957")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1984")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19EB")

    label("loc_1984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AC")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19EB")

    label("loc_19AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D4")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19EB")

    label("loc_19D4")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19EB")

    Sleep(1000)

    ChrTalk(    #20
        0x10F,
        "#1444F#5POh...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    def lambda_1A60():
        OP_6D(1130, 8050, 67300, 1500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1A60)
    OP_8E(0x10F, 0xFFFFFEE8, 0x1F72, 0x10CFC, 0x3E8, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x10F, 6)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x16, 0x64, 0x238C, 0x10E5A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x16, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05Found \x1F\x59\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x359, 1)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6C, 0x0, 0x64)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x19)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    Sleep(500)
    Fade(500)
    OP_6D(910, 11600, 106980, 0)
    OP_67(0, 2670, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(276, 0)

    def lambda_1B98():
        OP_6B(4600, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1B98)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    WaitChrThread(0x10F, 0x0)
    SetChrPos(0x10F, -360, 8050, 68500, 0)
    SetChrPos(0xF3, 470, 8050, 66800, 0)
    SetChrPos(0xF4, -1590, 8050, 66500, 0)
    SetChrPos(0xF5, -660, 8050, 65500, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(790, 8050, 68460, 0)
    OP_67(0, 5810, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(224, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF3")
    OP_A2(0x2)

    ChrTalk(    #22
        0x10D,
        (
            "#272F#12PThat seems to be the end of our trial, at least.\x02\x03",

            "#270FAlthough I certainly wasn't expecting that to be\x01",
            "a fiend perfectly disguised as Kevin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1CF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBB")
    OP_A2(0x1)

    ChrTalk(    #23
        0x10E,
        (
            "#176F#12PThat seems to be the end of our trial, at least.\x02\x03",

            "#178FAlthough I certainly wasn't expecting that to be \x01",
            "a fiend that had perfectly disguised itself as\x01",
            "Father Kevin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E64")
    OP_A2(0x4)

    ChrTalk(    #24
        0x102,
        (
            "#1505F#12PIt looks like that's the end of this trial, at\x01",
            "least.\x02\x03",

            "#1503FI really wasn't expecting that to be a fiend\x01",
            "disguised as Kevin, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1E64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0B")
    OP_A2(0x3)

    ChrTalk(    #25
        0x10B,
        (
            "#413F#12PW-Well, it looks like that's the end of this\x01",
            "trial, at least.\x02\x03",

            "#212FSure didn't expect that Kevin to be a fiend in\x01",
            "disguise, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBA")

    label("loc_1F0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FBA")
    OP_A2(0x5)

    ChrTalk(    #26
        0x105,
        (
            "#1167F#12PWell, that seems to be the end of this trial.\x02\x03",

            "#1163FAlthough, I don't think any of us expected it\x01",
            "to be a fiend perfectly disguised as Kevin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FBA")

    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #27
        0x10F,
        (
            "#1446F#5PTrue. I wasn't...\x02\x03",

            "#1445F...Oh.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x10F, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(300)
    Fade(500)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 5)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2049")
    OP_62(0xF3, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20B0")

    label("loc_2049")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2071")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20B0")

    label("loc_2071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF3)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2099")
    OP_62(0xF3, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_20B0")

    label("loc_2099")

    OP_62(0xF3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_20B0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
    OP_62(0xF4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2144")

    label("loc_20DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2105")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2144")

    label("loc_2105")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF4)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212D")
    OP_62(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2144")

    label("loc_212D")

    OP_62(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2144")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2171")
    OP_62(0xF5, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D8")

    label("loc_2171")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2199")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D8")

    label("loc_2199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF5)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C1")
    OP_62(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D8")

    label("loc_21C1")

    OP_62(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_21D8")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_221D")
    OP_A2(0x0)

    ChrTalk(    #28
        0x107,
        (
            "#065F#12PR-Ries?!\x02\x03",

            "Are you all right?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AD")

    label("loc_221D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2281")
    OP_A2(0x5)

    ChrTalk(    #29
        0x105,
        (
            "#1164F#12PR-Ries?!\x02\x03",

            "#1163FA-Are you all right? You weren't hurt,\x01",
            "were you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AD")

    label("loc_2281")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E2")
    OP_A2(0x3)

    ChrTalk(    #30
        0x10B,
        (
            "#213F#12PWh-Whoa, there!\x02\x03",

            "#214FYou okay?! You didn't get hurt, did you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AD")

    label("loc_22E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_234A")
    OP_A2(0x4)

    ChrTalk(    #31
        0x102,
        (
            "#1504F#12PRies?!\x02\x03",

            "#1502FAre you all right? Were you injured during\x01",
            "the battle?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AD")

    label("loc_234A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AD")
    OP_A2(0x1)

    ChrTalk(    #32
        0x10E,
        (
            "#173F#12PRies?!\x02\x03",

            "#178FAre you all right? Were you injured during\x01",
            "the battle?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AD")


    ChrTalk(    #33
        0x10F,
        (
            "#1806F#5PI-I'm fine...\x02\x03",

            "I was just so relieved to find out that it wasn't\x01",
            "really Kevin...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_62(0x10F, 0xE6, 1200, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #34
        0x10F,
        (
            "#1800F#5PA-And now that the fight is over...it seems clear\x01",
            "to me that battle was a trap set by our foes.\x01",
            "Those bizarre cannon fiends are further evidence.\x02\x03",

            "#1443FLet's hurry through that door. I'm quite concerned\x01",
            "about the other group.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25AC")

    ChrTalk(    #35
        0x105,
        (
            "#1382F#12PSo am I...\x02\x03",

            "#1165F(Heehee. Just how worried about Kevin was she?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_25AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2614")

    ChrTalk(    #36
        0x10B,
        (
            "#213F#12PS-Sure...\x02\x03",

            "#210F(Haha. She must've been so worried about\x01",
            "him, huh?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_2614")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_269B")

    ChrTalk(    #37
        0x102,
        (
            "#1500F#12PYeah, you're right.\x02\x03",

            "#1513F(...She must have been really worried about\x01",
            "Kevin to react like that.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_272E")

    label("loc_269B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_272E")

    ChrTalk(    #38
        0x10E,
        (
            "#170F#12PYes, I suppose we should.\x02\x03",

            "#179F(Heh. She must have been truly worried about\x01",
            "Father Graham to react in that way.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_272E")

    OP_A2(0x280A)
    OP_28(0x31, 0x1, 0x8)
    OP_28(0x31, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_15D7 end

    SaveToFile()

Try(main)
