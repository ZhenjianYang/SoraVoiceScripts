from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7106   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7106.x',
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
        'Spark Mirror',                         # 9
        'Haunted Mirror',                       # 10
        'Haunted Mirror',                       # 11
        'Haunted Mirror',                       # 12
        'Ries',                                 # 13
        'Sealing Stone 7',                      # 14
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
        'ED6_DT29/CH14140 ._CH',             # 00
        'ED6_DT29/CH14140 ._CH',             # 01
        'ED6_DT29/CH14150 ._CH',             # 02
        'ED6_DT29/CH14150 ._CH',             # 03
        'ED6_DT27/CH04150 ._CH',             # 04
        'ED6_DT27/CH04151 ._CH',             # 05
        'ED6_DT27/CH04155 ._CH',             # 06
        'ED6_DT27/CH04156 ._CH',             # 07
        'ED6_DT26/CH20621 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT29/CH14140P._CP',             # 00
        'ED6_DT29/CH14140P._CP',             # 01
        'ED6_DT29/CH14150P._CP',             # 02
        'ED6_DT29/CH14150P._CP',             # 03
        'ED6_DT27/CH04150P._CP',             # 04
        'ED6_DT27/CH04151P._CP',             # 05
        'ED6_DT27/CH04155P._CP',             # 06
        'ED6_DT27/CH04156P._CP',             # 07
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        "Function_0_1D2",          # 00, 0
        "Function_1_1D3",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_211",          # 03, 3
        "Function_4_13EC",         # 04, 4
        "Function_5_1446",         # 05, 5
        "Function_6_14A6",         # 06, 6
        "Function_7_1506",         # 07, 7
        "Function_8_1566",         # 08, 8
        "Function_9_15C6",         # 09, 9
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Return()

    # Function_0_1D2 end

    def Function_1_1D3(): pass

    label("Function_1_1D3")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFF1D70, 0x230089)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 7)), scpexpr(EXPR_END)), "loc_1FF")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x800, 0x0)
    ExitThread()
    OP_6F(0x0, 120)

    label("loc_1FF")

    Return()

    # Function_1_1D3 end

    def Function_2_200(): pass

    label("Function_2_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 7)), scpexpr(EXPR_END)), "loc_208")
    Return()

    label("loc_208")

    Call(0, 3)
    Call(0, 9)
    Return()

    # Function_2_200 end

    def Function_3_211(): pass

    label("Function_3_211")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    Fade(1000)
    OP_6D(1650, 10000, 76160, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(5500, 0)
    OP_6C(57000, 0)
    OP_6E(382, 0)

    def lambda_2AB():
        OP_6D(1650, 10000, 66310, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2AB)

    def lambda_2C3():
        OP_67(0, 8850, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2C3)

    def lambda_2DB():
        OP_6B(6140, 6000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2DB)

    def lambda_2EB():
        OP_6E(382, 6000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2EB)
    SetChrPos(0x109, 0, 8000, 54580, 0)
    SetChrPos(0xEF, 330, 8000, 53450, 0)
    SetChrPos(0xF0, -1200, 8000, 52990, 0)
    SetChrPos(0xF1, -220, 8000, 51620, 0)
    Sleep(1000)

    def lambda_344():
        OP_8E(0xFE, 0x0, 0x1F72, 0x1022A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_344)
    Sleep(50)

    def lambda_364():
        OP_8E(0xFE, 0x4B0, 0x1F72, 0xFEB9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_364)
    Sleep(150)

    def lambda_384():
        OP_8E(0xFE, 0xFFFFFAEC, 0x1F72, 0xFC8A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_384)
    Sleep(50)

    def lambda_3A4():
        OP_8E(0xFE, 0xFFFFFF42, 0x1F72, 0xF898, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3A4)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(244, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(300)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_42D():
        OP_6D(910, 11600, 106980, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42D)

    def lambda_445():
        OP_67(0, 2670, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_445)

    def lambda_45D():
        OP_6B(4580, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D)

    def lambda_46D():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_46D)

    def lambda_47D():
        OP_6E(276, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_47D)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(1020, 8050, 66150, 0)
    OP_67(0, 6280, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(244, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x109,
        "#1079F#5POver there!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_532")

    ChrTalk(    #1
        0x10D,
        "#277F#6PCould that be the exit, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_639")

    label("loc_532")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_571")

    ChrTalk(    #2
        0x10E,
        "#170F#6PCould that be the exit, perhaps?\x02",
    )

    CloseMessageWindow()
    Jump("loc_639")

    label("loc_571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B5")

    ChrTalk(    #3
        0x105,
        "#1382F#6PDo you think that could be the exit?\x02",
    )

    CloseMessageWindow()
    Jump("loc_639")

    label("loc_5B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F9")

    ChrTalk(    #4
        0x102,
        "#1500F#6PThat looks like it must be the exit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_639")

    label("loc_5F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_639")

    ChrTalk(    #5
        0x107,
        "#560F#6PDo you think that could be the exit?\x02",
    )

    CloseMessageWindow()

    label("loc_639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C7")

    ChrTalk(    #6
        0x109,
        (
            "#1075F#5PSure looks that way.\x02\x03",

            "#1840FWhew... I hope everything's going well\x01",
            "for Ries' group, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72E")

    label("loc_6C7")


    ChrTalk(    #7
        0x109,
        (
            "#1075F#5PSure looks that way.\x02\x03",

            "#1840FWhew... I hope everything's going well\x01",
            "for Ries' group, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DD")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_844")

    label("loc_7DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_805")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_844")

    label("loc_805")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82D")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_844")

    label("loc_82D")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_844")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_871")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D8")

    label("loc_871")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D8")

    label("loc_899")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C1")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D8")

    label("loc_8C1")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8D8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_96C")

    label("loc_905")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_96C")

    label("loc_92D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_955")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_96C")

    label("loc_955")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_96C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_999")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A00")

    label("loc_999")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A00")

    label("loc_9C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A00")

    label("loc_9E9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A00")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 10)
    SetChrSubChip(0xEF, 0)
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

    ChrTalk(    #8
        0x109,
        "#1063F#6PBah. There go my hopes of just walking.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF5")
    OP_A2(0x3)

    ChrTalk(    #9
        0x10B,
        (
            "#210F#6PHeh. Looks like they're not gonna let us\x01",
            "reach it without a fight.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_AF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B54")
    OP_A2(0x0)

    ChrTalk(    #10
        0x107,
        (
            "#062F#6PI think we're going to have to fight\x01",
            "our way to it, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_B54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB8")
    OP_A2(0x4)

    ChrTalk(    #11
        0x102,
        (
            "#1502F#6PIt looks like we're going to have to fight\x01",
            "our way to it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_BB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C28")
    OP_A2(0x5)

    ChrTalk(    #12
        0x105,
        (
            "#1162F#6PI think we'll have another battle ahead\x01",
            "of us before we can reach it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C93")

    label("loc_C28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C93")
    OP_A2(0x1)

    ChrTalk(    #13
        0x10E,
        (
            "#178F#6PIt seems we have another battle ahead\x01",
            "of us before we can reach it, however.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C93")

    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)

    def lambda_CA0():

        label("loc_CA0")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_CA0")

    QueueWorkItem2(0xEF, 0, lambda_CA0)

    def lambda_CBB():
        OP_6D(1200, 8050, 71600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CBB)

    def lambda_CD3():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CD3)

    def lambda_CEB():
        OP_6B(3510, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CEB)

    def lambda_CFB():
        OP_6E(258, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CFB)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 5050, 73750, 180)
    OP_43(0x14, 0x0, 0x0, 0x4)
    WaitChrThread(0x14, 0x0)
    OP_44(0xEF, 0x0)
    OP_23(0x85)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D60")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DC7")

    label("loc_D60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D88")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DC7")

    label("loc_D88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB0")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DC7")

    label("loc_DB0")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DC7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF4")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E5B")

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E5B")

    label("loc_E1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E5B")

    label("loc_E44")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E5B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E88")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EEF")

    label("loc_E88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB0")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EEF")

    label("loc_EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EEF")

    label("loc_ED8")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EEF")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1C")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F83")

    label("loc_F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F44")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F83")

    label("loc_F44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F83")

    label("loc_F6C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F83")

    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1069F#6P...What?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FCC")

    ChrTalk(    #15
        0x107,
        "#065F#6PR-Ries?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_FCC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(    #16
        0x10E,
        "#173F#6PR-Ries?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_FF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #17
        0x102,
        "#1504F#6PRies?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_1023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #18
        0x105,
        "#1164F#6PR-Ries?!\x02",
    )

    CloseMessageWindow()

    label("loc_104D")


    ChrTalk(    #19
        0x14,
        "#1807F#5P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x14, 6)
    SetChrSubChip(0x14, 0)

    def lambda_107E():

        label("loc_107E")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_107E")

    QueueWorkItem2(0x14, 2, lambda_107E)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 0, 8050, 73750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x1, 0xFF, -2200, 8150, 74400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 2200, 8050, 74400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFF, -4000, 8050, 76000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, 4000, 8050, 76000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(0, 8800, 69800, 0)
    OP_67(0, 4019, -10000, 0)
    OP_6B(4090, 0)
    OP_6C(0, 0)
    OP_6E(254, 0)
    SetChrPos(0x109, 0, 8050, 66090, 0)
    SetChrPos(0xEF, 1200, 8050, 65209, 0)
    SetChrPos(0xF0, -1300, 8050, 64650, 0)
    SetChrPos(0xF1, -90, 8050, 63640, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_125C():

        label("loc_125C")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_125C")

    QueueWorkItem2(0xEF, 0, lambda_125C)

    def lambda_1277():
        OP_6D(0, 8800, 70100, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1277)

    def lambda_128F():
        OP_67(0, 2310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128F)

    def lambda_12A7():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12A7)

    def lambda_12B7():
        OP_6E(230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_12B7)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, -2000, 5150, 74400, 180)
    SetChrPos(0x11, 2000, 5050, 74400, 180)
    SetChrPos(0x12, -4000, 5050, 76000, 180)
    SetChrPos(0x13, 4000, 5050, 76000, 180)
    OP_43(0x10, 0x0, 0x0, 0x5)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x12, 0x0, 0x0, 0x7)
    OP_43(0x13, 0x0, 0x0, 0x8)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x0, 0x2)
    WaitChrThread(0x109, 0x0)
    OP_44(0xEF, 0x0)
    OP_23(0x85)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x14, 4)
    SetChrSubChip(0x14, 0)
    OP_44(0x14, 0x2)
    OP_0D()
    Sleep(800)

    ChrTalk(    #20
        0x109,
        (
            "#1069F#6PDamn it... Is she being mind controlled\x01",
            "or something?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0x13D, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_211 end

    def Function_4_13EC(): pass

    label("Function_4_13EC")

    SetChrFlags(0xFE, 0x20)
    PlayEffect(0x1, 0x4, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_13EC end

    def Function_5_1446(): pass

    label("Function_5_1446")

    PlayEffect(0x1, 0xFF, 0xFF, -2000, 8150, 74400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1481():

        label("loc_1481")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1481")

    QueueWorkItem2(0xFE, 1, lambda_1481)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x1, 0x2)
    Return()

    # Function_5_1446 end

    def Function_6_14A6(): pass

    label("Function_6_14A6")

    PlayEffect(0x1, 0xFF, 0xFF, 2000, 8150, 74400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14E1():

        label("loc_14E1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14E1")

    QueueWorkItem2(0xFE, 1, lambda_14E1)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x2, 0x2)
    Return()

    # Function_6_14A6 end

    def Function_7_1506(): pass

    label("Function_7_1506")

    PlayEffect(0x1, 0xFF, 0xFF, -4000, 8050, 76000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1541():

        label("loc_1541")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1541")

    QueueWorkItem2(0xFE, 1, lambda_1541)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x3, 0x2)
    Return()

    # Function_7_1506 end

    def Function_8_1566(): pass

    label("Function_8_1566")

    PlayEffect(0x1, 0xFF, 0xFF, 4000, 8050, 76000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_15A1():

        label("loc_15A1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_15A1")

    QueueWorkItem2(0xFE, 1, lambda_15A1)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x4, 0x2)
    Return()

    # Function_8_1566 end

    def Function_9_15C6(): pass

    label("Function_9_15C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x1, "map\\mp253_00.eff")
    LoadEffect(0x2, "map\\mp253_01.eff")
    OP_E0(238, 0x49, 0x2)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(240, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x2)
    SetChrPos(0x109, -240, 8050, 67870, 0)
    SetChrPos(0xEF, 1330, 8050, 66380, 0)
    SetChrPos(0xF0, -1330, 8050, 66880, 0)
    SetChrPos(0xF1, 40, 8050, 65430, 0)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0xEF, 10)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 11)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 12)
    SetChrSubChip(0xF1, 0)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
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
    ClearChrFlags(0x15, 0x80)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x15, -260, 9300, 69960, 0)
    PlayEffect(0x1, 0x7, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x6, 0x15, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B2")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1819")

    label("loc_17B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DA")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1819")

    label("loc_17DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1802")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1819")

    label("loc_1802")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1819")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1846")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AD")

    label("loc_1846")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AD")

    label("loc_186E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1896")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18AD")

    label("loc_1896")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18AD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DA")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_18DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1902")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_1902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1941")

    label("loc_192A")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1941")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D5")

    label("loc_196E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1996")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D5")

    label("loc_1996")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19D5")

    label("loc_19BE")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19D5")

    Sleep(1000)

    ChrTalk(    #21
        0x109,
        "#1079F#5POh...\x02",
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

    def lambda_1A4A():
        OP_6D(1130, 8050, 67300, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A4A)
    OP_8E(0x109, 0xFFFFFEE8, 0x1F72, 0x10CFC, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x15, 0x64, 0x238C, 0x10E5A, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x15, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Found \x1F\x58\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x358, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
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

    def lambda_1B82():
        OP_6B(4600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B82)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x109, -360, 8050, 68500, 0)
    SetChrPos(0xEF, 270, 8050, 67000, 0)
    SetChrPos(0xF0, -1590, 8050, 66600, 0)
    SetChrPos(0xF1, -660, 8050, 65680, 0)
    Sleep(1000)
    Fade(500)
    OP_6D(790, 8050, 68460, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(224, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x109,
        (
            "#1065F#5PWell, looks like that's the end of this trial.\x02\x03",

            "#1840FSure came as a surprise to find out that Ries\x01",
            "was just a fiend in disguise, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D2D")
    OP_A2(0x0)

    ChrTalk(    #24
        0x107,
        (
            "#561F#12PY-Yeah...\x02\x03",

            "#560FI thought she was being mind controlled\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1D2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA1")
    OP_A2(0x5)

    ChrTalk(    #25
        0x105,
        (
            "#1383F#12PI was shocked, too.\x02\x03",

            "#1382FI thought she was being mind controlled\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1DA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E22")
    OP_A2(0x3)

    ChrTalk(    #26
        0x10B,
        (
            "#413F#12PI-I couldn't believe it, either...\x02\x03",

            "#210FI thought she was being mind controlled\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1E22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E98")
    OP_A2(0x4)

    ChrTalk(    #27
        0x102,
        (
            "#1505F#12PI was shocked, too...\x02\x03",

            "#1500FI thought she was being mind controlled\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F09")

    label("loc_1E98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F09")
    OP_A2(0x1)

    ChrTalk(    #28
        0x10E,
        (
            "#179F#12PI was shocked, too...\x02\x03",

            "#170FI thought she was being mind controlled\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F09")

    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2017")

    ChrTalk(    #29
        0x109,
        (
            "#1840F#5PI've known her for a long time, and if I was\x01",
            "fooled, it's no surprise that you guys would\x01",
            "be.\x02\x03",

            "#1065FThe mirrors with it were so deadly, too.\x02\x03",

            "#1063FI think it's safe to say that whole battle was\x01",
            "a trap set for us by our enemies.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210B")

    label("loc_2017")


    ChrTalk(    #30
        0x109,
        (
            "#1840F#5PI've known her for a long time, and if I was\x01",
            "fooled, it's no surprise that you guys would\x01",
            "be.\x02\x03",

            "#1065FThe mirrors with it were so deadly, too.\x02\x03",

            "#1063FI think it's safe to say that whole battle was\x01",
            "a trap set for us by our enemies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210B")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A5")
    OP_A2(0x2)

    ChrTalk(    #31
        0x10D,
        (
            "#272F#12PThat being the case, I'm concerned for how\x01",
            "the other group is faring.\x02\x03",

            "#270FWe should hurry on ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CE")

    label("loc_21A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222D")
    OP_A2(0x1)

    ChrTalk(    #32
        0x10E,
        (
            "#176F#12PThat being the case, I'm concerned for how\x01",
            "the other group is faring.\x02\x03",

            "#178FWe should hurry on ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CE")

    label("loc_222D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BB")
    OP_A2(0x4)

    ChrTalk(    #33
        0x102,
        (
            "#1505F#12PExactly... Which is why I'm concerned\x01",
            "about how the other group is doing.\x02\x03",

            "#1502FWe should probably hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CE")

    label("loc_22BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2348")
    OP_A2(0x3)

    ChrTalk(    #34
        0x10B,
        (
            "#416F#12PYeah... I'm kinda worried about how\x01",
            "the other group is doing, too.\x02\x03",

            "#212FWe should hurry, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23CE")

    label("loc_2348")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23CE")
    OP_A2(0x5)

    ChrTalk(    #35
        0x105,
        (
            "#1167F#12PThat's true...and it makes me worry\x01",
            "even more about the other group.\x02\x03",

            "#1162FWe should hurry on ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_241B")

    ChrTalk(    #36
        0x109,
        "#1063F#5PYeah. Let's get ourselves over to that gate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_241B")


    ChrTalk(    #37
        0x109,
        "#1063F#5PYeah. Let's get ourselves over to that gate.\x02",
    )

    CloseMessageWindow()

    label("loc_2456")

    OP_A2(0x2807)
    OP_28(0x30, 0x1, 0x8)
    OP_28(0x30, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_9_15C6 end

    SaveToFile()

Try(main)
