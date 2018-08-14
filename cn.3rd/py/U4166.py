from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '魔兽①',                               # 9
        '魔兽②',                               # 10
        '魔兽③',                               # 11
        '魔兽④',                               # 12
        '魔兽⑤',                               # 13
        '魔兽⑥',                               # 14
        '黑暗降临者',                           # 15
        '封印石⑤',                             # 16
        '',                                     # 17
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
        "Function_4_EC9",          # 04, 4
        "Function_5_EF1",          # 05, 5
        "Function_6_F54",          # 06, 6
        "Function_7_FB7",          # 07, 7
        "Function_8_101A",         # 08, 8
        "Function_9_107D",         # 09, 9
        "Function_10_10E0",        # 0A, 10
        "Function_11_1143",        # 0B, 11
        "Function_12_11A6",        # 0C, 12
        "Function_13_1209",        # 0D, 13
        "Function_14_1248",        # 0E, 14
        "Function_15_1287",        # 0F, 15
        "Function_16_12C6",        # 10, 16
        "Function_17_1305",        # 11, 17
        "Function_18_1B3A",        # 12, 18
        "Function_19_1B94",        # 13, 19
        "Function_20_24D8",        # 14, 20
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
            "#1060F#5P……这里是比赛场地吧。\x02\x03",

            "#1066F哈哈，这时候应该\x01",
            "啪啪的出现对手才符合……\x02",
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

    def lambda_74B():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_74B)
    Sleep(100)

    def lambda_75E():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_75E)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D5")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83C")

    label("loc_7D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83C")

    label("loc_7FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_83C")

    label("loc_825")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_83C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_869")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D0")

    label("loc_869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D0")

    label("loc_891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8D0")

    label("loc_8B9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8D0")

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
        "#1064F#6P哇！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10F,
        "#1801F#5P…………凯文？（瞪）\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #3
        0x109,
        (
            "#1068F#6P这是偶然！偶然！\x01",
            "才不关我的事！\x02\x03",

            "#1069F真是的，不知道是谁搞的鬼，\x01",
            "这也太顺理成章了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A46")

    ChrTalk(    #4
        0x107,
        "#065F#6P哇、哇哇……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_A46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8D")

    ChrTalk(    #5
        0x10B,
        (
            "#216F#6P事、事到如今\x01",
            "就不用管这些了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC2")

    label("loc_A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC2")

    ChrTalk(    #6
        0x10E,
        "#172F#6P……一会儿再说吧！\x02",
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF4")

    ChrTalk(    #7
        0x10D,
        "#271F#6P要来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B24")

    ChrTalk(    #8
        0x10E,
        "#177F#6P来了……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_B51")

    label("loc_B24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B51")

    ChrTalk(    #9
        0x10B,
        "#214F#6P来了……！\x02",
    )

    CloseMessageWindow()

    label("loc_B51")

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
        "#1063F#6P哼，是连战吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        "#1443F#6P……正好……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_242 end

    def Function_4_EC9(): pass

    label("Function_4_EC9")


    def lambda_ECF():

        label("loc_ECF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_ECF")

    QueueWorkItem2(0xFE, 1, lambda_ECF)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x5DC, 0x0)
    Return()

    # Function_4_EC9 end

    def Function_5_EF1(): pass

    label("Function_5_EF1")

    PlayEffect(0x1, 0x4, 0xFF, 740, 0, -10010, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_F2C():

        label("loc_F2C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F2C")

    QueueWorkItem2(0xFE, 1, lambda_F2C)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    Return()

    # Function_5_EF1 end

    def Function_6_F54(): pass

    label("Function_6_F54")

    PlayEffect(0x1, 0x5, 0xFF, -1320, 0, -11740, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_F8F():

        label("loc_F8F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F8F")

    QueueWorkItem2(0xFE, 1, lambda_F8F)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_6_F54 end

    def Function_7_FB7(): pass

    label("Function_7_FB7")

    PlayEffect(0x1, 0x6, 0xFF, 3110, 0, -11950, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_FF2():

        label("loc_FF2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FF2")

    QueueWorkItem2(0xFE, 1, lambda_FF2)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    Return()

    # Function_7_FB7 end

    def Function_8_101A(): pass

    label("Function_8_101A")

    PlayEffect(0x1, 0x7, 0xFF, 980, 0, -14000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_1055():

        label("loc_1055")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1055")

    QueueWorkItem2(0xFE, 1, lambda_1055)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x514, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_8_101A end

    def Function_9_107D(): pass

    label("Function_9_107D")

    PlayEffect(0x1, 0x4, 0xFF, 740, 0, -10010, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_10B8():

        label("loc_10B8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_10B8")

    QueueWorkItem2(0xFE, 1, lambda_10B8)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x4, 0x2)
    Return()

    # Function_9_107D end

    def Function_10_10E0(): pass

    label("Function_10_10E0")

    PlayEffect(0x1, 0x5, 0xFF, -2020, 0, -11740, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_111B():

        label("loc_111B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_111B")

    QueueWorkItem2(0xFE, 1, lambda_111B)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_10_10E0 end

    def Function_11_1143(): pass

    label("Function_11_1143")

    PlayEffect(0x1, 0x6, 0xFF, 3810, 0, -11950, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_117E():

        label("loc_117E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_117E")

    QueueWorkItem2(0xFE, 1, lambda_117E)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x6, 0x2)
    Return()

    # Function_11_1143 end

    def Function_12_11A6(): pass

    label("Function_12_11A6")

    PlayEffect(0x1, 0x7, 0xFF, 980, 0, -14500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_11E1():

        label("loc_11E1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_11E1")

    QueueWorkItem2(0xFE, 1, lambda_11E1)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x3, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_12_11A6 end

    def Function_13_1209(): pass

    label("Function_13_1209")


    def lambda_120F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_120F)
    OP_8E(0xFE, 0x12C, 0x0, 0xFFFFF920, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_13_1209 end

    def Function_14_1248(): pass

    label("Function_14_1248")


    def lambda_124E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_124E)
    OP_8E(0xFE, 0x6F4, 0x0, 0xFFFFF93E, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_14_1248 end

    def Function_15_1287(): pass

    label("Function_15_1287")


    def lambda_128D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_128D)
    OP_8E(0xFE, 0xFFFFFF42, 0x0, 0xFFFFFF06, 0x7D0, 0x0)
    Sleep(200)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_15_1287 end

    def Function_16_12C6(): pass

    label("Function_16_12C6")


    def lambda_12CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12CC)
    OP_8E(0xFE, 0x8A2, 0x0, 0xFFFFFF24, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 135, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_16_12C6 end

    def Function_17_1305(): pass

    label("Function_17_1305")

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
        "#1069F#6P嘁……真烦人！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1441F#6P而且……\x01",
            "这次是个超级大怪物呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)

    def lambda_154A():

        label("loc_154A")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_154A")

    QueueWorkItem2(0x10F, 0, lambda_154A)
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

    def lambda_15FB():
        OP_6D(940, 2100, -14340, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15FB)

    def lambda_1613():
        OP_67(0, 1790, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1613)

    def lambda_162B():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_162B)

    def lambda_163B():
        OP_6C(180000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_163B)

    def lambda_164B():
        OP_6E(455, 8000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_164B)

    def lambda_165B():
        OP_91(0xFE, 0x0, 0x1F40, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_165B)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1743")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17AA")

    label("loc_1743")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17AA")

    label("loc_176B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1793")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17AA")

    label("loc_1793")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17AA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_183E")

    label("loc_17D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_183E")

    label("loc_17FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1827")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_183E")

    label("loc_1827")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_183E")

    Sleep(1000)

    ChrTalk(    #14
        0x10F,
        "#1444F#5P这、这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1896")

    ChrTalk(    #15
        0x10B,
        "#216F#5P这、这家伙！？\x02",
    )

    CloseMessageWindow()

    label("loc_1896")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18D4")

    ChrTalk(    #16
        0x107,
        (
            "#065F#5P机、机器马……！？\x01",
            "　\x02",
        )
    )

    Jump("loc_18D0")

    label("loc_18D0")

    CloseMessageWindow()
    Jump("loc_1943")

    label("loc_18D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_190C")

    ChrTalk(    #17
        0x10E,
        "#173F#5P甲胄人马兵……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1943")

    label("loc_190C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1943")

    ChrTalk(    #18
        0x10D,
        "#271F#5P是甲胄人马兵……！？\x02",
    )

    CloseMessageWindow()

    label("loc_1943")


    ChrTalk(    #19
        0x109,
        (
            "#1065F#5P好像和艾丝蒂尔他们\x01",
            "在学院地下打倒的机器\x01",
            "是同一种类……\x02\x03",

            "#1069F算了，\x01",
            "总之这个应该是最后了！\x02\x03",

            "把他修理一番取得优胜吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_19E7():
        OP_6D(370, 2720, -3670, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19E7)

    def lambda_19FF():
        OP_67(0, 7800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19FF)

    def lambda_1A17():
        OP_6B(2100, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A17)

    def lambda_1A27():
        OP_6C(127000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1A27)

    def lambda_1A37():
        OP_6E(430, 1300)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1A37)

    def lambda_1A47():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1A47)
    OP_D8(0x7, 0x3E8)
    OP_B0(0x7, 0xD)
    OP_6F(0x7, 251)
    OP_70(0x7, 0x10A)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x16, 0x1)

    def lambda_1A91():
        OP_67(0, 5800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A91)
    OP_72(0x2007, 0x0)
    ExitThread()
    OP_D8(0x7, 0x3E8)
    OP_B0(0x7, 0x8)
    OP_6F(0x7, 81)
    OP_70(0x7, 0x61)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(1700)

    def lambda_1ACF():
        OP_6D(1140, 1650, -3820, 200)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1ACF)

    def lambda_1AE7():
        OP_67(0, 5000, -10000, 200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AE7)

    def lambda_1AFF():
        OP_6B(1800, 200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AFF)

    def lambda_1B0F():
        OP_6E(380, 200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1B0F)
    OP_73(0x7)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_17_1305 end

    def Function_18_1B3A(): pass

    label("Function_18_1B3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B93")
    OP_24(0xEC, 0x32)
    OP_B0(0x7, 0xD)
    OP_6F(0x7, 251)
    OP_70(0x7, 0x10A)

    def lambda_1B5F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_1B5F)
    Sleep(500)
    OP_22(0xEC, 0x0, 0x64)
    Sleep(200)
    OP_22(0xEC, 0x0, 0x64)
    WaitChrThread(0x16, 0x1)
    OP_73(0x7)
    Jump("Function_18_1B3A")

    label("loc_1B93")

    Return()

    # Function_18_1B3A end

    def Function_19_1B94(): pass

    label("Function_19_1B94")

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

    def lambda_1D48():
        OP_67(0, 4230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D48)

    def lambda_1D60():
        OP_6D(1220, 0, -13610, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D60)
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

    def lambda_1DEC():

        label("loc_1DEC")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1DEC")

    QueueWorkItem2(0x10F, 0, lambda_1DEC)
    OP_22(0x85, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0xFF, 870, 100, -12290, 0, 0, 0, 1600, 1600, 1600, 0xFF, 0, 0, 0, 0)

    def lambda_1E41():
        OP_91(0xFE, 0x0, 0xFFFFEC78, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1E41)
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
        "#1078F#5P哦哦……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1444F#5P那是……\x02",
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

    def lambda_1FCB():
        OP_6D(1280, 0, -11070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FCB)

    def lambda_1FE3():
        OP_67(0, 6490, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FE3)

    def lambda_1FFB():
        OP_6B(2180, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1FFB)

    def lambda_200B():
        OP_6E(382, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_200B)

    def lambda_201B():
        OP_8E(0xFE, 0x33E, 0x0, 0xFFFFD526, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_201B)
    Sleep(450)

    def lambda_203B():
        OP_8E(0xFE, 0x28A, 0x0, 0xFFFFDB52, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_203B)
    Sleep(150)

    def lambda_205B():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0xFFFFE1D8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_205B)
    Sleep(150)

    def lambda_207B():
        OP_8E(0xFE, 0x514, 0x0, 0xFFFFE0B6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_207B)
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
        "\x07\x00得到了\x1F\x56\x03\x07\x00。\x02",
    )

    Jump("loc_2108")

    label("loc_2108")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x356, 1)

    ChrTalk(    #23
        0x10F,
        (
            "#1442F#5P……难道，\x01",
            "那是优胜奖品？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1840F#5P哈哈，看起来是呢。\x02\x03",

            "#1075F该说对方很正直呢，\x01",
            "还是遵守规则呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FE")

    ChrTalk(    #25
        0x10D,
        (
            "#272F哼……\x01",
            "不知道是谁的安排，\x01",
            "还真是费了一番工夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2291")

    label("loc_21FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_224E")

    ChrTalk(    #26
        0x10E,
        (
            "#176F不知道是谁干的，\x01",
            "净在无关紧要的地方下功夫……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2291")

    label("loc_224E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2291")

    ChrTalk(    #27
        0x10B,
        (
            "#413F不知道是谁干的，\x01",
            "还真是闲得发慌啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2291")

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
            "#1060F#2P好了……\x01",
            "这下就是第五个封印石了。\x02\x03",

            "我们先回据点一趟，\x01",
            "把里面的人解放出来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2362")

    ChrTalk(    #29
        0x107,
        "#560F#6P是、是啊～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C5")

    label("loc_2362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2396")

    ChrTalk(    #30
        0x10E,
        "#170F#6P嗯，就这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C5")

    label("loc_2396")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C5")

    ChrTalk(    #31
        0x10D,
        "#277F#6P啊，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_23C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241A")

    ChrTalk(    #32
        0x10B,
        (
            "#210F#6P嗯……\x01",
            "能被封进那样的石头中\x01",
            "还真是有些难以置信……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241A")

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

    # Function_19_1B94 end

    def Function_20_24D8(): pass

    label("Function_20_24D8")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_20_24D8 end

    SaveToFile()

Try(main)
