from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0100   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0100.x',
        MapIndex            = 23,
        MapDefaultBGM       = "ed60029",
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
        '利吉',                                 # 9
        '旅行者',                               # 10
        '旅行者',                               # 11
        '旅行者',                               # 12
        '旅行者',                               # 13
        '洛连特方向',                           # 14
        '布莱特家方向',                         # 15
        '格鲁纳门方向',                         # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
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
        'ED6_DT09/CH10240 ._CH',             # 00
        'ED6_DT09/CH10241 ._CH',             # 01
        'ED6_DT09/CH10230 ._CH',             # 02
        'ED6_DT09/CH10231 ._CH',             # 03
        'ED6_DT09/CH10020 ._CH',             # 04
        'ED6_DT09/CH10021 ._CH',             # 05
        'ED6_DT09/CH10020 ._CH',             # 06
        'ED6_DT09/CH10021 ._CH',             # 07
        'ED6_DT09/CH10020 ._CH',             # 08
        'ED6_DT09/CH10021 ._CH',             # 09
        'ED6_DT09/CH10020 ._CH',             # 0A
        'ED6_DT09/CH10021 ._CH',             # 0B
        'ED6_DT07/CH01760 ._CH',             # 0C
        'ED6_DT07/CH01200 ._CH',             # 0D
        'ED6_DT07/CH01230 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01220 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10240P._CP',             # 00
        'ED6_DT09/CH10241P._CP',             # 01
        'ED6_DT09/CH10230P._CP',             # 02
        'ED6_DT09/CH10231P._CP',             # 03
        'ED6_DT09/CH10020P._CP',             # 04
        'ED6_DT09/CH10021P._CP',             # 05
        'ED6_DT09/CH10020P._CP',             # 06
        'ED6_DT09/CH10021P._CP',             # 07
        'ED6_DT09/CH10020P._CP',             # 08
        'ED6_DT09/CH10021P._CP',             # 09
        'ED6_DT09/CH10020P._CP',             # 0A
        'ED6_DT09/CH10021P._CP',             # 0B
        'ED6_DT07/CH01760P._CP',             # 0C
        'ED6_DT07/CH01200P._CP',             # 0D
        'ED6_DT07/CH01230P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01220P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -14030,
        Z                   = 1000,
        Y                   = 217340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -60890,
        Z                   = 1030,
        Y                   = 216800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39320,
        Z                   = 1000,
        Y                   = 90280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -47710,
        Z                   = 1070,
        Y                   = 180970,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x15,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13870,
        Z                   = 990,
        Y                   = 154000,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x16,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46050,
        Z                   = 970,
        Y                   = 122240,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x17,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28090,
        Z                   = 2080,
        Y                   = 121460,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x14,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -22940,
        Y                   = 0,
        Z                   = 197540,
        Range               = -5430,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x30AC0,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -44530,
        Y                   = 500,
        Z                   = 103860,
        Range               = -33910,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1A054,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -36800,
        TriggerZ            = 1000,
        TriggerY            = 152300,
        TriggerRange        = 1500,
        ActorX              = -36800,
        ActorZ              = 2500,
        ActorY              = 152800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39100,
        TriggerZ            = 1000,
        TriggerY            = 153300,
        TriggerRange        = 1500,
        ActorX              = -39100,
        ActorZ              = 2200,
        ActorY              = 153300,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_32B",          # 01, 1
        "Function_2_397",          # 02, 2
        "Function_3_C7F",          # 03, 3
        "Function_4_CA5",          # 04, 4
        "Function_5_CCB",          # 05, 5
        "Function_6_CF1",          # 06, 6
        "Function_7_D17",          # 07, 7
        "Function_8_DB3",          # 08, 8
        "Function_9_E05",          # 09, 9
        "Function_10_F07",         # 0A, 10
        "Function_11_F73",         # 0B, 11
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Return()

    # Function_0_32A end

    def Function_1_32B(): pass

    label("Function_1_32B")

    OP_16(0x2, 0xFA0, 0xFFFD7F60, 0x6D60, 0x230008)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_354")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    OP_B5(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_381")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_396")

    label("loc_381")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_396")

    Return()

    # Function_1_32B end

    def Function_2_397(): pass

    label("Function_2_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A4")
    Return()

    label("loc_3A4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C4")
    Call(0, 7)
    FadeToBright(0, 0)
    Call(0, 8)

    label("loc_3C4")

    Fade(1000)
    OP_6D(-14210, 1000, 198480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -14640, 1000, 198480, 0)
    SetChrPos(0x103, -13640, 1000, 198480, 0)
    SetChrPos(0xF8, -14890, 1000, 197480, 0)
    SetChrPos(0xF9, -13390, 1000, 197480, 0)
    OP_0D()
    SetChrPos(0x8, -14040, 1000, 212170, 180)

    NpcTalk(    #0
        0x8,
        "青年的声音",
        "#4P啊……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #1
        0x8,
        "青年的声音",
        (
            "#4P那不是\x01",
            "前辈吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F3")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_531")

    label("loc_4F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_531")

    label("loc_51A")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_531")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_596")

    label("loc_558")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_596")

    label("loc_57F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_596")

    Sleep(1000)

    def lambda_5A1():
        OP_6D(-13440, 1000, 202010, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A1)

    def lambda_5B9():
        OP_67(0, 8050, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B9)

    def lambda_5D1():
        OP_6C(49000, 2500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D1)

    def lambda_5E1():
        OP_6E(293, 2500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E1)
    SetChrPos(0x8, -13760, 1000, 215490, 180)
    SetChrPos(0x9, -13260, 1000, 215490, 180)
    SetChrPos(0xA, -14260, 1000, 215490, 180)
    SetChrPos(0xB, -13260, 1000, 215490, 180)
    SetChrPos(0xC, -14260, 1000, 215490, 180)
    ClearChrFlags(0x8, 0x80)

    def lambda_64B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFCB44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64B)
    Sleep(500)
    ClearChrFlags(0x9, 0x80)

    def lambda_670():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFCF2C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_670)
    Sleep(100)
    ClearChrFlags(0xA, 0x80)

    def lambda_695():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFCF2C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_695)
    Sleep(500)
    ClearChrFlags(0xB, 0x80)

    def lambda_6BA():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD314, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6BA)
    Sleep(100)
    ClearChrFlags(0xC, 0x80)

    def lambda_6DF():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD314, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6DF)
    WaitChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第４章和利吉再会过】\x01",          # 0
            "【◇在第４章没有和利吉再会过】\x01",      # 1
            "【◇不变更】\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_78F"),
        (1, "loc_795"),
        (SWITCH_DEFAULT, "loc_79B"),
    )


    label("loc_78F")

    OP_A3(0x1880)
    Jump("loc_79B")

    label("loc_795")

    OP_A2(0x1880)
    Jump("loc_79B")

    label("loc_79B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_931")

    ChrTalk(    #2
        0x103,
        "#023F#2P哎呀，这不是利吉吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1011F#6P利吉先生，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#5P啊，艾丝蒂尔。\x01",
            "自从你到训练场后就没再见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#5P我听爱娜说过了。\x01",
            "说你在做很重要的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1016F#6P嗯，是呀。\x02\x03",

            "#1015F利吉先生是在\x01",
            "进行护卫的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#5P嗯，这些客人\x01",
            "好像有急事要去王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#5P按现在这种情形，\x01",
            "今天的定期船恐怕也没法航行了，\x01",
            "所以就由我送他们过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1006F#6P原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C6")

    label("loc_931")


    ChrTalk(    #10
        0x103,
        "#020F#2P哎呀，这不是利吉吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1011F#6P要出发去王都了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#5P嗯，客人已经\x01",
            "全部到齐了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#5P到那边之后，我也要\x01",
            "顺便去一趟王都支部。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C6")


    ChrTalk(    #14
        0x103,
        "#021F#2P呵呵，辛苦了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#5P前辈你们才是。\x01",
            "雾的调查工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "#5P街道的状況怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#020F#2P艾利兹街道的雾\x01",
            "并没有扩散得很远。\x02\x03",

            "稍走一走\x01",
            "立刻视野就开阔了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#5P呼，那太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#5P那么\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #20
        0x8,
        (
            "#4P各位，\x01",
            "我们出发前往王都吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#4P请不要离我太远啊！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x9,
        "商人",
        "#2P噢！拜托了。\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0xA,
        "旅行者",
        "#1P全靠你了啊，游击士先生。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1811)
    OP_8C(0x8, 180, 400)

    def lambda_B49():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B49)
    Sleep(50)

    def lambda_B69():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B69)
    Sleep(30)

    def lambda_B89():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B89)
    Sleep(50)

    def lambda_BA9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BA9)
    Sleep(30)

    def lambda_BC9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFC568, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BC9)
    Sleep(300)
    OP_43(0x101, 0x1, 0x0, 0x3)
    Sleep(50)
    OP_43(0x103, 0x1, 0x0, 0x4)
    Sleep(200)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(50)
    OP_43(0xF9, 0x1, 0x0, 0x6)

    def lambda_C14():
        OP_6D(-15630, 1000, 200190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C14)

    def lambda_C2C():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C2C)

    def lambda_C44():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_C44)
    WaitChrThread(0x8, 0x1)
    OP_44(0x0, 0x3)
    OP_44(0x1, 0x3)
    OP_44(0x2, 0x3)
    OP_44(0x3, 0x3)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_397 end

    def Function_3_C7F(): pass

    label("Function_3_C7F")

    OP_8F(0xFE, 0xFFFFC2F2, 0x3E8, 0x30DFE, 0x7D0, 0x0)

    def lambda_C99():

        label("loc_C99")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_C99")

    QueueWorkItem2(0xFE, 3, lambda_C99)
    Return()

    # Function_3_C7F end

    def Function_4_CA5(): pass

    label("Function_4_CA5")

    OP_8F(0xFE, 0xFFFFC2F2, 0x3E8, 0x30A16, 0x7D0, 0x0)

    def lambda_CBF():

        label("loc_CBF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CBF")

    QueueWorkItem2(0xFE, 3, lambda_CBF)
    Return()

    # Function_4_CA5 end

    def Function_5_CCB(): pass

    label("Function_5_CCB")

    OP_8F(0xFE, 0xFFFFC2F2, 0x3E8, 0x3062E, 0x7D0, 0x0)

    def lambda_CE5():

        label("loc_CE5")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CE5")

    QueueWorkItem2(0xFE, 3, lambda_CE5)
    Return()

    # Function_5_CCB end

    def Function_6_CF1(): pass

    label("Function_6_CF1")

    OP_8F(0xFE, 0xFFFFC2F2, 0x3E8, 0x30246, 0x7D0, 0x0)

    def lambda_D0B():

        label("loc_D0B")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_D0B")

    QueueWorkItem2(0xFE, 3, lambda_D0B)
    Return()

    # Function_6_CF1 end

    def Function_7_D17(): pass

    label("Function_7_D17")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D94"),
        (1, "loc_D9A"),
        (SWITCH_DEFAULT, "loc_DA0"),
    )


    label("loc_D94")

    OP_A2(0x1200)
    Jump("loc_DA0")

    label("loc_D9A")

    OP_A2(0x1201)
    Jump("loc_DA0")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DAE")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_DB2")

    label("loc_DAE")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_DB2")

    Return()

    # Function_7_D17 end

    def Function_8_DB3(): pass

    label("Function_8_DB3")

    ClearMapFlags(0x1)
    OP_6D(20400, 1640, 198520, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_8_DB3 end

    def Function_9_E05(): pass

    label("Function_9_E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7E")
    EventBegin(0x1)

    ChrTalk(    #24
        0x101,
        (
            "#505F啊，走过头了。\x01",
            "必须快点回家才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x142, 0x0, 400)

    ChrTalk(    #25
        0x142,
        "#1060F呵呵，早点回去吧。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_F06")

    label("loc_E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F06")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA2")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_EA9")

    label("loc_EA2")

    TurnDirection(0x103, 0x0, 400)

    label("loc_EA9")


    ChrTalk(    #26
        0x103,
        (
            "#020F这边和城里是反方向啊。\x02\x03",

            "不要耽误时间了，\x01",
            "快点去协会吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_F06")

    Return()

    # Function_9_E05 end

    def Function_10_F07(): pass

    label("Function_10_F07")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        (
            "\x07\x05北　洛连特市　　　４９塞尔矩\x01",
            "南　格鲁纳门　　２５９塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_F07 end

    def Function_11_F73(): pass

    label("Function_11_F73")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #28
        "\x07\x05西　布莱特家\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_F73 end

    SaveToFile()

Try(main)
