from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5412   ._SN',
        MapName             = 'Other',
        Location            = 'C5412.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        '亡命守护者',                           # 9
        '目标探索者',                           # 10
        '目标探索者',                           # 11
        '哨兵570（蓝）',                        # 12
        '哨兵570（蓝）',                        # 13
        '目标探索者',                           # 14
        '哨兵235（红）',                        # 15
        '哨兵235（红）',                        # 16
        '亡命守护者',                           # 17
        '目标探索者',                           # 18
        '目标探索者',                           # 19
        '哨兵570（蓝）',                        # 20
        '哨兵570（蓝）',                        # 21
        '目标探索者',                           # 22
        '哨兵235（红）',                        # 23
        '哨兵235（红）',                        # 24
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12350 ._CH',             # 02
        'ED6_DT29/CH12351 ._CH',             # 03
        'ED6_DT29/CH12580 ._CH',             # 04
        'ED6_DT29/CH12581 ._CH',             # 05
        'ED6_DT29/CH12320 ._CH',             # 06
        'ED6_DT29/CH12321 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT29/CH12580P._CP',             # 04
        'ED6_DT29/CH12581P._CP',             # 05
        'ED6_DT29/CH12320P._CP',             # 06
        'ED6_DT29/CH12321P._CP',             # 07
    )

    DeclMonster(
        X                   = 980,
        Z                   = -1000,
        Y                   = 16570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x425,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16140,
        Z                   = -1000,
        Y                   = 43740,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14260,
        Z                   = -1000,
        Y                   = 43870,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17850,
        Z                   = -1000,
        Y                   = 145970,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12070,
        Z                   = -1000,
        Y                   = 145960,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2860,
        Z                   = -1000,
        Y                   = 174250,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17920,
        Z                   = -1000,
        Y                   = 202020,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12050,
        Z                   = -1000,
        Y                   = 201850,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 980,
        Z                   = -1000,
        Y                   = 16570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16140,
        Z                   = -1000,
        Y                   = 43740,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14260,
        Z                   = -1000,
        Y                   = 43870,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17850,
        Z                   = -1000,
        Y                   = 145970,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12070,
        Z                   = -1000,
        Y                   = 145960,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2860,
        Z                   = -1000,
        Y                   = 174250,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17920,
        Z                   = -1000,
        Y                   = 202020,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -12050,
        Z                   = -1000,
        Y                   = 201850,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2C3",          # 01, 1
        "Function_2_357",          # 02, 2
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x385, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2")
    Event(0, 2)

    label("loc_2C2")

    Return()

    # Function_0_2AA end

    def Function_1_2C3(): pass

    label("Function_1_2C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E1")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jump("loc_356")

    label("loc_32E")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_356")

    Return()

    # Function_1_2C3 end

    def Function_2_357(): pass

    label("Function_2_357")

    EventBegin(0x0)
    OP_6D(1030, -1000, -14910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    SetChrPos(0x101, 1630, -1000, -15000, 0)
    SetChrPos(0x102, 480, -1000, -15000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6D(580, -1000, 13910, 0)
    OP_67(0, 9110, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(27000, 0)
    OP_6E(642, 0)
    OP_0D()
    Sleep(1000)

    def lambda_42C():
        OP_6D(1030, -1000, -14910, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42C)

    def lambda_444():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_444)

    def lambda_45C():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_45C)
    OP_6E(234, 8000)

    ChrTalk(    #0
        0x101,
        (
            "#1000F好、好厉害……\x02\x03",

            "飞船里竟然有\x01",
            "这么大的起降场……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#1030F结社引以为傲的战斗空母、\x01",
            "『红色方舟』古罗力亚斯。\x02\x03",

            "能够容纳\x01",
            "１２艘飞艇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F真不得了……\x02\x03",

            "刚才出动了５艘。\x01",
            "那么还剩下７艘吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#1030F其中一艘\x01",
            "我已经确保来逃脱用了，\x02\x03",

            "在最深处的机库里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1000F嗯，明白了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C28)
    OP_28(0x99, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_2_357 end

    SaveToFile()

Try(main)
