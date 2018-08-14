from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '电光魔镜',                             # 9
        '鬼魅魔镜',                             # 10
        '鬼魅魔镜',                             # 11
        '鬼魅魔镜',                             # 12
        '莉丝',                                 # 13
        '封印石⑦',                             # 14
        '',                                     # 15
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
        "Function_4_1396",         # 04, 4
        "Function_5_13F0",         # 05, 5
        "Function_6_1450",         # 06, 6
        "Function_7_14B0",         # 07, 7
        "Function_8_1510",         # 08, 8
        "Function_9_1570",         # 09, 9
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
        "#1079F#5P那是……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534")

    ChrTalk(    #1
        0x10D,
        (
            "#277F#6P嗯……\x01",
            "这也许是出口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_534")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_571")

    ChrTalk(    #2
        0x10E,
        (
            "#170F#6P啊……\x01",
            "这可能是出口呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AF")

    ChrTalk(    #3
        0x105,
        (
            "#1382F#6P难道……\x01",
            "到达出口了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_5AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F1")

    ChrTalk(    #4
        0x102,
        (
            "#1500F#6P看起来……\x01",
            "这儿就是出口呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F")

    label("loc_5F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62F")

    ChrTalk(    #5
        0x107,
        (
            "#560F#6P难、难道……\x01",
            "那就是出口！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B7")

    ChrTalk(    #6
        0x109,
        (
            "#1075F#5P嗯……\x01",
            "很有可能。\x02\x03",

            "#1840F呼……\x01",
            "要是莉丝那边的进展也很顺利就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A")

    label("loc_6B7")


    ChrTalk(    #7
        0x109,
        (
            "#1075F#5P啊啊……\x01",
            "很有可能。\x02\x03",

            "#1840F呼……\x01",
            "要是莉丝那边的进展也很顺利就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C9")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_830")

    label("loc_7C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_830")

    label("loc_7F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_830")

    label("loc_819")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_830")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85D")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C4")

    label("loc_85D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C4")

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AD")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8C4")

    label("loc_8AD")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8C4")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F1")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_958")

    label("loc_8F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_919")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_958")

    label("loc_919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_941")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_958")

    label("loc_941")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_958")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_985")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_985")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9EC")

    label("loc_9D5")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9EC")

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
        "#1063F#6P嘁……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAF")
    OP_A2(0x3)

    ChrTalk(    #9
        0x10B,
        (
            "#210F#6P哼……\x01",
            "看来不容我们轻易通过这里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_AAF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFB")
    OP_A2(0x0)

    ChrTalk(    #10
        0x107,
        (
            "#062F#6P看、看起来\x01",
            "敌人不准我们轻易通过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4C")
    OP_A2(0x4)

    ChrTalk(    #11
        0x102,
        (
            "#1502F#6P……看来，\x01",
            "对方不容我们这么简单就通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9D")
    OP_A2(0x5)

    ChrTalk(    #12
        0x105,
        (
            "#1162F#6P……看来，\x01",
            "对方不容我们这么简单就通过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_B9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE6")
    OP_A2(0x1)

    ChrTalk(    #13
        0x10E,
        (
            "#178F#6P……好像还是不能\x01",
            "这么简单就通过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6")

    OP_1D(0x9A)
    OP_22(0x85, 0x1, 0x64)

    def lambda_BF3():

        label("loc_BF3")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_BF3")

    QueueWorkItem2(0xEF, 0, lambda_BF3)

    def lambda_C0E():
        OP_6D(1200, 8050, 71600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C0E)

    def lambda_C26():
        OP_67(0, 5400, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C26)

    def lambda_C3E():
        OP_6B(3510, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C3E)

    def lambda_C4E():
        OP_6E(258, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C4E)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 5050, 73750, 180)
    OP_43(0x14, 0x0, 0x0, 0x4)
    WaitChrThread(0x14, 0x0)
    OP_44(0xEF, 0x0)
    OP_23(0x85)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB3")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1A")

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDB")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1A")

    label("loc_CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D03")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D1A")

    label("loc_D03")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D1A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D47")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DAE")

    label("loc_D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6F")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DAE")

    label("loc_D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D97")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_DAE")

    label("loc_D97")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_DAE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E42")

    label("loc_DDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E03")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E42")

    label("loc_E03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E2B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E42")

    label("loc_E2B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E42")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ED6")

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E97")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ED6")

    label("loc_E97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ED6")

    label("loc_EBF")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_ED6")

    Sleep(1000)

    ChrTalk(    #14
        0x109,
        "#1069F#6P……什么……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F40")

    ChrTalk(    #15
        0x107,
        "#065F#6P莉、莉丝姐姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7F")

    ChrTalk(    #16
        0x10E,
        "#173F#6P莉、莉丝小姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FBB")

    ChrTalk(    #17
        0x102,
        "#1504F#6P莉丝小姐……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_FF4")

    label("loc_FBB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FF4")

    ChrTalk(    #18
        0x105,
        "#1164F#6P莉丝小姐……！？\x02",
    )

    CloseMessageWindow()

    label("loc_FF4")


    ChrTalk(    #19
        0x14,
        "#1807F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x14, 6)
    SetChrSubChip(0x14, 0)

    def lambda_1041():

        label("loc_1041")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_1041")

    QueueWorkItem2(0x14, 2, lambda_1041)
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

    def lambda_121F():

        label("loc_121F")

        OP_7C(0x32, 0x32, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_121F")

    QueueWorkItem2(0xEF, 0, lambda_121F)

    def lambda_123A():
        OP_6D(0, 8800, 70100, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_123A)

    def lambda_1252():
        OP_67(0, 2310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1252)

    def lambda_126A():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_126A)

    def lambda_127A():
        OP_6E(230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_127A)
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
        "#1069F#6P难道……她被操纵了！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0x13D, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_211 end

    def Function_4_1396(): pass

    label("Function_4_1396")

    SetChrFlags(0xFE, 0x20)
    PlayEffect(0x1, 0x4, 0xFF, 0, 8150, 73750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1396 end

    def Function_5_13F0(): pass

    label("Function_5_13F0")

    PlayEffect(0x1, 0xFF, 0xFF, -2000, 8150, 74400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_142B():

        label("loc_142B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_142B")

    QueueWorkItem2(0xFE, 1, lambda_142B)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x1, 0x2)
    Return()

    # Function_5_13F0 end

    def Function_6_1450(): pass

    label("Function_6_1450")

    PlayEffect(0x1, 0xFF, 0xFF, 2000, 8150, 74400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_148B():

        label("loc_148B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_148B")

    QueueWorkItem2(0xFE, 1, lambda_148B)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x2, 0x2)
    Return()

    # Function_6_1450 end

    def Function_7_14B0(): pass

    label("Function_7_14B0")

    PlayEffect(0x1, 0xFF, 0xFF, -4000, 8050, 76000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_14EB():

        label("loc_14EB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_14EB")

    QueueWorkItem2(0xFE, 1, lambda_14EB)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x3, 0x2)
    Return()

    # Function_7_14B0 end

    def Function_8_1510(): pass

    label("Function_8_1510")

    PlayEffect(0x1, 0xFF, 0xFF, 4000, 8050, 76000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_154B():

        label("loc_154B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_154B")

    QueueWorkItem2(0xFE, 1, lambda_154B)
    OP_91(0xFE, 0x0, 0xFA0, 0x0, 0x320, 0x0)
    OP_82(0x4, 0x2)
    Return()

    # Function_8_1510 end

    def Function_9_1570(): pass

    label("Function_9_1570")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175C")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17C3")

    label("loc_175C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1784")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17C3")

    label("loc_1784")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AC")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17C3")

    label("loc_17AC")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17C3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F0")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1857")

    label("loc_17F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1818")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1857")

    label("loc_1818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1840")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1857")

    label("loc_1840")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1857")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1884")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18EB")

    label("loc_1884")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18AC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18EB")

    label("loc_18AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18D4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18EB")

    label("loc_18D4")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18EB")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1918")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_197F")

    label("loc_1918")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1940")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_197F")

    label("loc_1940")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1968")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_197F")

    label("loc_1968")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_197F")

    Sleep(1000)

    ChrTalk(    #21
        0x109,
        "#1079F#5P哦……\x02",
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

    def lambda_19FC():
        OP_6D(1130, 8050, 67300, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19FC)
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
        "\x07\x00得到了\x1F\x58\x03\x07\x00。\x02",
    )

    Jump("loc_1AA1")

    label("loc_1AA1")

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

    def lambda_1B3A():
        OP_6B(4600, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1B3A)
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
            "#1065F#5P……看起来，\x01",
            "那个所谓的试炼算是到此为止了。\x02\x03",

            "#1840F话说回来……\x01",
            "没想到会有能变成\x01",
            "和莉丝一模一样的魔物啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CD6")
    OP_A2(0x0)

    ChrTalk(    #24
        0x107,
        (
            "#561F#12P吓、吓了我一跳……\x02\x03",

            "#560F我还以为她一定是\x01",
            "被敌人操纵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9F")

    label("loc_1CD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D49")
    OP_A2(0x5)

    ChrTalk(    #25
        0x105,
        (
            "#1383F#12P的确是让人惊讶啊……\x02\x03",

            "#1382F我本来还以为她\x01",
            "一定是被敌人操纵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9F")

    label("loc_1D49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBE")
    OP_A2(0x3)

    ChrTalk(    #26
        0x10B,
        (
            "#413F#12P的、的确是让人惊讶啊……\x02\x03",

            "#210F我本来还以为她\x01",
            "一定是被敌人操纵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9F")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E35")
    OP_A2(0x4)

    ChrTalk(    #27
        0x102,
        (
            "#1505F#12P……还真是有点不可思议。\x02\x03",

            "#1500F我本来还以为她\x01",
            "一定是被敌人操纵了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E9F")

    label("loc_1E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9F")
    OP_A2(0x1)

    ChrTalk(    #28
        0x10E,
        (
            "#179F#12P真是让人吃惊……\x02\x03",

            "#170F我本来还以为她\x01",
            "一定是被敌人操纵了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E9F")

    OP_8C(0x109, 180, 400)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F66")

    ChrTalk(    #29
        0x109,
        (
            "#1840F#5P嗯，即使是和她非常熟悉的我，\x01",
            "在那一瞬间也被骗了啊。\x02\x03",

            "#1065F刚才一起出现的镜子\x01",
            "也是些很难对付的咒具……\x02\x03",

            "#1063F这果然也是\x01",
            "敌人布下的陷阱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2013")

    label("loc_1F66")


    ChrTalk(    #30
        0x109,
        (
            "#1840F#5P嗯，即使是和她非常熟悉的我，\x01",
            "在那一瞬间也被骗了啊。\x02\x03",

            "#1065F刚才一起出现的镜子\x01",
            "也是些很难对付的咒具……\x02\x03",

            "#1063F这果然也是\x01",
            "敌人布下的陷阱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2013")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2096")
    OP_A2(0x2)

    ChrTalk(    #31
        0x10D,
        (
            "#272F#12P这样一来……\x01",
            "修女那边就很令人担心了啊。\x02\x03",

            "#270F我们最好加快脚步。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_2096")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210D")
    OP_A2(0x1)

    ChrTalk(    #32
        0x10E,
        (
            "#176F#12P这样一来……\x01",
            "莉丝小姐那边就很令人担心了啊。\x02\x03",

            "#178F我们最好赶快前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_210D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218A")
    OP_A2(0x4)

    ChrTalk(    #33
        0x102,
        (
            "#1505F#12P这样一来……\x01",
            "莉丝小姐那边就很令人担心了啊。\x02\x03",

            "#1502F我们还是赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_218A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FD")
    OP_A2(0x3)

    ChrTalk(    #34
        0x10B,
        (
            "#416F#12P这样的话……\x01",
            "修女那边就很令人担心了啊。\x02\x03",

            "#212F我们还是赶快前进吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2277")

    label("loc_21FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2277")
    OP_A2(0x5)

    ChrTalk(    #35
        0x105,
        (
            "#1167F#12P这样的话……\x01",
            "莉丝小姐那边就很令人担心了啊。\x02\x03",

            "#1162F我们还是赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22B8")

    ChrTalk(    #36
        0x109,
        (
            "#1063F#5P嗯……\x01",
            "赶快穿过那扇门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_22B8")


    ChrTalk(    #37
        0x109,
        (
            "#1063F#5P啊啊……\x01",
            "赶快穿过那扇门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E9")

    OP_A2(0x2807)
    OP_28(0x30, 0x1, 0x8)
    OP_28(0x30, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_9_1570 end

    SaveToFile()

Try(main)
