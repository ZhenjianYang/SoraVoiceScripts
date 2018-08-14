from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3112   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3112.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '希德中校',                             # 9
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '王国军士兵',                           # 12
        '王国军士兵',                           # 13
        '王国军士兵',                           # 14
        '王国军士兵',                           # 15
        '',                                     # 16
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
        'ED6_DT27/CH03590 ._CH',             # 00
        'ED6_DT27/CH04590 ._CH',             # 01
        'ED6_DT27/CH04591 ._CH',             # 02
        'ED6_DT27/CH04596 ._CH',             # 03
        'ED6_DT27/CH04594 ._CH',             # 04
        'ED6_DT27/CH04595 ._CH',             # 05
        'ED6_DT07/CH00320 ._CH',             # 06
        'ED6_DT07/CH00321 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03590P._CP',             # 00
        'ED6_DT27/CH04590P._CP',             # 01
        'ED6_DT27/CH04591P._CP',             # 02
        'ED6_DT27/CH04596P._CP',             # 03
        'ED6_DT27/CH04594P._CP',             # 04
        'ED6_DT27/CH04595P._CP',             # 05
        'ED6_DT07/CH00320P._CP',             # 06
        'ED6_DT07/CH00321P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1CA",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_1E8",          # 02, 2
        "Function_3_1F1",          # 03, 3
        "Function_4_14B1",         # 04, 4
        "Function_5_1500",         # 05, 5
        "Function_6_154F",         # 06, 6
        "Function_7_159E",         # 07, 7
        "Function_8_15ED",         # 08, 8
        "Function_9_163C",         # 09, 9
        "Function_10_168B",        # 0A, 10
        "Function_11_241D",        # 0B, 11
    )


    def Function_0_1CA(): pass

    label("Function_0_1CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E6")
    Event(0, 2)

    label("loc_1E6")

    Return()

    # Function_0_1CA end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    Return()

    # Function_1_1E7 end

    def Function_2_1E8(): pass

    label("Function_2_1E8")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_1E8 end

    def Function_3_1F1(): pass

    label("Function_3_1F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x48, 0x2)
    OP_E0(238, 0x49, 0x3)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x3)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(240, 0x4D, 0x3)
    OP_E0(241, 0x4E, 0x2)
    OP_E0(241, 0x4F, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 9830, 0, 640, 270)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, -570, 0, -3980, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    SetChrPos(0xEF, -2180, 0, -3890, 0)
    SetChrPos(0xF2, -410, 0, -5470, 0)
    SetChrPos(0xF0, -2310, 0, -5500, 0)
    Jump("loc_35B")

    label("loc_2D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31A")
    SetChrPos(0xF0, -2180, 0, -3890, 0)
    SetChrPos(0xF1, -410, 0, -5470, 0)
    SetChrPos(0xEF, -2310, 0, -5500, 0)
    Jump("loc_35B")

    label("loc_31A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    SetChrPos(0xF1, -2180, 0, -3890, 0)
    SetChrPos(0xF0, -410, 0, -5470, 0)
    SetChrPos(0xEF, -2310, 0, -5500, 0)

    label("loc_35B")

    OP_6D(-380, 0, -3800, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #0
        0x10,
        "男性的声音",
        (
            "#6P欢迎光临……\x01",
            "这么说会比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_420")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_487")

    label("loc_420")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_487")

    label("loc_448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_487")

    label("loc_470")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_487")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51B")

    label("loc_4B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51B")

    label("loc_4DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_51B")

    label("loc_504")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_51B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AF")

    label("loc_548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AF")

    label("loc_570")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_598")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5AF")

    label("loc_598")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5AF")

    Sleep(1000)
    Fade(500)
    OP_6D(10510, 0, 1480, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #1
        0x109,
        "#1063F#2P希德中校……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10C,
        "#112F#2P……是你吗………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x109, 690, 0, -460, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69F")
    SetChrPos(0xEF, -470, 0, 1320, 90)
    SetChrPos(0xF1, -2240, 0, -810, 90)
    SetChrPos(0xF0, -840, 0, -1340, 90)
    Jump("loc_724")

    label("loc_69F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E3")
    SetChrPos(0xF0, -470, 0, 1320, 90)
    SetChrPos(0xF1, -2240, 0, -810, 90)
    SetChrPos(0xEF, -840, 0, -1340, 90)
    Jump("loc_724")

    label("loc_6E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    SetChrPos(0xF1, -470, 0, 1320, 90)
    SetChrPos(0xF0, -2240, 0, -810, 90)
    SetChrPos(0xEF, -840, 0, -1340, 90)

    label("loc_724")

    SetChrChipByIndex(0xEE, 8)
    SetChrChipByIndex(0xEF, 10)
    SetChrChipByIndex(0xF0, 12)
    SetChrChipByIndex(0xF1, 14)

    def lambda_73E():
        OP_6D(7820, 0, 2250, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_73E)

    def lambda_756():
        OP_67(0, 4690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_756)

    def lambda_76E():
        OP_6B(2950, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_76E)

    def lambda_77E():
        OP_6E(305, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_77E)
    Sleep(500)

    def lambda_793():
        OP_8F(0xFE, 0xF3C, 0x0, 0xFFFFFEC0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_793)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_819")

    def lambda_7C1():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_7C1)
    Sleep(100)

    def lambda_7E1():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_7E1)
    Sleep(100)

    def lambda_801():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_801)
    Jump("loc_8EE")

    label("loc_819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_885")

    def lambda_82D():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_82D)
    Sleep(100)

    def lambda_84D():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_84D)
    Sleep(100)

    def lambda_86D():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_86D)
    Jump("loc_8EE")

    label("loc_885")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE")

    def lambda_899():
        OP_8F(0xFE, 0xF8C, 0x0, 0x564, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_899)
    Sleep(100)

    def lambda_8B9():
        OP_8F(0xFE, 0x88E, 0x0, 0x4C4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8B9)
    Sleep(100)

    def lambda_8D9():
        OP_8F(0xFE, 0x820, 0x0, 0xFFFFFD58, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8D9)

    label("loc_8EE")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #3
        0x10,
        (
            "#701F#11P凯文神父……\x01",
            "看来你被折腾得够呛吧。\x02\x03",

            "我可一点都没有想到\x01",
            "会变成这个样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x109,
        (
            "#1068F#6P是啊……\x01",
            "简直就像是一场噩梦。\x02\x03",

            "#1063F不过……\x01",
            "看样子，你还记得我们\x01",
            "在大圣堂地下讨价还价时的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#703F#2P啊，虽然不知道\x01",
            "『我』是什么时候被再现于这里的……\x02\x03",

            "#700F但是的确有那时的记忆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1067F#6P嗯……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")

    ChrTalk(    #7
        0x10F,
        "#1443F#6P这似乎有什么深刻的含义……\x02",
    )

    CloseMessageWindow()

    label("loc_AB3")


    ChrTalk(    #8
        0x10,
        (
            "#703F#11P理查德先生。\x01",
            "好久不见了。\x02\x03",

            "#701F没有想到\x01",
            "竟然会是以这种方式\x01",
            "与您再次相遇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10C,
        (
            "#119F#6P哈哈……我也是。\x02\x03",

            "#118F但是如果前锋是你的话，\x01",
            "可以想象接下来的战斗会有多么艰难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#701F#11P呵呵，您过谦了。\x02\x03",

            "#703F不过我也不打算……\x01",
            "就这样轻易地输给你们。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 5)

    def lambda_C0F():

        label("loc_C0F")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_C0F")

    QueueWorkItem2(0x10, 3, lambda_C0F)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 9470, 100, 3510, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 6730, 100, 4930, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, 3450, 100, 5170, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 9430, 100, -2260, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 6420, 100, -4250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0xFF, 2980, 100, -4470, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC6")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E2D")

    label("loc_DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEE")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E2D")

    label("loc_DEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E16")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E2D")

    label("loc_E16")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E2D")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5A")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC1")

    label("loc_E5A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E82")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC1")

    label("loc_E82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAA")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EC1")

    label("loc_EAA")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EC1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EEE")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F55")

    label("loc_EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F16")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F55")

    label("loc_F16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F55")

    label("loc_F3E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F55")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F82")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FE9")

    label("loc_F82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FE9")

    label("loc_FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FE9")

    label("loc_FD2")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FE9")

    Sleep(1000)

    def lambda_FF4():
        OP_6D(7180, 0, 1230, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_FF4)

    def lambda_100C():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_100C)

    def lambda_1024():
        OP_6B(3320, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1024)

    def lambda_1034():
        OP_6E(255, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1034)

    def lambda_1044():
        OP_6C(56000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1044)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x11, 9470, -3000, 3510, 225)
    SetChrPos(0x12, 6730, -3000, 4930, 225)
    SetChrPos(0x13, 3450, -3000, 5170, 225)
    SetChrPos(0x14, 9430, -3000, -2260, 270)
    SetChrPos(0x15, 6420, -3000, -4250, 315)
    SetChrPos(0x16, 2980, -3000, -4470, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_10DD():

        label("loc_10DD")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_10DD")

    QueueWorkItem2(0x109, 3, lambda_10DD)
    OP_43(0x11, 0x0, 0x0, 0x4)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_43(0x13, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x7)
    OP_43(0x15, 0x0, 0x0, 0x8)
    OP_43(0x16, 0x0, 0x0, 0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116D")

    def lambda_1130():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1130)
    Sleep(50)

    def lambda_1143():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1143)
    Sleep(50)

    def lambda_1156():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1156)
    Sleep(50)
    OP_8C(0xF1, 0, 400)
    Jump("loc_120C")

    label("loc_116D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BE")

    def lambda_1181():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1181)
    Sleep(50)

    def lambda_1194():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1194)
    Sleep(50)

    def lambda_11A7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11A7)
    Sleep(50)
    OP_8C(0xF1, 0, 400)
    Jump("loc_120C")

    label("loc_11BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120C")

    def lambda_11D2():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_11D2)
    Sleep(50)

    def lambda_11E5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_11E5)
    Sleep(50)

    def lambda_11F8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11F8)
    Sleep(50)
    OP_8C(0xF0, 0, 400)

    label("loc_120C")

    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10, 0x3)
    OP_23(0x85)
    OP_1D(0xC4)
    Fade(1000)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x109,
        "#1063F#6P嘁……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10C,
        "#112F#6P被包围了吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#703F#11P王国军中校，\x01",
            "马克西米利安·希德……\x02\x03",

            "#704F以雷斯顿要塞\x01",
            "原守备队长的名义\x01",
            "阻止你们的行动……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    Sleep(150)
    SetChrSubChip(0x10, 1)
    Sleep(100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1377():
        OP_6D(5800, 0, 1100, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1377)

    def lambda_138F():
        OP_67(0, 7350, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_138F)

    def lambda_13A7():
        OP_6B(2580, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_13A7)

    def lambda_13B7():
        OP_6E(240, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_13B7)
    SetChrChipByIndex(0x11, 7)

    def lambda_13CC():
        OP_8F(0xFE, 0x1914, 0x0, 0x55A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_13CC)
    SetChrChipByIndex(0x12, 7)

    def lambda_13EC():
        OP_8F(0xFE, 0x13A6, 0x0, 0x8A2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_13EC)
    SetChrChipByIndex(0x13, 7)

    def lambda_140C():
        OP_8F(0xFE, 0xC94, 0x0, 0x910, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_140C)
    SetChrChipByIndex(0x14, 7)
    OP_8C(0x14, 315, 0)

    def lambda_1433():
        OP_8F(0xFE, 0x17DE, 0x0, 0xFFFFFDB2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1433)
    SetChrChipByIndex(0x15, 7)
    OP_8C(0x15, 0, 0)

    def lambda_145A():
        OP_8F(0xFE, 0x12F2, 0x0, 0xFFFFFB5A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_145A)
    SetChrChipByIndex(0x16, 7)

    def lambda_147A():
        OP_8F(0xFE, 0xC4E, 0x0, 0xFFFFF8C6, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_147A)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_1F1 end

    def Function_4_14B1(): pass

    label("Function_4_14B1")

    PlayEffect(0x1, 0xFF, 0xFF, 9470, 100, 3510, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_14B1 end

    def Function_5_1500(): pass

    label("Function_5_1500")

    PlayEffect(0x1, 0xFF, 0xFF, 6730, 100, 4930, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_1500 end

    def Function_6_154F(): pass

    label("Function_6_154F")

    PlayEffect(0x1, 0xFF, 0xFF, 3450, 100, 5170, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_154F end

    def Function_7_159E(): pass

    label("Function_7_159E")

    PlayEffect(0x1, 0xFF, 0xFF, 9430, 100, -2260, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_159E end

    def Function_8_15ED(): pass

    label("Function_8_15ED")

    PlayEffect(0x1, 0xFF, 0xFF, 6420, 100, -4250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_15ED end

    def Function_9_163C(): pass

    label("Function_9_163C")

    PlayEffect(0x1, 0xFF, 0xFF, 2980, 100, -4470, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_163C end

    def Function_10_168B(): pass

    label("Function_10_168B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 8220, 0, 800, 270)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xB)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, 5360, 0, -400, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B7")
    SetChrPos(0xEF, 5560, 0, 1260, 90)
    SetChrPos(0xF1, 3720, 0, 1170, 90)
    SetChrPos(0xF0, 3700, 0, -530, 90)
    Jump("loc_183C")

    label("loc_17B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FB")
    SetChrPos(0xF0, 5560, 0, 1260, 90)
    SetChrPos(0xF1, 3720, 0, 1170, 90)
    SetChrPos(0xEF, 3700, 0, -530, 90)
    Jump("loc_183C")

    label("loc_17FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183C")
    SetChrPos(0xF1, 5560, 0, 1260, 90)
    SetChrPos(0xF0, 3720, 0, 1170, 90)
    SetChrPos(0xEF, 3700, 0, -530, 90)

    label("loc_183C")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(7460, 0, 1820, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(45000, 0)
    OP_6E(273, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #14
        0x10,
        (
            "#703F#11P呵呵……\x01",
            "不愧是理查德先生。\x02\x03",

            "#701F再加上星杯骑士，\x01",
            "我方的失败也是理所当然的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10C,
        (
            "#110F#6P请别这么谦虚……\x01",
            "你已经让我见识了如铜墙铁壁般的布阵。\x02\x03",

            "关于指挥的能力，\x01",
            "你已经超过我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#701F#11P呵呵……我还差得很远。\x02\x03",

            "#703F因为是在这种场合，　\x01",
            "我才敢冒昧说这样的话……\x02\x03",

            "#700F理查德前辈。\x01",
            "自从您离开王国军之后，\x01",
            "我们实在深感惋惜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10C,
        (
            "#119F#6P哈哈……\x01",
            "就像当初准将退役那样，\x01",
            "我能够体会你的感受。\x02\x03",

            "#111F我们已经分道扬镳，\x01",
            "我走我的剑道，你从你的军道，\x01",
            "各自继承准将的衣钵。\x02\x03",

            "但是，即便道路不同，\x01",
            "也可以有共同的志向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "#701F#11P呵呵……确实。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    PlayEffect(0x0, 0x0, 0x10, -100, 800, 100, 0, 0, 0, 2200, 3500, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)

    def lambda_1B8B():

        label("loc_1B8B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1B8B")

    QueueWorkItem2(0x109, 3, lambda_1B8B)

    def lambda_1B9C():
        OP_6D(7050, 0, 1890, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1B9C)
    OP_8F(0x10, 0x1B58, 0x0, 0x3E8, 0x3E8, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #19
        0x10,
        "#701F#11P……请收下这个。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x00得到了\x1F\x32\x03\x07\x00。\x02",
    )

    Jump("loc_1C23")

    label("loc_1C23")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x332, 1)
    OP_8F(0x10, 0x1F40, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_44(0x109, 0x3)
    Sleep(300)

    ChrTalk(    #21
        0x10C,
        "#113F#6P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#703F#11P呵呵，前辈刚才也说过了，\x01",
            "我只不过是个先锋……\x02\x03",

            "#701F你们最好抱持着\x01",
            "试炼才刚刚开始的觉悟。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E08")
    Sleep(500)

    ChrTalk(    #23
        0x10,
        (
            "#703F#11P凯文神父，莉丝小姐……\x01",
            "拜托你们了。\x02\x03",

            "#700F殿下、舒华兹上尉、\x01",
            "理查德先生，\x01",
            "还有艾丝蒂尔他们……\x02\x03",

            "当然，也包括你们在内。\x01",
            "请引导每一个人\x01",
            "平安逃离这个世界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10F,
        "#1802F#6P希德中校……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1840F#6P嗯……\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE3")

    label("loc_1E08")

    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#703F#2P凯文神父……\x01",
            "拜托你了。\x02\x03",

            "#700F殿下、舒华兹上尉、\x01",
            "理查德先生，\x01",
            "还有艾丝蒂尔他们……\x02\x03",

            "当然，也包括你们在内。\x01",
            "请引导每一个人\x01",
            "平安逃离这个世界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1840F#6P嗯……\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE3")

    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -600, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_1F2D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F2D)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_1F4C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F4C)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    OP_6D(6450, 0, 1710, 1000)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB0")

    ChrTalk(    #28
        0x107,
        "#063F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2006")

    label("loc_1FB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FDC")

    ChrTalk(    #29
        0x10A,
        "#813F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2006")

    label("loc_1FDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2006")

    ChrTalk(    #30
        0x10F,
        "#1445F#6P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_2006")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_203A")

    ChrTalk(    #31
        0x10E,
        "#176F#6P真是耿直啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_213F")

    label("loc_203A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207B")

    ChrTalk(    #32
        0x106,
        (
            "#552F#6P哼……\x01",
            "还是那样有板有眼啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213F")

    label("loc_207B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BC")

    ChrTalk(    #33
        0x103,
        "#1534F#6P呵呵……真是个耿直的人啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_213F")

    label("loc_20BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2101")

    ChrTalk(    #34
        0x10B,
        (
            "#215F#6P好、好像是个\x01",
            "非常正直的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213F")

    label("loc_2101")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_213F")

    ChrTalk(    #35
        0x110,
        (
            "#267F#6P呼……\x01",
            "好像是个很正直的人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2183")

    ChrTalk(    #36
        0x105,
        (
            "#1383F#6P呵呵……\x01",
            "真像希德先生的作风。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C2")

    label("loc_2183")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C2")

    ChrTalk(    #37
        0x101,
        (
            "#1025F#6P呵呵……\x01",
            "这才像希德先生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FB")

    ChrTalk(    #38
        0x10D,
        "#278F#6P……这就是王国军人吗。\x02",
    )

    CloseMessageWindow()

    label("loc_21FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_223A")

    ChrTalk(    #39
        0x104,
        (
            "#1541F#6P呼……\x01",
            "的确是军人的楷模啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_223A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(    #40
        0x102,
        "#1513F#6P……是个了不起的人物啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22B7")

    label("loc_2279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B7")

    ChrTalk(    #41
        0x108,
        (
            "#070F#6P哈哈……\x01",
            "是个了不起的兄弟。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B7")


    ChrTalk(    #42
        0x10C,
        "#116F#5P……………………………\x02",
    )

    CloseMessageWindow()

    def lambda_22E8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_22E8)
    Sleep(200)
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #43
        0x10C,
        (
            "#110F#5P……我们继续前进吧。\x02\x03",

            "难得中校\x01",
            "给我们指明了道路。\x02",
        )
    )

    Jump("loc_2359")

    label("loc_2359")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23BF")

    ChrTalk(    #44
        0x109,
        "#1060F#12P嗯，知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10F,
        (
            "#1806F#6P接下来\x01",
            "应该是去『兵营』吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240C")

    label("loc_23BF")


    ChrTalk(    #46
        0x109,
        (
            "#1075F#12P嗯，知道了。\x02\x03",

            "#1060F接下来\x01",
            "应该是去『兵营』吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_240C")

    OP_A2(0x2B1A)
    OP_28(0x39, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_10_168B end

    def Function_11_241D(): pass

    label("Function_11_241D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243E")
    Sleep(100)
    Jump("loc_24B9")

    label("loc_243E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2453")
    Sleep(200)
    Jump("loc_24B9")

    label("loc_2453")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2468")
    Sleep(300)
    Jump("loc_24B9")

    label("loc_2468")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247D")
    Sleep(400)
    Jump("loc_24B9")

    label("loc_247D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2492")
    Sleep(500)
    Jump("loc_24B9")

    label("loc_2492")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A7")
    Sleep(600)
    Jump("loc_24B9")

    label("loc_24A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B9")
    Sleep(700)

    label("loc_24B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24DB")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_24B9")

    label("loc_24DB")

    Return()

    # Function_11_241D end

    SaveToFile()

Try(main)
