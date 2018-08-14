from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M5415   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5415.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60114",
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
        '莱维',                                 # 9
        '黑骑士',                               # 10
        '德尔基昂初号机',                       # 11
        '德尔基昂贰号机',                       # 12
        '露菲娜',                               # 13
        '',                                     # 14
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
        'ED6_DT27/CH03440 ._CH',             # 00
        'ED6_DT27/CH04450 ._CH',             # 01
        'ED6_DT27/CH04454 ._CH',             # 02
        'ED6_DT27/CH04455 ._CH',             # 03
        'ED6_DT26/CH20710 ._CH',             # 04
        'ED6_DT26/CH20711 ._CH',             # 05
        'ED6_DT27/CH03940 ._CH',             # 06
        'ED6_DT26/CH20733 ._CH',             # 07
        'ED6_DT27/CH04082 ._CH',             # 08
        'ED6_DT27/CH04080 ._CH',             # 09
        'ED6_DT26/CH20731 ._CH',             # 0A
        'ED6_DT26/CH20734 ._CH',             # 0B
        'ED6_DT26/CH20735 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT27/CH03440P._CP',             # 00
        'ED6_DT27/CH04450P._CP',             # 01
        'ED6_DT27/CH04454P._CP',             # 02
        'ED6_DT27/CH04455P._CP',             # 03
        'ED6_DT26/CH20710P._CP',             # 04
        'ED6_DT26/CH20711P._CP',             # 05
        'ED6_DT27/CH03940P._CP',             # 06
        'ED6_DT26/CH20733P._CP',             # 07
        'ED6_DT27/CH04082P._CP',             # 08
        'ED6_DT27/CH04080P._CP',             # 09
        'ED6_DT26/CH20731P._CP',             # 0A
        'ED6_DT26/CH20734P._CP',             # 0B
        'ED6_DT26/CH20735P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0xC5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4250,
        Y                   = 14000,
        Z                   = -17850,
        Range               = 3950,
        Unknown_10          = 0x4650,
        Unknown_14          = 0xFFFFC84C,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_1D2",          # 00, 0
        "Function_1_223",          # 01, 1
        "Function_2_258",          # 02, 2
        "Function_3_269",          # 03, 3
        "Function_4_2F44",         # 04, 4
        "Function_5_4FF0",         # 05, 5
        "Function_6_5027",         # 06, 6
        "Function_7_504A",         # 07, 7
        "Function_8_5CDE",         # 08, 8
        "Function_9_87C2",         # 09, 9
    )


    def Function_0_1D2(): pass

    label("Function_0_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_222")

    label("loc_1EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_206")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_222")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_222")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_222")

    Return()

    # Function_0_1D2 end

    def Function_1_223(): pass

    label("Function_1_223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248")
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_248")

    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    Return()

    # Function_1_223 end

    def Function_2_258(): pass

    label("Function_2_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_260")
    Return()

    label("loc_260")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_258 end

    def Function_3_269(): pass

    label("Function_3_269")

    EventBegin(0x0)
    LoadEffect(0x0, "monster\\ms30803a.eff")
    LoadEffect(0x1, "map\\mp021_00.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    LoadEffect(0x3, "scraft\\sc000_33.eff")
    LoadEffect(0x4, "monster\\ms30803c.eff")
    LoadEffect(0x5, "monster\\ms30803d.eff")
    LoadEffect(0x6, "map\\mpM54_02")
    OP_E0(238, 0x4D, 0x2)
    OP_E0(238, 0x4E, 0x3)
    OP_E0(239, 0x4F, 0x2)
    OP_E0(239, 0x50, 0x3)
    OP_E0(240, 0x51, 0x2)
    OP_E0(240, 0x52, 0x3)
    OP_E0(241, 0x53, 0x2)
    OP_E0(241, 0x54, 0x3)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 0, 15550, 3500, 180)
    SetChrSubChip(0x10, 0)

    NpcTalk(    #0
        0x10,
        "男子的声音",
        (
            "\x07\x05#4P——欢迎光临。\x02\x03",

            "灭亡故里的遗孤……\x01",
            "以及背负着圣痕的赎罪者啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_443")

    label("loc_3DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_443")

    label("loc_404")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_443")

    label("loc_42C")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_443")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_470")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4D7")

    label("loc_470")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_498")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4D7")

    label("loc_498")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4D7")

    label("loc_4C0")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4D7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_504")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56B")

    label("loc_504")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56B")

    label("loc_52C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_554")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_56B")

    label("loc_554")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_56B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_598")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF")

    label("loc_598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF")

    label("loc_5C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF")

    label("loc_5E8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5FF")

    Sleep(1000)

    def lambda_60A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_60A)

    def lambda_61C():
        OP_6D(0, 15550, 4000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_61C)

    def lambda_634():
        OP_67(0, 2960, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_634)

    def lambda_64C():
        OP_6B(1930, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_64C)

    def lambda_65C():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_65C)

    def lambda_66C():
        OP_6E(444, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_66C)

    def lambda_67C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_67C)

    def lambda_68A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_68A)

    def lambda_698():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_698)

    def lambda_6A6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_6A6)
    WaitChrThread(0xEE, 0x0)
    SetChrPos(0x109, 500, 15550, -8540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E6")
    SetChrPos(0xEF, -300, 15550, -8540, 0)
    Jump("loc_727")

    label("loc_6E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")
    SetChrPos(0xF0, -300, 15550, -8540, 0)
    Jump("loc_727")

    label("loc_708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    SetChrPos(0xF1, -300, 15550, -8540, 0)

    label("loc_727")

    Sleep(300)

    ChrTalk(    #1
        0x102,
        "#1502F#5P……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        "#1069F#5P在这里等着吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(660, 15550, -130, 0)
    OP_67(0, 4750, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(485, 0)
    SetChrPos(0x109, 910, 15550, -9540, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80C")
    SetChrPos(0xEF, -590, 15550, -8650, 0)
    SetChrPos(0xF0, 830, 15550, -11370, 0)
    SetChrPos(0xF1, -1590, 15550, -11870, 0)
    Jump("loc_891")

    label("loc_80C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    SetChrPos(0xF0, -590, 15550, -8650, 0)
    SetChrPos(0xEF, 830, 15550, -11370, 0)
    SetChrPos(0xF1, -1590, 15550, -11870, 0)
    Jump("loc_891")

    label("loc_850")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")
    SetChrPos(0xF1, -590, 15550, -8650, 0)
    SetChrPos(0xEF, 830, 15550, -11370, 0)
    SetChrPos(0xF0, -1590, 15550, -11870, 0)

    label("loc_891")


    def lambda_897():
        OP_6B(2100, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_897)
    SetChrPos(0x10, 0, 15550, 3800, 180)

    def lambda_8B8():
        OP_8F(0xFE, 0xFFFFFFF6, 0x3CBE, 0xFFFFEF5C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8B8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92F")

    def lambda_8E1():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8E1)

    def lambda_8FC():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8FC)

    def lambda_917():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_917)
    Jump("loc_9F0")

    label("loc_92F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")

    def lambda_943():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_943)

    def lambda_95E():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_95E)

    def lambda_979():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_979)
    Jump("loc_9F0")

    label("loc_991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F0")

    def lambda_9A5():
        OP_8F(0xFE, 0xFFFFFA2E, 0x3CBE, 0xFFFFEFFC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_9A5)

    def lambda_9C0():
        OP_8F(0xFE, 0xFFFFFF6A, 0x3CBE, 0xFFFFE980, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_9C0)

    def lambda_9DB():
        OP_8F(0xFE, 0xFFFFF84E, 0x3CBE, 0xFFFFE96C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_9DB)

    label("loc_9F0")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(500)

    NpcTalk(    #3
        0x10,
        "黑骑士",
        (
            "\x07\x05#1590F#5P『王』精心策划的棋盘，\x01",
            "终于演绎至如今一幕。\x02\x03",

            "只要击败作为最后守护者的本人，\x01",
            "你们就可见到『第六星层』的尽头。\x02\x03",

            "#1591F哈哈，当然……\x01",
            "这可是一场近乎不可能完成的试炼。\x07\x00\x02",
        )
    )

    Jump("loc_AE8")

    label("loc_AE8")

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#1502F#6P…………………………………\x02\x03",

            "#1505F有一件事……\x01",
            "能否请教一下？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    NpcTalk(    #5
        0x10,
        "黑骑士",
        "\x07\x05#1592F#5P什么……？\x07\x00\x02",
    )

    Jump("loc_B8D")

    label("loc_B8D")

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1503F#6P…………………………………\x02\x03",

            "#1505F为什么……\x02\x03",

            "#1502F为什么……\x01",
            "你非得戴着那个面具，\x01",
            "不以真面目示人？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10,
        "黑骑士",
        (
            "\x07\x05#1591F#5P呵呵……\x01",
            "还以为你要问什么难题呢。\x02\x03",

            "『王』希望我以如此姿态行事……\x01",
            "除此之外，还有更重要的理由吗？\x07\x00\x02",
        )
    )

    Jump("loc_CA6")

    label("loc_CA6")

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #8
        0x102,
        "#1506F#6P不对……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #9
        0x102,
        (
            "#1505F#6P或许，\x01",
            "你留守于此的目的确实如此。\x02\x03",

            "#1506F但是，\x01",
            "带上面具并不是『影之王』的要求！\x02\x03",

            "其理由绝非如此！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #10
        0x10,
        "黑骑士",
        "\x07\x05#1590F#5P…………………………………\x07\x00\x02",
    )

    Jump("loc_DC7")

    label("loc_DC7")

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        "#1067F#12P约修亚……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #12
        0x101,
        "#1003F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_E21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E58")

    ChrTalk(    #13
        0x10B,
        "#215F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_E58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E90")

    ChrTalk(    #14
        0x105,
        "#1169F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_E90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ECB")

    ChrTalk(    #15
        0x107,
        "#063F#12P……约修亚哥哥………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F03")

    ChrTalk(    #16
        0x103,
        "#1532F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3D")

    ChrTalk(    #17
        0x104,
        "#1551F#12P……约修亚君………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_F3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F78")

    ChrTalk(    #18
        0x106,
        "#552F#12P……约修亚，你………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_F78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FB3")

    ChrTalk(    #19
        0x108,
        "#572F#12P……约修亚，你………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEA")

    ChrTalk(    #20
        0x10E,
        "#175F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_101D")

    ChrTalk(    #21
        0x10D,
        "#276F#12P……你………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1054")

    ChrTalk(    #22
        0x10C,
        "#116F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_1054")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108C")

    ChrTalk(    #23
        0x110,
        "#1300F#12P……约修亚………\x02",
    )

    CloseMessageWindow()
    Jump("loc_10BD")

    label("loc_108C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")

    ChrTalk(    #24
        0x10A,
        "#1317F#12P呃，嗯……？\x02",
    )

    CloseMessageWindow()

    label("loc_10BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FD")

    ChrTalk(    #25
        0x10F,
        "#1802F#12P（……在说什么………？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_10FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1135")

    ChrTalk(    #26
        0x10A,
        "#1317F#12P（唔，那个……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_1135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1177")

    ChrTalk(    #27
        0x110,
        "#1300F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_1177")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B8")

    ChrTalk(    #28
        0x10C,
        "#115F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_11B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(    #29
        0x10D,
        "#272F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_11F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_123A")

    ChrTalk(    #30
        0x10E,
        "#176F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_123A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127B")

    ChrTalk(    #31
        0x108,
        "#074F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_127B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12BC")

    ChrTalk(    #32
        0x106,
        "#552F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_12BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12FE")

    ChrTalk(    #33
        0x104,
        "#1551F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_12FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1340")

    ChrTalk(    #34
        0x103,
        "#1532F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_1340")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #35
        0x107,
        "#063F#12P……哥哥………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_1375")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B7")

    ChrTalk(    #36
        0x105,
        "#1169F#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_13F5")

    label("loc_13B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F5")

    ChrTalk(    #37
        0x10B,
        "#215F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_13F5")


    ChrTalk(    #38
        0x102,
        (
            "#1505F#6P果然……\x01",
            "大家都察觉了吧。\x02\x03",

            "#1514F我实在是太懦弱了……\x01",
            "真是非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        (
            "#1075F#12P什么嘛……\x01",
            "怎么把责任都揽在自己身上了。\x02\x03",

            "#1840F其实我们确实也都猜到\x01",
            "大概是那么回事了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14FE")

    ChrTalk(    #40
        0x101,
        "#1025F#12P嗯……是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_14FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1531")

    ChrTalk(    #41
        0x10B,
        "#413F#12P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1531")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1563")

    ChrTalk(    #42
        0x105,
        "#1382F#12P……是呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1563")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A0")

    ChrTalk(    #43
        0x107,
        "#562F#12P……唉、唉………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_15A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D2")

    ChrTalk(    #44
        0x103,
        "#1534F#12P……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_15D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(    #45
        0x104,
        "#1545F#12P呵……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1606")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1637")

    ChrTalk(    #46
        0x106,
        "#556F#12P……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1637")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1668")

    ChrTalk(    #47
        0x108,
        "#573F#12P……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1668")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1699")

    ChrTalk(    #48
        0x10E,
        "#170F#12P……的确。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_1699")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16CA")

    ChrTalk(    #49
        0x10D,
        "#277F#12P……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16F8")

    label("loc_16CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F8")

    ChrTalk(    #50
        0x10C,
        "#119F#12P……确实。\x02",
    )

    CloseMessageWindow()

    label("loc_16F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1761")

    ChrTalk(    #51
        0x110,
        (
            "#268F#12P玲呢……\x01",
            "一早就发现了哦。\x02\x03",

            "#1300F总觉得……\x01",
            "不方便说出来罢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1761")


    NpcTalk(    #52
        0x10,
        "黑骑士",
        (
            "\x07\x05#1590F#5P……虽然不知道\x01",
            "你们明白了什么事情……\x02\x03",

            "#1591F但是如果觉得那是真相的话，\x01",
            "就开门见山地说出来吧。\x02\x03",

            "哼哼，\x01",
            "只要你们有能说出来的勇气。\x07\x00\x02",
        )
    )

    Jump("loc_1822")

    label("loc_1822")

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#1505F#6P……我拒绝。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #54
        0x10,
        "黑骑士",
        "\x07\x05#1592F#5P………什么………………\x07\x00\x02",
    )

    Jump("loc_18A0")

    label("loc_18A0")

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1514F#6P你的真面目，\x01",
            "只要用我们的力量剥去那面具，\x01",
            "就能知道……\x02\x03",

            "我们现在所能确定的是……\x01",
            "不渡过这道难关，\x01",
            "就没有未来可言这件事而已。\x02\x03",

            "#1513F——那么现在\x01",
            "没有必要去管你的真面目是什么。\x02\x03",

            "我不会再迷惘，\x01",
            "更不会逃避……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_19AA():
        OP_6B(2000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_19AA)
    OP_22(0x1F5, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D4")
    SetChrChipByIndex(0x102, 15)
    SetChrSubChip(0x102, 0)
    Jump("loc_1A07")

    label("loc_19D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19EF")
    SetChrChipByIndex(0x102, 17)
    SetChrSubChip(0x102, 0)
    Jump("loc_1A07")

    label("loc_19EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A07")
    SetChrChipByIndex(0x102, 19)
    SetChrSubChip(0x102, 0)

    label("loc_1A07")

    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x102,
        (
            "#1506F#6P#2S只有赌上自己的一切，\x01",
            "通过你这道试炼！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #57
        0x109,
        "#1840F#12P约修亚……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD0")

    ChrTalk(    #58
        0x101,
        (
            "#1012F#12P约修亚……\x02\x03",

            "#1006F嗯，算上我一个！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B0B")

    ChrTalk(    #59
        0x108,
        (
            "#071F#12P哈哈……\x01",
            "决心下得好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B41")

    ChrTalk(    #60
        0x10D,
        "#275F#12P呼……就是这气势。\x02",
    )

    CloseMessageWindow()

    label("loc_1B41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B8E")

    ChrTalk(    #61
        0x106,
        (
            "#051F#12P呵，\x01",
            "我也想借此让你偿还那时欠下的债呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD9")

    ChrTalk(    #62
        0x10E,
        (
            "#179F#12P现在，\x01",
            "为了再度驱散利贝尔国中的阴影……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C21")

    ChrTalk(    #63
        0x10F,
        (
            "#1447F#12P……为了通过试炼，\x01",
            "得到明日的光明。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6A")

    ChrTalk(    #64
        0x10C,
        (
            "#118F#12P政变事件时欠的债……\x01",
            "就在此地偿还吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CBE")

    ChrTalk(    #65
        0x103,
        (
            "#1521F#12P好，既然你下定这样的决心，\x01",
            "我自然要尽力帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D0E")

    ChrTalk(    #66
        0x104,
        (
            "#1541F#12P那么，我就为了爱，\x01",
            "而成为约修亚君的支柱吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D4A")

    ChrTalk(    #67
        0x105,
        (
            "#1168F#12P呵呵……\x01",
            "也让我帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8B")

    ChrTalk(    #68
        0x107,
        (
            "#066F#12P约修亚哥哥……\x01",
            "我也要帮忙哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCA")

    ChrTalk(    #69
        0x10B,
        (
            "#415F#12P嘿嘿，\x01",
            "这种事我也要帮忙啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0B")

    ChrTalk(    #70
        0x110,
        (
            "#261F#12P嘻嘻，没办法，\x01",
            "玲也来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E54")

    ChrTalk(    #71
        0x10A,
        (
            "#819F#12P虽、虽然不大清楚状况，\x01",
            "也让我帮忙吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E54")

    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 13)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EA6")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 19)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1F0B")

    label("loc_1EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDA")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 15)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 19)
    SetChrSubChip(0xF1, 0)
    Jump("loc_1F0B")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0B")
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 15)
    SetChrSubChip(0xEF, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 17)
    SetChrSubChip(0xF0, 0)

    label("loc_1F0B")

    OP_0D()
    Sleep(500)

    NpcTalk(    #72
        0x10,
        "黑骑士",
        "\x07\x05#1590F#5P……呼呼…………\x07\x00\x02",
    )

    Jump("loc_1F4A")

    label("loc_1F4A")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #73
        0x10,
        "黑骑士",
        "\x07\x05#1591F#5P#4S哈哈哈哈哈哈哈哈哈哈！\x07\x00\x02",
    )

    Jump("loc_1F92")

    label("loc_1F92")

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_1FB4():
        OP_6D(800, 15550, 1000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1FB4)

    def lambda_1FCC():
        OP_6B(1950, 500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1FCC)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #74
        0x10,
        "黑骑士",
        (
            "\x07\x05#1591F#5P真没想到\x01",
            "你会如此坦率啊！\x02\x03",

            "#1593F好吧，那你就用实力\x01",
            "来揭示我的真面目吧！\x07\x00\x02",
        )
    )

    Jump("loc_2063")

    label("loc_2063")

    CloseMessageWindow()
    Sleep(150)
    OP_20(0x5DC)
    Fade(500)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)

    def lambda_2083():

        label("loc_2083")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2083")

    QueueWorkItem2(0x10, 3, lambda_2083)
    PlayEffect(0x2, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x158, 0x1, 0x64)

    def lambda_20D6():

        label("loc_20D6")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_20D6")

    QueueWorkItem2(0x12, 3, lambda_20D6)

    def lambda_20F1():
        OP_6D(660, 15550, -130, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_20F1)

    def lambda_2109():
        OP_67(0, 5700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2109)

    def lambda_2121():
        OP_6B(2590, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2121)

    def lambda_2131():
        OP_6C(45000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2131)

    def lambda_2141():
        OP_6E(508, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2141)
    Sleep(1000)
    OP_1D(0x77)
    Fade(500)
    OP_6D(660, 15550, -130, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(45000, 0)
    OP_6E(508, 0)

    def lambda_219A():

        label("loc_219A")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_219A")

    QueueWorkItem2(0x12, 3, lambda_219A)

    def lambda_21B5():
        OP_6D(-4430, 30000, -5500, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_21B5)

    def lambda_21CD():
        OP_67(0, 6670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_21CD)

    def lambda_21E5():
        OP_6B(8990, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_21E5)

    def lambda_21F5():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_21F5)

    def lambda_2205():
        OP_6E(543, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2205)
    Sleep(1500)
    PlayEffect(0x6, 0x6, 0xFF, 90890, 0, -133260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2262():

        label("loc_2262")

        OP_7C(0x12C, 0x12C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2262")

    QueueWorkItem2(0x12, 3, lambda_2262)
    OP_6D(-4430, 30000, -5500, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(8990, 0)
    OP_6C(47000, 0)
    OP_6E(543, 0)

    def lambda_22BA():
        OP_6D(-4430, 100000, -5500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_22BA)

    def lambda_22D2():
        OP_67(0, -1670, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_22D2)

    def lambda_22EA():
        OP_6B(9300, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_22EA)

    def lambda_22FA():
        OP_6C(25000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_22FA)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -80850, 90000, -65000, 90)
    OP_A1(0x13, 0x1)
    OP_D1(19, 10000, 90000, 30000, 0)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 320)
    OP_70(0x1, 0x140)
    OP_22(0x159, 0x0, 0x64)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_235C():
        OP_D1(254, 30000, 80000, 90000, 2000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_235C)
    OP_98(0x0, 0x13)
    OP_98(0x1, 0x7530, 0x7530, 0xFFFFC568)
    OP_98(0x1, 0xFFFFD8F0, 0xC350, 0x9C40)

    def lambda_2396():
        OP_98(0x2, 0xFE, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2396)
    WaitChrThread(0x13, 0x3)

    def lambda_23AB():
        OP_D1(254, -20000, -80000, 80000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_23AB)
    WaitChrThread(0x13, 0x3)

    def lambda_23CA():
        OP_D1(254, -60000, -140000, 60000, 500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_23CA)
    WaitChrThread(0x13, 0x3)
    Fade(250)
    OP_82(0x80, 0x0)
    PlayEffect(0x3, 0x5, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x1)
    OP_44(0xEE, 0x2)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    OP_44(0x13, 0x0)

    def lambda_243E():

        label("loc_243E")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_243E")

    QueueWorkItem2(0x12, 3, lambda_243E)
    OP_6D(92670, 20560, -131770, 0)
    OP_67(0, -77060, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(180000, 0)
    OP_6E(856, 0)
    SetChrPos(0x13, 90890, 70000, -133260, 90)
    OP_D1(19, 90000, 90000, 130000, 0)

    def lambda_24BA():
        OP_D1(254, 90000, 90000, 30000, 1500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_24BA)

    def lambda_24D4():
        OP_8F(0xFE, 0x15F90, 0xFFFDB610, 0xFFFE320C, 0x15F90, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_24D4)

    def lambda_24EF():
        OP_6B(800, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_24EF)
    Sleep(600)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(700)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x5, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEE, 0x1)
    OP_44(0xEE, 0x2)
    OP_44(0xEE, 0x3)
    OP_44(0xEF, 0x1)
    OP_44(0x13, 0x0)
    OP_44(0x12, 0x3)
    OP_6D(-120, 24500, 10100, 0)
    OP_67(0, -1000, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(0, 0)
    OP_6E(360, 0)

    def lambda_259F():
        OP_6D(0, 18000, 8000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_259F)

    def lambda_25B7():
        OP_67(0, 3300, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_25B7)

    def lambda_25CF():
        OP_6B(2900, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_25CF)

    def lambda_25DF():
        OP_6E(380, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_25DF)
    SetChrPos(0x10, 0, 15550, 4000, 180)
    SetChrPos(0x109, 900, 15550, -3420, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264F")
    SetChrPos(0xEF, -550, 15550, -3310, 0)
    SetChrPos(0xF1, -1220, 15550, -5140, 0)
    SetChrPos(0xF0, 1500, 15550, -5350, 0)
    Jump("loc_26D4")

    label("loc_264F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2693")
    SetChrPos(0xF0, -550, 15550, -3310, 0)
    SetChrPos(0xF1, -1220, 15550, -5140, 0)
    SetChrPos(0xEF, 1500, 15550, -5350, 0)
    Jump("loc_26D4")

    label("loc_2693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D4")
    SetChrPos(0xF1, -550, 15550, -3310, 0)
    SetChrPos(0xF0, -1220, 15550, -5140, 0)
    SetChrPos(0xEF, 1500, 15550, -5350, 0)

    label("loc_26D4")

    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 20000, 9090, 180)
    OP_A1(0x12, 0x0)
    OP_72(0x400, 0x0)
    ExitThread()
    OP_6F(0x0, 160)

    def lambda_2707():
        OP_8F(0xFE, 0x0, 0x3CBE, 0x2382, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2707)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x23)
    OP_6F(0x0, 160)
    OP_70(0x0, 0x96)
    WaitChrThread(0x12, 0x0)
    OP_23(0x158)
    OP_22(0xEC, 0x0, 0x64)
    OP_22(0xC8, 0x0, 0x64)

    def lambda_274C():

        label("loc_274C")

        OP_7C(0x0, 0x5DC, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_274C")

    QueueWorkItem2(0x12, 3, lambda_274C)
    PlayEffect(0x1, 0x0, 0x12, 0, -500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_27A1():

        label("loc_27A1")

        OP_7C(0x0, 0x3E8, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_27A1")

    QueueWorkItem2(0x12, 3, lambda_27A1)
    Sleep(300)

    def lambda_27C1():

        label("loc_27C1")

        OP_7C(0x0, 0x1F4, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_27C1")

    QueueWorkItem2(0x12, 3, lambda_27C1)
    Sleep(300)

    def lambda_27E1():

        label("loc_27E1")

        OP_7C(0x0, 0x12C, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_27E1")

    QueueWorkItem2(0x12, 3, lambda_27E1)
    Sleep(300)

    def lambda_2801():

        label("loc_2801")

        OP_7C(0x0, 0x0, 0x3E8, 0x12C)
        OP_48()
        Jump("loc_2801")

    QueueWorkItem2(0x12, 3, lambda_2801)
    OP_44(0x12, 0x3)
    WaitChrThread(0xEE, 0x0)
    OP_82(0x0, 0x2)
    Fade(1000)
    OP_22(0xF3, 0x0, 0x64)
    Play3DEffect(0x0, 0x4, 0x0, "Frame14_Bone__13_", 0x0, 0xF0, 0xFFFFFFBA, 0xB4, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x4, 0x5, 0x0, "Frame79_Bone__78_", 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    Play3DEffect(0x5, 0x6, 0x0, "Frame82_Bone__81_", 0x0, 0x0, 0x0, 0xB4, 0x0, 0x0, 0x258, 0x258, 0x258, 0x0)
    OP_0D()
    OP_43(0x12, 0x0, 0x0, 0x5)
    WaitChrThread(0xEE, 0x0)
    Sleep(1500)

    def lambda_28EC():
        OP_6D(0, 16500, 5660, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_28EC)

    def lambda_2904():
        OP_67(0, 2000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2904)

    def lambda_291C():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_291C)

    def lambda_292C():
        OP_6E(380, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_292C)
    OP_82(0x7, 0x2)
    OP_44(0x10, 0x3)
    Sleep(1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296A")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29D1")

    label("loc_296A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2992")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29D1")

    label("loc_2992")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29BA")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_29D1")

    label("loc_29BA")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_29D1")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29FE")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A65")

    label("loc_29FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A26")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A65")

    label("loc_2A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2A65")

    label("loc_2A4E")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2A65")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A92")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2A92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2AF9")

    label("loc_2AE2")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2AF9")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B26")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B76")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2B8D")

    label("loc_2B76")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2B8D")

    Sleep(1000)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #75
        0x102,
        "#1506F#6P黑色德尔基昂……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        "#1063F#6P哼，这东西也来了！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)

    def lambda_2BFC():
        OP_6E(400, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2BFC)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #77
        0x10,
        "黑骑士",
        (
            "\x07\x05#1591F#5P吾名为『黑骑士』……\x01",
            "驱策漆黑龙机兵的深渊守护者！\x02\x03",

            "基于与『影之王』订立的誓约，\x01",
            "在此作为试炼阻挡你们前进！\x02",
        )
    )

    Jump("loc_2CB3")

    label("loc_2CB3")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #78
        0x10,
        "黑骑士",
        "\x07\x05#1593F#5P#4S来吧——堂堂正正地决一胜负！\x07\x00\x02",
    )

    Jump("loc_2D01")

    label("loc_2D01")

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #79
        0x102,
        "#1506F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        "#1069F#6P求之不得……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xEE, 0x0)
    PlayEffect(0x3, 0x0, 0xFF, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    def lambda_2D9A():
        OP_6D(0, 16600, 5610, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2D9A)

    def lambda_2DB2():
        OP_67(0, 2480, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2DB2)

    def lambda_2DCA():
        OP_6B(1780, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2DCA)

    def lambda_2DDA():
        OP_6E(465, 300)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_2DDA)

    def lambda_2DEA():
        OP_8F(0xFE, 0x212, 0x3CBE, 0x139C, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DEA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E61")

    def lambda_2E13():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E13)

    def lambda_2E2E():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2E2E)

    def lambda_2E49():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2E49)
    Jump("loc_2F22")

    label("loc_2E61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC3")

    def lambda_2E75():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2E75)

    def lambda_2E90():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2E90)

    def lambda_2EAB():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2EAB)
    Jump("loc_2F22")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F22")

    def lambda_2ED7():
        OP_8F(0xFE, 0xFFFFFE98, 0x3CBE, 0x12CA, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2ED7)

    def lambda_2EF2():
        OP_8F(0xFE, 0x41A, 0x3CBE, 0x1072, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2EF2)

    def lambda_2F0D():
        OP_8F(0xFE, 0xFFFFFC54, 0x3CBE, 0xF5A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2F0D)

    label("loc_2F22")

    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AE, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_269 end

    def Function_4_2F44(): pass

    label("Function_4_2F44")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    LoadEffect(0x0, "map\\mp306_00.eff")
    LoadEffect(0x1, "map\\mp285_00.eff")
    LoadEffect(0x2, "map\\mp275_00.eff")
    OP_D2(0x70573, 0x70578, 0x6)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x400, 0x0)
    ExitThread()
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 15550, 0, 180)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x2)
    OP_43(0x10, 0x3, 0x0, 0x6)
    SetChrPos(0x14, 950, 15550, 650, 180)
    SetChrChipByIndex(0x14, 6)
    ClearChrFlags(0x14, 0x80)

    def lambda_3013():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3013)
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 0, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -600, 15550, -10410, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30AE")
    SetChrPos(0xEF, 600, 15550, -10150, 0)
    SetChrPos(0xF0, -1100, 15550, -12150, 0)
    SetChrPos(0xF1, 1200, 15550, -12250, 0)
    Jump("loc_3133")

    label("loc_30AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30F2")
    SetChrPos(0xF0, 600, 15550, -10150, 0)
    SetChrPos(0xEF, -1100, 15550, -12150, 0)
    SetChrPos(0xF1, 1200, 15550, -12250, 0)
    Jump("loc_3133")

    label("loc_30F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3133")
    SetChrPos(0xF1, 600, 15550, -10150, 0)
    SetChrPos(0xEF, -1100, 15550, -12150, 0)
    SetChrPos(0xF0, 1200, 15550, -12250, 0)

    label("loc_3133")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(0, 15550, -160, 0)
    OP_67(0, 4420, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #81
        0x10,
        "黑骑士",
        "\x07\x0C#1605F#5P#40W呵呵……\x07\x00\x02",
    )

    Jump("loc_31DC")

    label("loc_31DC")

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(0, 15550, 340, 0)
    OP_67(0, 4330, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(0, 0)
    OP_6E(400, 0)
    Sleep(500)
    OP_99(0x10, 0x0, 0x5, 0x5DC)
    OP_22(0x12C, 0x0, 0x64)
    OP_0D()
    Sleep(1000)

    def lambda_3243():
        OP_99(0xFE, 0x8, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3243)
    Sleep(400)
    OP_22(0x179, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0x102,
        "#1504F#5P！！！\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    OP_1D(0x72)

    def lambda_33A3():
        OP_6D(0, 15550, 1340, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_33A3)

    def lambda_33BB():
        OP_67(0, 3900, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_33BB)

    def lambda_33D3():
        OP_6B(1950, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_33D3)

    def lambda_33E3():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_33E3)

    def lambda_33F3():
        OP_6E(400, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_33F3)
    Sleep(1000)
    OP_99(0x10, 0x18, 0x1E, 0x5DC)
    OP_99(0x10, 0x1E, 0x21, 0x5DC)
    WaitChrThread(0xEE, 0x0)

    NpcTalk(    #83
        0x10,
        "黑骑士",
        (
            "\x07\x0C#1596F#5P#40W干得漂亮……\x01",
            "终于让我现出真面目了吗。\x07\x00\x02",
        )
    )

    Jump("loc_346B")

    label("loc_346B")

    CloseMessageWindow()

    ChrTalk(    #84
        0x109,
        "#1840F#5P……果然………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        "#1501F#5P…………莱维……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-330, 15550, -2570, 0)
    OP_67(0, 3600, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(315000, 0)
    OP_6E(490, 0)
    SetChrPos(0x10, 620, 15550, 0, 180)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 40)
    SetChrPos(0x109, 340, 15550, -6310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3573")
    SetChrPos(0xEF, 960, 15550, -5310, 0)
    SetChrPos(0xF0, 2090, 15550, -6550, 0)
    SetChrPos(0xF1, 1310, 15550, -7380, 0)
    Jump("loc_35F8")

    label("loc_3573")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B7")
    SetChrPos(0xF0, 960, 15550, -5310, 0)
    SetChrPos(0xEF, 2090, 15550, -6550, 0)
    SetChrPos(0xF1, 1310, 15550, -7380, 0)
    Jump("loc_35F8")

    label("loc_35B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F8")
    SetChrPos(0xF1, 960, 15550, -5310, 0)
    SetChrPos(0xEF, 2090, 15550, -6550, 0)
    SetChrPos(0xF0, 1310, 15550, -7380, 0)

    label("loc_35F8")


    def lambda_35FE():
        OP_6D(-900, 15550, -250, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_35FE)

    def lambda_3616():
        OP_67(0, 4000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_3616)

    def lambda_362E():
        OP_6B(1900, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_362E)

    def lambda_363E():
        OP_6E(520, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_363E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3674")

    def lambda_365C():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_365C)
    Jump("loc_36C9")

    label("loc_3674")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A0")

    def lambda_3688():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3688)
    Jump("loc_36C9")

    label("loc_36A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C9")

    def lambda_36B4():
        OP_8F(0xFE, 0x26C, 0x3CBE, 0xFFFFF4A2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_36B4)

    label("loc_36C9")

    Sleep(200)

    def lambda_36D4():
        OP_8F(0xFE, 0xFFFFFF38, 0x3CBE, 0xFFFFF0BA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_36D4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_373A")
    Sleep(300)

    def lambda_3702():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_3702)
    Sleep(100)

    def lambda_3722():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3722)
    Jump("loc_37D9")

    label("loc_373A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378B")
    Sleep(300)

    def lambda_3753():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3753)
    Sleep(100)

    def lambda_3773():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_3773)
    Jump("loc_37D9")

    label("loc_378B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D9")
    Sleep(300)

    def lambda_37A4():
        OP_8F(0xFE, 0x71C, 0x3CBE, 0xFFFFEE62, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_37A4)
    Sleep(100)

    def lambda_37C4():
        OP_8F(0xFE, 0x37A, 0x3CBE, 0xFFFFEB6A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_37C4)

    label("loc_37D9")

    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x3)
    Sleep(500)

    ChrTalk(    #86
        0x10,
        (
            "\x07\x0C#1599F#11P#40W……没想到会\x01",
            "以这样的形式重逢。\x02\x03",

            "#1596F呵呵，虽然\x01",
            "对你来说或许已是多余的再会……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1513F#6P哈哈……\x01",
            "这种事……怎么可能呢。\x02\x03",

            "#1503F…………………………………\x02\x03",

            "我……\x01",
            "其实很害怕。\x02\x03",

            "#1505F就算再次见到莱维，\x01",
            "也很快就会分别……\x02\x03",

            "我不想再体味这种痛苦，\x01",
            "所以装作没有发觉……\x02\x03",

            "正因为我这么软弱，\x01",
            "才让莱维戴上了面具。\x02\x03",

            "#1514F……这就是真相吧？\x02",
        )
    )

    Jump("loc_39A9")

    label("loc_39A9")

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "\x07\x0C#1597F#11P#40W嗯……说得没错。\x02\x03",

            "#1594F『影之王』使我这个概念\x01",
            "重生于这个世界。\x02\x03",

            "作为你们面前的敌人，\x01",
            "最强且最重要的守护者……\x02\x03",

            "#1597F然而，\x01",
            "让我戴上面具的的确是你们的意念。\x02\x03",

            "因为这个『影之国』……\x01",
            "会因为思绪而产生变化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x102,
        "#1503F#6P果然是这样吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "\x07\x0C#1599F#11P#40W然而这任务，\x01",
            "也因你们而终结了。\x02\x03",

            "#1596F呵呵，说实话，\x01",
            "连德尔基昂都出马了，\x01",
            "还真没想到会被打败啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1513F#6P哈哈……\x01",
            "真的是很危险呢。\x02\x03",

            "#1501F不过……\x01",
            "这是大家齐心协力的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x10,
        (
            "\x07\x0C#1599F#11P#40W呼……\x01",
            "这也是一种力量吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EED")
    Sleep(500)

    ChrTalk(    #93
        0x10,
        (
            "\x07\x0C#1596F#11P#40W艾丝蒂尔·布莱特……\x01",
            "看来你有了很大的长进啊。\x02\x03",

            "不过，\x01",
            "要达到你父亲的境界还有很长的路要走。\x07\x00\x02",
        )
    )

    Jump("loc_3C92")

    label("loc_3C92")

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "我也不认为会有那么简单呢。\x02\x03",

            "#1017F即使如此，\x01",
            "我还是在一步一步踏实地前进着。\x02\x03",

            "和约修亚——\x01",
            "你的弟弟一起哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        "#1501F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D90")

    ChrTalk(    #96
        0x10,
        "\x07\x0C#1599F#11P#40W呵呵……那样就好。\x07\x00\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EED")

    label("loc_3D90")


    ChrTalk(    #97
        0x10,
        (
            "\x07\x0C#1599F#11P#40W呵呵……那样就好。\x02\x03",

            "#1594F还有……\x01",
            "玲的事情要谢谢你们。\x02\x03",

            "这孩子，\x01",
            "可是特别令我担心呢。\x07\x00\x02",
        )
    )

    Jump("loc_3E1E")

    label("loc_3E1E")

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1025F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        (
            "\x07\x0C#1597F#11P#40W嗯，\x01",
            "虽然这也是不易处理的难题……\x02\x03",

            "#1596F不过，\x01",
            "你们一定能找到正确的道路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        "#1514F#6P莱维……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#1017F#6P嗯……放心吧！\x02",
    )

    CloseMessageWindow()

    label("loc_3EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4161")
    Sleep(500)

    ChrTalk(    #102
        0x10,
        (
            "\x07\x0C#1596F#11P#40W阿加特·科洛斯纳……\x01",
            "你可真是个棘手的家伙。\x02\x03",

            "那把重剑，\x01",
            "看来也使得更加像样了嘛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x106,
        (
            "#051F#6P哈哈……\x01",
            "你会夸奖别人，\x01",
            "真是太阳从西边出来了。\x02\x03",

            "#053F不过，连同这把重剑，\x01",
            "我还会继续成长的。\x02\x03",

            "#556F我一定会\x01",
            "踏踏实实的磨练自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "\x07\x0C#1598F#11P#40W……没想到\x01",
            "你竟会说出这种话来……\x02\x03",

            "#1596F呼……就像是成家之人\x01",
            "才会表现出的镇定一样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        "#055F#6P什、什么话……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4161")

    ChrTalk(    #106
        0x107,
        "#064F#6P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        "\x07\x0C#1599F#11P#40W……呵呵，原来如此啊。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #108
        0x106,
        (
            "#055F#6P喂！？\x01",
            "你刚才绝对误会了什么吧！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4161")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4315")
    Sleep(500)

    ChrTalk(    #109
        0x10,
        (
            "\x07\x0C#1596F#11P#40W提妲·拉赛尔……\x01",
            "你似乎已经找到了自己的道路，真是太好了。\x02\x03",

            "『导力装甲』……\x01",
            "到底会对『十三工房』造成多大的威胁，\x01",
            "我个人倒是相当期待哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        (
            "#067F#6P哇哇……\x01",
            "我、我会努力的！\x02\x03",

            "#066F虽、虽然动机\x01",
            "可能稍微有点不纯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        (
            "\x07\x0C#1599F#11P#40W呼……\x01",
            "说到底没有什么动机是完全单纯的。\x02\x03",

            "#1596F一边迷惑和烦恼，\x01",
            "一边走自己的路便是。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        "#560F#6P……是。\x02",
    )

    CloseMessageWindow()

    label("loc_4315")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44B3")
    Sleep(500)

    ChrTalk(    #113
        0x10,
        (
            "\x07\x0C#1596F#11P#40W理查德上校……\x01",
            "政变事件之后好久不见了呢。\x02\x03",

            "没想到，\x01",
            "能以这种方式与你再会。\x02",
        )
    )

    Jump("loc_43A1")

    label("loc_43A1")

    CloseMessageWindow()

    ChrTalk(    #114
        0x10C,
        (
            "#119F#6P洛伦斯少尉……\x01",
            "这是我的台词才对啊。\x02\x03",

            "#111F不过，\x01",
            "能与你在此交手，\x01",
            "我感到十分荣幸。\x02\x03",

            "因为终于能够\x01",
            "确定你的实力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "\x07\x0C#1599F#11P#40W呵呵……\x01",
            "希望没有\x01",
            "让你太过失望。\x02\x03",

            "#1596F倒是你，\x01",
            "让我见识了剑圣亲授的剑术。\x07\x00\x02",
        )
    )

    Jump("loc_44B2")

    label("loc_44B2")

    CloseMessageWindow()

    label("loc_44B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46FA")
    Sleep(500)

    ChrTalk(    #116
        0x110,
        "#1300F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        (
            "\x07\x0C#1597F#11P#40W说起来……\x01",
            "还没和你\x01",
            "道别呢。\x02\x03",

            "#1594F抱歉啊，玲。\x01",
            "我就这么半途而废的消失了。\x07\x00\x02",
        )
    )

    Jump("loc_457C")

    label("loc_457C")

    CloseMessageWindow()

    ChrTalk(    #118
        0x110,
        (
            "#268F#6P不……\x01",
            "莱维不用道歉啊。\x02\x03",

            "#265F那时候，如果不是你和约修亚一起\x01",
            "将我带出『馆』外，\x01",
            "玲到现在都只能是独自一人。\x02\x03",

            "#261F所以……真是谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "\x07\x0C#1596F#11P#40W……是吗………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x110,
        (
            "#260F#6P嘻嘻，\x01",
            "本来希望最后你能再摸摸我的头……\x02\x03",

            "#263F不过被你那爪子碰到好像会很痛的样子，\x01",
            "还是算了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        "\x07\x0C#1599F#11P#40W呵呵，抱歉啊。\x07\x00\x02",
    )

    CloseMessageWindow()

    label("loc_46FA")

    Sleep(500)

    ChrTalk(    #122
        0x10,
        (
            "\x07\x0C#1595F#11P#40W……接下来。\x01",
            "凯文·格拉汉姆……\x02\x03",

            "你终于得到确信了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x109,
        (
            "#1065F#6P啊……\x01",
            "已经再清楚不过了。\x02\x03",

            "#1840F以后……\x01",
            "就请交给我吧。\x02\x03",

            "你所珍重的人们……\x01",
            "我一定会平安地把他们带回原来的世界。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10,
        (
            "\x07\x0C#1597F#11P#40W……是吗。\x01",
            "那么，我就放心地交给你吧。\x02\x03",

            "#1594F我想你应该知道，\x01",
            "『王』绝非等闲之辈。\x02\x03",

            "需怎样面对……\x01",
            "希望你处处谨慎小心。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x109,
        "#1075F#6P嗯……感谢你的忠告。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F1")

    ChrTalk(    #126
        0x10F,
        (
            "#1802F#6P等、等一下……\x01",
            "你在说什么？\x02\x03",

            "而且……\x01",
            "你之前对我……\x02",
        )
    )

    Jump("loc_4927")

    label("loc_4927")

    CloseMessageWindow()

    ChrTalk(    #127
        0x10,
        (
            "\x07\x0C#1597F#11P#40W抱歉，\x01",
            "莉丝·亚尔珍特。\x02\x03",

            "关于这件事，\x01",
            "由于现在我依然被『规则』束缚，\x01",
            "所以无法回答。\x02\x03",

            "#1596F只是……你的疑问，\x01",
            "很快就将得到解答。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x10F,
        "#1444F#6P咦……\x02",
    )

    CloseMessageWindow()

    label("loc_49F1")

    Sleep(300)
    Fade(500)

    def lambda_4A01():
        OP_6B(1850, 500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4A01)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 0, 0, 100, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0xEE, 0x2)

    def lambda_4A55():
        OP_6B(1700, 20000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4A55)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8C")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4AF3")

    label("loc_4A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AB4")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4AF3")

    label("loc_4AB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ADC")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4AF3")

    label("loc_4ADC")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4AF3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B20")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4B87")

    label("loc_4B20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B48")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4B87")

    label("loc_4B48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B70")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4B87")

    label("loc_4B70")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4B87")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BB4")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4C1B")

    label("loc_4BB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BDC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4C1B")

    label("loc_4BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C04")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4C1B")

    label("loc_4C04")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4C1B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C48")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CAF")

    label("loc_4C48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C70")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CAF")

    label("loc_4C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C98")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4CAF")

    label("loc_4C98")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4CAF")

    Sleep(1500)

    ChrTalk(    #129
        0x102,
        "#1503F#6P……莱维…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "\x07\x0C#1599F#11P#40W呵呵……\x01",
            "看来时间到了。\x02\x03",

            "#1596F我终于……\x01",
            "能够回到应得之所了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        (
            "#1513F#6P#40W嗯……辛苦你了。\x02\x03",

            "#1514F折断的那把剑……\x01",
            "我已经带到姐姐那里了……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)

    ChrTalk(    #132
        0x10,
        (
            "\x07\x0C#1599F#11P#40W啊啊……抱歉了。\x02\x03",

            "让我和她……\x01",
            "一起好好休息吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Sleep(300)

    ChrTalk(    #133
        0x10,
        (
            "\x07\x0C#1604F#11P#60W那么再见了……\x01",
            "………约修亚……………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        "#1516F#6P#40W………嗯…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #135
        0x102,
        "#1501F#6P#40W永别了……莱维………\x02",
    )

    CloseMessageWindow()

    def lambda_4F01():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F01)
    Sleep(1000)
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Fade(500)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x2, 0x2, 0x10, 0, 500, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x3C)
    OP_22(0x1B0, 0x0, 0x64)

    def lambda_4F86():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4F86)
    Sleep(500)

    def lambda_4F9D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F9D)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x2)

    def lambda_4FB5():
        OP_6B(3000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4FB5)
    OP_0D()
    OP_44(0x10, 0x3)
    Sleep(1000)
    Sleep(3000)
    SetChrFlags(0x10, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2F44 end

    def Function_5_4FF0(): pass

    label("Function_5_4FF0")

    OP_73(0x0)
    Sleep(1500)
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 150)
    OP_70(0x0, 0x8C)
    OP_D8(0x0, 0x5DC)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0xF)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x14)
    Return()

    # Function_5_4FF0 end

    def Function_6_5027(): pass

    label("Function_6_5027")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5049")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("Function_6_5027")

    label("loc_5049")

    Return()

    # Function_6_5027 end

    def Function_7_504A(): pass

    label("Function_7_504A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -200, 15550, -3910, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51B4")
    SetChrPos(0xEF, 810, 15550, -1890, 0)
    SetChrPos(0xF0, 1820, 15550, -4510, 0)
    SetChrPos(0xF1, 890, 15550, -5270, 0)
    Jump("loc_5239")

    label("loc_51B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51F8")
    SetChrPos(0xF0, 810, 15550, -1890, 0)
    SetChrPos(0xEF, 1820, 15550, -4510, 0)
    SetChrPos(0xF1, 890, 15550, -5270, 0)
    Jump("loc_5239")

    label("loc_51F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5239")
    SetChrPos(0xF1, 810, 15550, -1890, 0)
    SetChrPos(0xEF, 1820, 15550, -4510, 0)
    SetChrPos(0xF0, 890, 15550, -5270, 0)

    label("loc_5239")

    OP_6D(-70, 15550, 2000, 0)
    OP_67(0, 5180, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(315000, 0)
    OP_6E(520, 0)
    Sleep(2000)

    def lambda_5281():
        OP_6D(-70, 15550, -1200, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5281)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(150)

    ChrTalk(    #136
        0x102,
        "#1516F#5P………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_530D")

    ChrTalk(    #137
        0x110,
        "#1309F#6P………莱维……………\x02",
    )

    CloseMessageWindow()

    label("loc_530D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5349")

    ChrTalk(    #138
        0x10F,
        "#1445F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_5349")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5384")

    ChrTalk(    #139
        0x106,
        "#552F#6P………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_5384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53BD")

    ChrTalk(    #140
        0x101,
        "#1027F#6P约修亚……那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_53BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53F7")

    ChrTalk(    #141
        0x10B,
        "#212F#6P约修亚……不要紧吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_53F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5434")

    ChrTalk(    #142
        0x107,
        (
            "#562F#6P那个……\x01",
            "约修亚哥哥……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_5434")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_546D")

    ChrTalk(    #143
        0x105,
        "#1169F#6P约修亚……那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_546D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54A6")

    ChrTalk(    #144
        0x103,
        "#1532F#6P约修亚……那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_54A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54E1")

    ChrTalk(    #145
        0x104,
        "#1542F#6P约修亚君……还好吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_54E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5519")

    ChrTalk(    #146
        0x10A,
        "#813F#6P约修亚……那个……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_5519")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5553")

    ChrTalk(    #147
        0x108,
        "#072F#6P约修亚……不要紧吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_5553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_558D")

    ChrTalk(    #148
        0x10E,
        "#178F#6P约修亚……不要紧吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_558D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55C5")

    ChrTalk(    #149
        0x10D,
        "#270F#6P……不要紧吧……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_55C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55FF")

    ChrTalk(    #150
        0x10C,
        "#112F#6P约修亚……不要紧吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5629")

    label("loc_55FF")


    ChrTalk(    #151
        0x109,
        "#1063F#6P约修亚……你还好吧？\x02",
    )

    CloseMessageWindow()

    label("loc_5629")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_570F")

    ChrTalk(    #152
        0x102,
        (
            "#1501F#5P不要紧……\x01",
            "况且我已经预料到了。\x02\x03",

            "#1513F那个时候……\x01",
            "总是让莱维担心我的事情，\x01",
            "所以也不知道跟他说什么好……\x02\x03",

            "这次总算可以……\x01",
            "和他说句道别的话了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57C1")

    label("loc_570F")


    ChrTalk(    #153
        0x102,
        (
            "#1501F#5P不要紧……\x01",
            "我早已有所觉悟了。\x02\x03",

            "#1513F那个时候……\x01",
            "总是让莱维担心我的事情，\x01",
            "所以也不知道跟他说什么好……\x02\x03",

            "这次总算可以……\x01",
            "和他说句道别的话了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57F4")

    ChrTalk(    #154
        0x110,
        "#260F#6P……约修亚………\x02",
    )

    CloseMessageWindow()

    label("loc_57F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5822")

    ChrTalk(    #155
        0x105,
        "#1382F#6P约修亚……\x02",
    )

    CloseMessageWindow()

    label("loc_5822")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_584D")

    ChrTalk(    #156
        0x107,
        "#066F#6P哥哥……\x02",
    )

    CloseMessageWindow()

    label("loc_584D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5882")

    ChrTalk(    #157
        0x101,
        "#1017F#6P……是啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_5940")

    label("loc_5882")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58B4")

    ChrTalk(    #158
        0x106,
        "#556F#6P……唔………\x02",
    )

    CloseMessageWindow()
    Jump("loc_5940")

    label("loc_58B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E9")

    ChrTalk(    #159
        0x103,
        "#1534F#6P……是吗………\x02",
    )

    CloseMessageWindow()
    Jump("loc_5940")

    label("loc_58E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5917")

    ChrTalk(    #160
        0x10C,
        "#111F#6P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5940")

    label("loc_5917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5940")

    ChrTalk(    #161
        0x10D,
        "#275F#6P嗯……\x02",
    )

    CloseMessageWindow()

    label("loc_5940")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5972")

    ChrTalk(    #162
        0x10B,
        "#415F#6P……太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A81")

    label("loc_5972")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59A5")

    ChrTalk(    #163
        0x10F,
        "#1447F#6P……太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A81")

    label("loc_59A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_59E3")

    ChrTalk(    #164
        0x104,
        (
            "#1545F#6P啊啊……\x01",
            "这比什么都好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A81")

    label("loc_59E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A19")

    ChrTalk(    #165
        0x108,
        "#573F#6P……真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A81")

    label("loc_5A19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A51")

    ChrTalk(    #166
        0x10E,
        "#179F#6P……这比什么都好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A81")

    label("loc_5A51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A81")

    ChrTalk(    #167
        0x10A,
        "#1314F#6P……太好了。\x02",
    )

    CloseMessageWindow()

    label("loc_5A81")


    def lambda_5A87():
        OP_6D(-70, 15550, -2440, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5A87)
    OP_8C(0x102, 180, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #168
        0x102,
        (
            "#1505F#11P……至此，\x01",
            "我的任务也算是完成了。\x02\x03",

            "#1502F凯文先生。\x01",
            "之后的事情就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x109,
        (
            "#1065F#6P啊啊……交给我吧。\x02\x03",

            "#1060F把最后的『守护者』打倒之后，\x01",
            "就应该可以解除周游道的结界了。\x02\x03",

            "我们先去那里看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x102,
        (
            "#1500F#11P明白了。\x01",
            "是通往离宫的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-340, 15550, -480, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)
    SetChrPos(0x0, -340, 15550, -480, 180)
    SetChrPos(0x1, -340, 15550, -480, 180)
    SetChrPos(0x2, -340, 15550, -480, 180)
    SetChrPos(0x3, -340, 15550, -480, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C9F")
    OP_A2(0x2644)

    label("loc_5C9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CB0")
    OP_A2(0x2645)

    label("loc_5CB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CC1")
    OP_A2(0x2646)

    label("loc_5CC1")

    OP_28(0x3B, 0x1, 0x2)
    OP_28(0x3B, 0x1, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_504A end

    def Function_8_5CDE(): pass

    label("Function_8_5CDE")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    OP_20(0x0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Sleep(1000)
    OP_AE(0x5DC)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 350, 15550, 2800, 180)
    OP_9F(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x109, -30, 15550, -4600, 0)
    SetChrPos(0x10F, -1350, 15550, -4550, 0)
    OP_51(0x10F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3CA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3B6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFC, 0x80)
    SetChrFlags(0xFD, 0x80)
    OP_6D(-5140, 35650, -5290, 0)
    OP_67(0, 0, -10000, 0)
    OP_6B(4760, 0)
    OP_6C(45000, 0)
    OP_6E(443, 0)

    def lambda_5ED5():
        OP_6D(-5140, 19250, -5290, 7000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5ED5)

    def lambda_5EED():
        OP_67(0, 5850, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EED)

    def lambda_5F05():
        OP_6B(4760, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5F05)

    def lambda_5F15():
        OP_6E(443, 7000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5F15)
    LoadEffect(0x1, "map\\mp121_00.eff")
    LoadEffect(0x2, "battle\\btgun10.eff")
    LoadEffect(0x3, "map\\mp274_00.eff")
    LoadEffect(0x4, "map\\mp275_00.eff")
    LoadEffect(0x5, "map\\mp275_01.eff")
    LoadEffect(0x6, "map\\mp306_00.eff")
    LoadEffect(0x7, "map\\mp285_00.eff")
    FadeToBright(4000, 16777215)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(600, 15550, -3200, 0)
    OP_67(0, 4850, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(45000, 0)
    OP_6E(360, 0)
    OP_82(0x86, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x8A, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #171
        0x10F,
        "#1934F#6P这、这里是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x109,
        "#1063F#12P和『黑骑士』战斗的……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #173
        (
            "\x07\x0C#40W……这是我和他商量之后，\x01",
            "特意建造的离别场所。\x02\x03",

            "呵呵……\x01",
            "果然，还是很有用呢。\x07\x00\x02",
        )
    )

    Jump("loc_60F1")

    label("loc_60F1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xD3)
    Sleep(500)

    def lambda_6151():
        OP_6D(1300, 15550, 600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6151)

    def lambda_6169():
        OP_67(0, 4500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6169)

    def lambda_6181():
        OP_6B(2820, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6181)

    def lambda_6191():
        OP_6E(326, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6191)
    Sleep(2000)
    Fade(500)
    OP_22(0x99, 0x0, 0x50)
    PlayEffect(0x6, 0x0, 0x14, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x1, 0x14, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_621A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_621A)
    OP_22(0x146, 0x1, 0x3C)
    WaitChrThread(0x14, 0x1)
    Sleep(800)
    OP_82(0x1, 0x2)

    ChrTalk(    #174
        0x109,
        "#1079F#4P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10F,
        "#1932F#6P姐、姐姐……\x02",
    )

    CloseMessageWindow()

    def lambda_627C():
        OP_6D(1200, 15550, 1800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_627C)

    def lambda_6294():
        OP_8E(0xFE, 0x0, 0x3CBE, 0xFFFFF8D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6294)
    Sleep(400)

    def lambda_62B4():
        OP_8E(0xFE, 0xFFFFFA56, 0x3CBE, 0xFFFFF7CC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_62B4)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #176
        0x109,
        (
            "#1840F#12P骑士的制服……\x02\x03",

            "……果然……\x01",
            "从『圣痕』之中解放出来了对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x14,
        (
            "\x07\x0C#1475F#5P#30W呵呵，托你们的福。\x02\x03",

            "#1471F你们俩……\x01",
            "一直以来都非常努力啊。\x02\x03",

            "在那种困难情况下，\x01",
            "还能锲而不舍地坚持到最后……\x02\x03",

            "#1479F嗯嗯。\x01",
            "真不愧是我最引以为豪的弟弟和妹妹。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10F,
        "#1952F#6P……姐姐…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x109,
        (
            "#1846F#12P……哈哈………\x01",
            "真是的，看来你一点都没变啊。\x02\x03",

            "#1840F话说回来……\x01",
            "『圣痕』真的已经消失了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x14,
        (
            "\x07\x0C#1474F#5P#30W不……\x01",
            "那东西还残留在我身体里面。\x02\x03",

            "#1477F因为刚才被你们打败，\x01",
            "所以暂时得到了压制……\x02\x03",

            "#1472F不过，如果放着不管的话，\x01",
            "很快就会恢复原来的样子。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x109,
        "#1067F#12P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x10F,
        "#1942F#6P那、那要怎么办才……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x14,
        (
            "\x07\x0C#1475F#5P#30W……所以呢，凯文。\x02\x03",

            "#1476F希望你亲手\x01",
            "给予我最后的一击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x109,
        "#1079F#12P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x10F,
        "#1934F#6P姐、姐姐……难道你想……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x14,
        (
            "\x07\x0C#1476F#5P#30W没错，就是杀了现在的我。\x02\x03",

            "#1475F只有这样做，\x01",
            "被这个世界复制的『圣痕』\x01",
            "才能完完全全地消失。\x02\x03",

            "#1471F那个人叫做赛雷斯托……是吧？\x02\x03",

            "她的力量也应该恢复了，\x01",
            "只要她在，\x01",
            "一定可以将你们带回到原来的世界。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x10F,
        "#1935F#6P但、但是……这样的话……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)

    ChrTalk(    #188
        0x109,
        (
            "#1075F#12P姐姐……\x02\x03",

            "#1840F……一定要这么做吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x14,
        (
            "\x07\x0C#1475F#5P#30W嗯……\x01",
            "除此之外，没有其它的路可走。\x02\x03",

            "#1476F五年前，你失去理智的时候，\x01",
            "几乎丧失了所有的意识。\x02\x03",

            "可是这次，\x01",
            "你一定要靠自己的意志去完成才行。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x109,
        "#1067F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x10F,
        (
            "#1950F#6P姐姐……这太残忍了……！\x02\x03",

            "这…对凯文来说……\x01",
            "根本就是不可能的事……！\x02\x03",

            "#1953F而且……而且……\x01",
            "这样做的话，姐姐一定会……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x14,
        (
            "\x07\x0C#1477F#5P#30W抱歉，莉丝……\x02\x03",

            "#1475F可是，我别无选择，\x01",
            "我一定要这么说才行。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #193
        0x14,
        (
            "\x07\x0C#1472F#5P#30W——凯文·格拉汉姆。\x01",
            "我最后再说一遍。\x02\x03",

            "将我消灭，\x01",
            "然后和大家一起回到原来的世界。\x02\x03",

            "#1474F作为姐姐，作为骑士前辈，\x01",
            "作为代替你母亲的人……\x02\x03",

            "#1471F这是我唯一的，也是最后的请求。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x10F,
        "#1950F#6P#40W……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x109,
        (
            "#1845F#12P#40W………哈哈…………\x02\x03",

            "#1846F你确实……很体贴，\x01",
            "同时，也是一位比谁都更严格的姐姐。\x02\x03",

            "#1844F但是……\x01",
            "这才是我们的露菲娜姐姐。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 8)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_6BC4():
        OP_6D(1100, 15550, 1900, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6BC4)

    def lambda_6BDC():
        OP_67(0, 4490, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6BDC)

    def lambda_6BF4():
        OP_6C(38000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6BF4)
    OP_99(0x109, 0x0, 0x7, 0x9C4)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x10F, 90, 600)
    Sleep(200)

    ChrTalk(    #196
        0x10F,
        "#1955F#6P凯文……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x109,
        (
            "#1076F#11P#40W抱歉，莉丝……\x02\x03",

            "#1844F……我不得不……\x01",
            "再次亲手将你姐姐给……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x10F,
        "#1950F#6P#40W那、那就……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #199
        0x10F,
        "#1951F#6P#3S那就让我也一起…！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #200
        0x109,
        "#1847F#11P什……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x14,
        "\x07\x0C#1473F#5P#30W………哎……………\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x10F,
        (
            "#1950F#6P#40W我、我不想……\x01",
            "再被你们两个置之不理……！\x02\x03",

            "我讨厌只当个旁观者……！\x01",
            "也讨厌只是单纯地等待！\x02\x03",

            "#1953F要是非要那样做的话……\x02\x03",

            "这次……\x01",
            "我愿意和凯文一起背负罪名！\x02",
        )
    )

    Jump("loc_6E63")

    label("loc_6E63")

    CloseMessageWindow()

    ChrTalk(    #203
        0x109,
        "#1067F#11P莉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x14,
        (
            "\x07\x0C#1476F#5P#30W呵呵……原来如此。\x02\x03",

            "#1475F五年了……\x01",
            "你真的成长了许多。\x02\x03",

            "#1471F我记得，你和凯文一样，\x01",
            "都是爱因门下的学生吧。\x02\x03",

            "呵呵……\x01",
            "看来，我真的要感激她才行啊。\x07\x00\x02",
        )
    )

    Jump("loc_6F54")

    label("loc_6F54")

    CloseMessageWindow()
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #205
        0x10F,
        "#1955F#6P姐、姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x14,
        (
            "\x07\x0C#1475F#5P#30W……我没有任何异议。\x02\x03",

            "#1470F凯文，一切由你来决断。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #207
        0x109,
        (
            "#1847F#12P等、等一下！\x02\x03",

            "#1069F这、这不应该是……\x01",
            "我一个人背负的责任才对吗！？\x02\x03",

            "为什么非要牵连莉丝进来……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #208
        0x14,
        (
            "\x07\x0C#1478F#3S#5P——你是个男人对吧！\x01",
            "别说这么没气量的话！\x07\x00\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0x14,
        (
            "\x07\x0C#1475F#5P#30W要是爱因本人在场的话，\x01",
            "一定会对你这样当头痛斥。\x02\x03",

            "#1471F也罢，接下来该如何做，\x01",
            "还是由你来决定好了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #210
        0x10F,
        "#1952F#6P#40W姐、姐姐你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x109,
        (
            "#1844F#12P#40W哈哈……好了……\x01",
            "……真的说不过你……\x02\x03",

            "#1843F………………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_99(0x109, 0x7, 0x0, 0x7D0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    OP_8C(0x109, 270, 400)
    Sleep(150)
    OP_8C(0x10F, 90, 400)
    Fade(500)
    OP_6D(640, 15550, -1090, 0)
    OP_67(0, 4450, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(130000, 0)
    OP_6E(386, 0)
    SetChrPos(0x14, -650, 15550, 3840, 180)
    SetChrPos(0x109, -400, 15550, -1400, 270)
    SetChrPos(0x10F, -1650, 15550, -1520, 90)
    OP_51(0x10F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x10F, 0x8)
    OP_0D()
    Sleep(300)
    OP_99(0x109, 0x0, 0x4, 0x4B0)
    Sleep(500)

    ChrTalk(    #212
        0x109,
        (
            "#1840F#5P#40W莉丝……过来这里。\x02\x03",

            "我们两人……\x01",
            "一起拿起弩枪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x10F,
        "#1946F#12P#40W……嗯………！\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x4, 0x0, 0x5DC)
    Sleep(300)

    def lambda_73EE():
        OP_6D(1300, 15550, -300, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73EE)
    OP_99(0x109, 0x10, 0x1C, 0x5DC)
    OP_22(0xD5, 0x0, 0x64)
    SetChrPos(0x10F, -1060, 15550, -1380, 90)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #214
        0x14,
        (
            "\x07\x0C#1475F#6P#30W呵呵……\x01",
            "看来，我还是差得远呢。\x02\x03",

            "这种选择……\x01",
            "我根本就没有想到。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x109,
        "#1079F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x10F,
        "#1942F#11P姐姐……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x14,
        (
            "\x07\x0C#1477F#6P#30W对了，凯文……\x02\x03",

            "刚才，你不是说要\x01",
            "前往我到达的境地吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x109,
        (
            "#1840F#5P啊，是啊……\x02\x03",

            "虽然前路好像还很漫长……\x01",
            "不过我有这个打算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x14,
        (
            "\x07\x0C#1475F#6P#30W虽说这是你的自由……\x01",
            "不过可以的话，我希望你能重新考虑一下。\x02\x03",

            "#1477F一直以来……\x01",
            "我都是在迷惘、苦恼中走过来的。\x02\x03",

            "……一个所有人都很幸福的世界。\x02\x03",

            "#1476F虽然我明知那是不可能的，\x01",
            "但每天仍然拼命做着\x01",
            "至少能够接近一点的努力。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x109,
        "#1075F#5P#40W……没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x10F,
        (
            "#1937F#11P#40W我也……\x02\x03",

            "#1946F要是可以的话，\x01",
            "我也想走和姐姐一样的路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x14,
        (
            "\x07\x0C#1475F#6P#30W呵呵……真拿你们没办法。\x02\x03",

            "#1477F……那么……\x02\x03",

            "#1476F那么，不要把目标\x01",
            "仅放在我曾待过的那片天地。\x02\x03",

            "我，希望你们能够达到\x01",
            "我梦寐以求却又未能到达的境界。\x02\x03",

            "#1475F我觉得……\x01",
            "你们两个一定能做到。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x10F,
        "#1952F#11P#40W姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x109,
        (
            "#1068F#5P#40W哈哈……\x01",
            "一下子就对我们\x01",
            "提出如此高的要求……\x02\x03",

            "#1840F不过……我们明白了。\x02\x03",

            "你既然这么说了，\x01",
            "我们无论如何也要以此为目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x10F,
        "#1937F#11P#40W……嗯，我们约定。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x14,
        (
            "\x07\x0C#1471F#6P#30W呵呵……不过说到底，\x01",
            "你们还是要保持属于自己的步伐。\x02\x03",

            "#1475F——好了。\x01",
            "让其他人等得太久了，\x01",
            "我会过意不去的。\x02\x03",

            "#1470F凯文、莉丝。\x01",
            "……接下来拜托你们了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x109,
        "#1844F#5P#40W……嗯嗯…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x10F,
        "#1935F#11P#40W……………嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(900, 15550, 1300, 0)
    OP_67(0, 3950, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(43000, 0)
    OP_6E(347, 0)
    SetChrPos(0x14, 200, 15550, 2800, 180)
    SetChrPos(0x109, -510, 15550, -2340, 0)
    SetChrPos(0x10F, -1040, 15550, -2240, 0)
    SetChrSubChip(0x109, 40)
    OP_0D()
    Sleep(300)
    OP_99(0x109, 0x28, 0x2C, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0x14, 0x2)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)
    OP_99(0x14, 0x0, 0x4, 0x5DC)

    def lambda_7AB4():
        OP_6B(2500, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7AB4)
    Sleep(500)

    ChrTalk(    #229
        0x10F,
        "#1950F#6P#40W………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x109,
        (
            "#1067F#11P#40W不要紧……\x01",
            "有我在……\x02\x03",

            "#1840F慢慢地……\x01",
            "嗯……这样慢慢来就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #231
        0x14,
        (
            "\x07\x0C#1475F#5P#40W呵呵……\x02\x03",

            "愿你们两个\x01",
            "能够得到女神的祝福……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #232
        0x14,
        (
            "\x07\x0C#1471F#5P#40W凯文……\x01",
            "莉丝就拜托你照顾了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x109,
        (
            "#1840F#12P#40W……嗯，你放心吧。\x02\x03",

            "#1075F这些年来……真是谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x10F,
        (
            "#1955F#6P#40W姐、姐姐……\x01",
            "我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x14,
        (
            "\x07\x0C#1476F#5P#40W呵呵……\x01",
            "莉丝也要好好照顾凯文哦。\x02\x03",

            "#1475F你们两个……\x01",
            "要永远地、快乐地相处下去啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x10F,
        (
            "#1950F#6P#40W……姐、姐姐……\x02\x03",

            "#1952F……嗯……！\x01",
            "我们会的……所以……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x109,
        (
            "#1848F#12P#40W再见了……\x01",
            "……露菲娜姐姐……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_99(0x109, 0x2C, 0x2F, 0x5DC)
    Sleep(250)
    OP_44(0x109, 0x2)

    def lambda_7DE7():
        OP_6D(1200, 15550, 3300, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7DE7)
    PlayEffect(0x2, 0x3, 0x109, 0, 1150, 1300, 0, 0, 0, 1000, 1000, 1000, 0x14, 0, 1000, 0, 0)

    def lambda_7E34():
        OP_99(0xFE, 0x31, 0x37, 0x7D0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E34)
    OP_22(0x2C5, 0x0, 0x64)
    Sleep(200)
    OP_22(0x22B, 0x0, 0x50)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)

    def lambda_7E63():
        OP_99(0xFE, 0x6, 0xC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7E63)
    OP_22(0x20C, 0x0, 0x46)
    WaitChrThread(0x14, 0x0)
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x3, 0x2, 0x14, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_44(0x109, 0x3)
    Fade(1000)
    OP_6D(180, 15550, 4019, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(0, 0)
    OP_6E(372, 0)
    SetChrPos(0x14, 0, 15550, 2800, 180)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x14, 0)
    SetChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x20)
    SetChrPos(0x109, 440, 15550, -3340, 0)
    SetChrPos(0x10F, 30, 15550, -3340, 0)
    SetChrChipByIndex(0x109, 11)
    SetChrSubChip(0x109, 39)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    PlayEffect(0x3, 0x2, 0x14, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(130)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_0D()

    def lambda_7FEE():

        label("loc_7FEE")

        OP_99(0xFE, 0x5, 0xC, 0x3E8)
        OP_48()
        Jump("loc_7FEE")

    QueueWorkItem2(0x14, 0, lambda_7FEE)

    def lambda_8001():
        OP_8F(0xFE, 0x0, 0x4718, 0xFA0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_8001)
    Sleep(500)

    def lambda_8021():
        OP_6D(0, 17650, 9770, 4500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8021)

    def lambda_8039():
        OP_67(0, 1700, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8039)

    def lambda_8051():
        OP_6B(2700, 4500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8051)

    def lambda_8061():
        OP_6E(389, 4500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8061)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x14, 0x1)
    Sleep(500)

    def lambda_8080():
        OP_99(0xFE, 0xD, 0x15, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8080)
    WaitChrThread(0x14, 0x0)

    def lambda_8095():

        label("loc_8095")

        OP_99(0xFE, 0x16, 0x1D, 0x3E8)
        OP_48()
        Jump("loc_8095")

    QueueWorkItem2(0x14, 0, lambda_8095)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_80BB():
        OP_6D(0, 18000, 9770, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80BB)

    def lambda_80D3():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_80D3)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x14, 0, 500, -2500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 500)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    WaitChrThread(0x109, 0x2)
    LoadEffect(0x4, "map\\mp275_00.eff")
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x89, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(1000)
    PlayEffect(0x4, 0x4, 0x14, 0, 500, 0, 0, -30, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x5, 0x14, 0, 0, 0, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)

    def lambda_82C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_82C4)
    OP_22(0x146, 0x1, 0x3C)
    OP_22(0x1B0, 0x0, 0x64)

    def lambda_82E0():
        OP_6D(0, 17600, 9770, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_82E0)

    def lambda_82F8():
        OP_67(0, 1050, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_82F8)

    def lambda_8310():
        OP_6B(3300, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8310)

    def lambda_8320():
        OP_6E(462, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8320)
    WaitChrThread(0x14, 0x1)
    OP_23(0x146)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x80)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x3)
    Sleep(500)

    ChrTalk(    #238 op#A
        0x10F,
        "#1949F#5P#40W#15A…………啊……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(230, 15550, -2790, 0)
    OP_67(0, 4610, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(180000, 0)
    OP_6E(456, 0)

    def lambda_83E7():
        OP_6B(1900, 50000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_83E7)
    SetChrPos(0x109, 430, 15550, -1220, 0)
    SetChrPos(0x10F, 0, 15550, -1190, 0)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 3)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x109, 0x8, 0xD, 0x4B0)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    Sleep(500)

    ChrTalk(    #239
        0x10F,
        "#1956F#11P#60W………呜呜…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_44(0x10F, 0x0)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #240
        0x10F,
        "#1957F#11P#60W…………啊啊……………\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x10, 0x16, 0x4B0)
    Sleep(500)

    ChrTalk(    #241
        0x109,
        "#1067F#5P#40W……莉丝……坚强点。\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x18, 0x1A, 0x3E8)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x109, 0x1B, 0x1E, 0x3E8)
    OP_99(0x109, 0x30, 0x34, 0x3E8)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #242
        0x109,
        (
            "#1848F#5P#40W总有一天……\x01",
            "我们一定会到达那里的。\x02\x03",

            "姐姐梦寐以求的……\x01",
            "想要到达的那个境界……\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x109, 0x20, 0x22, 0x3E8)
    Sleep(500)

    ChrTalk(    #243
        0x109,
        (
            "#1075F#5P#40W或许……\x01",
            "姐姐已经比我们两个先出发了……\x02\x03",

            "……所以，我们一定………\x02\x03",

            "#1840F我们……一定能和她再相会的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #244
        0x10F,
        "#1956F#11P#60W呜呜呜……啊啊啊啊……\x02",
    )

    CloseMessageWindow()

    def lambda_86F6():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_86F6)

    def lambda_8706():
        OP_6E(485, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8706)

    def lambda_8716():
        OP_67(0, 6500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8716)
    Sleep(1000)

    ChrTalk(    #245 op#A op#5
        0x10F,
        "#1957F#4S#25A#11P呜啊啊啊啊啊啊啊啊！\x05\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    FadeToDark(3000, 16777215, -1)
    CloseMessageWindow()
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    Sleep(1000)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_20(0x1388)
    OP_21()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_DC(0x0, 0x0)
    OP_A2(0x2508)
    NewScene("ED6_DT21/M7408   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_5CDE end

    def Function_9_87C2(): pass

    label("Function_9_87C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_880E")
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_9_87C2")

    label("loc_880E")

    Return()

    # Function_9_87C2 end

    SaveToFile()

Try(main)
