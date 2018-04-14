from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1201   ._SN',
        MapName             = 'Bose',
        Location            = 'R1201.x',
        MapIndex            = 61,
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
        '古罗尼山道方向',                       # 9
        '拉文努山道方向',                       # 10
        '柏斯方向',                             # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10310 ._CH',             # 02
        'ED6_DT09/CH10311 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10350 ._CH',             # 06
        'ED6_DT09/CH10351 ._CH',             # 07
        'ED6_DT09/CH10550 ._CH',             # 08
        'ED6_DT09/CH10551 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10310P._CP',             # 02
        'ED6_DT09/CH10311P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10350P._CP',             # 06
        'ED6_DT09/CH10351P._CP',             # 07
        'ED6_DT09/CH10550P._CP',             # 08
        'ED6_DT09/CH10551P._CP',             # 09
    )

    DeclNpc(
        X                   = -348670,
        Z                   = 150,
        Y                   = 8790,
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
        X                   = -251150,
        Z                   = 0,
        Y                   = 36410,
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
        X                   = -206940,
        Z                   = 0,
        Y                   = -15170,
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
        X                   = -245780,
        Z                   = 10,
        Y                   = -13290,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -283410,
        Z                   = 510,
        Y                   = 3500,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -257890,
        Z                   = -80,
        Y                   = -19810,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -297320,
        Z                   = -10,
        Y                   = -50,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -321660,
        Z                   = 0,
        Y                   = 7860,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -258500,
        Y                   = -2000,
        Z                   = 23000,
        Range               = -243800,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x5EEC,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -268700,
        Y                   = -360,
        Z                   = -4580,
        Range               = -270570,
        Unknown_10          = 0x41A,
        Unknown_14          = 0xFFFFD79C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = -234940,
        TriggerZ            = 1020,
        TriggerY            = -22700,
        TriggerRange        = 1000,
        ActorX              = -234380,
        ActorZ              = 1020,
        ActorY              = -22890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -254930,
        TriggerZ            = 0,
        TriggerY            = 140,
        TriggerRange        = 1500,
        ActorX              = -254930,
        ActorZ              = 1300,
        ActorY              = 140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -261790,
        TriggerZ            = 0,
        TriggerY            = -2900,
        TriggerRange        = 1500,
        ActorX              = -261790,
        ActorZ              = 1500,
        ActorY              = -2900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -267850,
        TriggerZ            = 10,
        TriggerY            = -14960,
        TriggerRange        = 1000,
        ActorX              = -270790,
        ActorZ              = -1000,
        ActorY              = -16940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_2CA",          # 01, 1
        "Function_2_30D",          # 02, 2
        "Function_3_396",          # 03, 3
        "Function_4_459",          # 04, 4
        "Function_5_8A4",          # 05, 5
        "Function_6_B57",          # 06, 6
        "Function_7_C6E",          # 07, 7
        "Function_8_CBD",          # 08, 8
        "Function_9_D29",          # 09, 9
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2C9")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_2C9")

    Return()

    # Function_0_2B6 end

    def Function_1_2CA(): pass

    label("Function_1_2CA")

    OP_16(0x2, 0xFA0, 0xFFF9E580, 0xFFFE0FE8, 0x23001A)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F3")
    OP_1B(0x2, 0x0, 0x5)

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x360, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_305")
    OP_6F(0x0, 0)
    Jump("loc_30C")

    label("loc_305")

    OP_6F(0x0, 60)

    label("loc_30C")

    Return()

    # Function_1_2CA end

    def Function_2_30D(): pass

    label("Function_2_30D")

    EventBegin(0x0)
    OP_6D(-249620, -10, 18100, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -249620, -10, 18100, 180)
    SetChrPos(0x106, -249620, -10, 18100, 180)
    SetChrPos(0xF8, -249620, -10, 18100, 180)
    SetChrPos(0xF9, -249620, -10, 18100, 180)
    OP_A2(0x1A11)
    EventEnd(0x0)
    Return()

    # Function_2_30D end

    def Function_3_396(): pass

    label("Function_3_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    TurnDirection(0x106, 0x1, 400)

    ChrTalk(    #0
        0x106,
        (
            "#552F这边是拉文努村\x02\x03",

            "等手边的工作\x01",
            "告一段落后再过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D")

    label("loc_3F6")


    ChrTalk(    #1
        0x106,
        (
            "#555F喂……\x01",
            "这边是拉文努村啦。\x02\x03",

            "等手边的工作\x01",
            "告一段落后再过去啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_458")

    Return()

    # Function_3_396 end

    def Function_4_459(): pass

    label("Function_4_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_611")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BD")

    ChrTalk(    #2
        0x101,
        (
            "#1002F啊，好像走过头了。\x02\x03",

            "#1002F拉文努村是在\x01",
            "这座桥之前往北走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6")

    label("loc_4BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_529")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4E8")

    label("loc_4E1")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4E8")


    ChrTalk(    #3
        0x103,
        (
            "#022F稍微走过头了吧。\x02\x03",

            "拉文努村是在\x01",
            "这座桥之前往北走哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6")

    label("loc_529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_590")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    Jump("loc_54D")

    label("loc_546")

    TurnDirection(0x104, 0x0, 400)

    label("loc_54D")


    ChrTalk(    #4
        0x104,
        (
            "#030F看来好像走过头了。\x02\x03",

            "拉文努村是在\x01",
            "这座桥之前往北走哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F6")

    label("loc_590")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD")
    Jump("loc_5B4")

    label("loc_5AD")

    TurnDirection(0x108, 0x0, 400)

    label("loc_5B4")


    ChrTalk(    #5
        0x108,
        (
            "#070F看来好像走过头了啊。\x02\x03",

            "拉文努村是在\x01",
            "这座桥之前往北走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F6")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_611")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_72F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(    #6
        0x106,
        (
            "#050F要去拉文努村的话该往北才对。\x01",
            "没有时间绕远路了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72C")

    label("loc_677")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B8")

    ChrTalk(    #7
        0x103,
        (
            "#025F拉文努村在北边呢……\x01",
            "没有时间绕远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72C")

    label("loc_6B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F7")

    ChrTalk(    #8
        0x108,
        (
            "#072F拉文努村在北边吧。\x01",
            "没有时间绕远路啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72C")

    label("loc_6F7")


    ChrTalk(    #9
        0x101,
        (
            "#1015F拉文努村在北边吧。\x01",
            "现在不是绕远路的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72C")

    Jump("loc_888")

    label("loc_72F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78D")

    ChrTalk(    #10
        0x106,
        (
            "#053F要去拉文努村的话该往北吧。\x02\x03",

            "#050F带着同行者，\x01",
            "可没有时间绕远路了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_885")

    label("loc_78D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E0")

    ChrTalk(    #11
        0x103,
        (
            "#025F啊，拉文努村在北边吧。\x02\x03",

            "带着同行者，\x01",
            "可没有时间绕远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_885")

    label("loc_7E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_838")

    ChrTalk(    #12
        0x108,
        (
            "#073F哦，拉文努村在北边吧。\x02\x03",

            "#070F带着同行者，\x01",
            "可没有时间绕远路啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_885")

    label("loc_838")


    ChrTalk(    #13
        0x101,
        (
            "#1015F啊，拉文努村在北边吧。\x02\x03",

            "毕竟队伍中有同行者，\x01",
            "绕远路的事之后再说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_885")

    OP_A2(0x0)

    label("loc_888")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_8A3")

    Return()

    # Function_4_459 end

    def Function_5_8A4(): pass

    label("Function_5_8A4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9A2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EE")

    ChrTalk(    #14
        0x106,
        (
            "#050F拉文努村在北边吧。\x01",
            "没有时间绕远路了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_8EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92D")

    ChrTalk(    #15
        0x103,
        (
            "#020F拉文努村在北边吧。\x01",
            "没有时间绕远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_92D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96A")

    ChrTalk(    #16
        0x108,
        (
            "#070F拉文努村在北边。\x01",
            "没有时间绕远路啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99F")

    label("loc_96A")


    ChrTalk(    #17
        0x101,
        (
            "#1000F拉文努村在北边吧。\x01",
            "现在不是绕远路的时候。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99F")

    Jump("loc_AF3")

    label("loc_9A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(    #18
        0x106,
        (
            "#050F要去拉文努村的话该往北才对。\x02\x03",

            "带着同行者，\x01",
            "可没有时间绕远路了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF0")

    label("loc_9FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A50")

    ChrTalk(    #19
        0x103,
        (
            "#020F啊，拉文努村在北边吧。\x02\x03",

            "带着同行者，\x01",
            "可没有时间绕远路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF0")

    label("loc_A50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA3")

    ChrTalk(    #20
        0x108,
        (
            "#070F哦，拉文努村在北边吧。\x02\x03",

            "带着同行者，\x01",
            "可没有时间绕远路啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF0")

    label("loc_AA3")


    ChrTalk(    #21
        0x101,
        (
            "#1000F啊，拉文努村在北边吧。\x02\x03",

            "毕竟队伍中有同行者，\x01",
            "绕远路的事之后再说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF0")

    OP_A2(0x0)

    label("loc_AF3")

    OP_59()
    Fade(1000)
    SetChrPos(0x101, -332600, 40, 8970, 90)
    SetChrPos(0xF7, -332600, 40, 8970, 90)
    SetChrPos(0xF8, -332600, 40, 8970, 90)
    SetChrPos(0xF9, -332600, 40, 8970, 90)
    SetChrPos(0x147, -332600, 40, 8970, 90)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_5_8A4 end

    def Function_6_B57(): pass

    label("Function_6_B57")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x360, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_BC6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B05)
    Jump("loc_C2C")

    label("loc_BC6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_C2C")

    Jump("loc_C60")

    label("loc_C2F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C60")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B57 end

    def Function_7_C6E(): pass

    label("Function_7_C6E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #25
        "\x07\x05北　拉文努村　　１４７塞尔矩\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_C6E end

    def Function_8_CBD(): pass

    label("Function_8_CBD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        (
            "\x07\x05东　柏斯市　　　１４０塞尔矩\x01",
            "西　古罗尼山顶　３０１塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_CBD end

    def Function_9_D29(): pass

    label("Function_9_D29")

    EventBegin(0x1)

    ChrTalk(    #27
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_D55():
        OP_6D(-270600, 50, -15450, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D55)

    def lambda_D6D():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D6D)

    def lambda_D7D():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_D7D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E04")
    OP_C0(0xE, 0xB, 0xFFFBE9B6, 0xA, 0xFFFFC590, 0xE1, 0xFFFBDE3A, 0xFFFFFC18, 0xFFFFBDD4)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_E13")

    label("loc_E04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E13")
    EventEnd(0x1)

    label("loc_E13")

    Return()

    # Function_9_D29 end

    SaveToFile()

Try(main)
