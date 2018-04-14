from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0610   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0610.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0610_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '罗宾队长',                             # 9
        '古利乌副队长',                         # 10
        '士兵安顿',                             # 11
        '萨姆',                                 # 12
        '亚米丽',                               # 13
        '拜舍尔',                               # 14
        '利吉',                                 # 15
        '旅行者',                               # 16
        '旅行者',                               # 17
        '旅行者',                               # 18
        '旅行者',                               # 19
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT26/CH20237 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01233 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01220 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT26/CH20237P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01233P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01220P._CP',             # 0B
    )

    DeclNpc(
        X                   = -19380,
        Z                   = 0,
        Y                   = -980,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -111940,
        Z                   = 0,
        Y                   = 21850,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -7220,
        Z                   = 0,
        Y                   = 2820,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -90130,
        Z                   = 0,
        Y                   = -22320,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -57740,
        Z                   = 0,
        Y                   = -21510,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -63920,
        Z                   = 0,
        Y                   = -22680,
        Direction           = 250,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -5350,
        Z                   = 0,
        Y                   = 880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -60600,
        Z                   = 0,
        Y                   = -27550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -59280,
        Z                   = 100,
        Y                   = -26820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -94140,
        Z                   = 0,
        Y                   = -28140,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -95590,
        Z                   = 0,
        Y                   = -25980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    DeclActor(
        TriggerX            = -7430,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = -7220,
        ActorZ              = 1500,
        ActorY              = 2820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -109840,
        TriggerZ            = 0,
        TriggerY            = 21450,
        TriggerRange        = 1000,
        ActorX              = -111940,
        ActorZ              = 1500,
        ActorY              = 21850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92220,
        TriggerZ            = 0,
        TriggerY            = -22040,
        TriggerRange        = 1000,
        ActorX              = -90130,
        ActorZ              = 1500,
        ActorY              = -22320,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_3DA",          # 01, 1
        "Function_2_442",          # 02, 2
        "Function_3_466",          # 03, 3
        "Function_4_46B",          # 04, 4
        "Function_5_470",          # 05, 5
        "Function_6_475",          # 06, 6
        "Function_7_CFA",          # 07, 7
        "Function_8_1324",         # 08, 8
        "Function_9_1A00",         # 09, 9
        "Function_10_215F",        # 0A, 10
        "Function_11_2A2E",        # 0B, 11
        "Function_12_2AD6",        # 0C, 12
        "Function_13_2E88",        # 0D, 13
        "Function_14_2F07",        # 0E, 14
        "Function_15_2F6D",        # 0F, 15
        "Function_16_2FAB",        # 10, 16
        "Function_17_3008",        # 11, 17
        "Function_18_3065",        # 12, 18
        "Function_19_3970",        # 13, 19
        "Function_20_39CC",        # 14, 20
        "Function_21_3A28",        # 15, 21
        "Function_22_3F1A",        # 16, 22
        "Function_23_4457",        # 17, 23
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2F2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_319")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52400, 0, 23230, 0)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jump("loc_3D9")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_360")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_338")
    ClearChrFlags(0xD, 0x80)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_35D")

    Jump("loc_3D9")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_3D9")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0x9, 0x80)
    OP_64(0x1, 0x1)
    Jump("loc_3D9")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrPos(0x8, -19540, 0, 1620, 109)
    SetChrFlags(0x8, 0x10)
    OP_43(0x8, 0x0, 0x6, 0x2)
    SetChrPos(0x9, -17890, 0, 1620, 271)
    SetChrFlags(0x9, 0x10)
    OP_64(0x1, 0x1)
    Jump("loc_3D9")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_3D9")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3D2")
    Jump("loc_3D9")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3D9")

    label("loc_3D9")

    Return()

    # Function_0_2D6 end

    def Function_1_3DA(): pass

    label("Function_1_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2")
    OP_B1("t0610_y")
    Jump("loc_3FB")

    label("loc_3F2")

    OP_B1("t0610_n")

    label("loc_3FB")

    OP_1C(0x5, 0x0, 0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    OP_1B(0x0, 0x0, 0x15)
    Jump("loc_425")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425")
    OP_1B(0x1, 0x0, 0x16)

    label("loc_425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_6F(0x5, 100)
    OP_72(0x5, 0x10)
    OP_64(0x1, 0x1)

    label("loc_441")

    Return()

    # Function_1_3DA end

    def Function_2_442(): pass

    label("Function_2_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_465")
    OP_8D(0xFE, -22660, -4810, -14730, 1940, 3000)
    Jump("Function_2_442")

    label("loc_465")

    Return()

    # Function_2_442 end

    def Function_3_466(): pass

    label("Function_3_466")

    Call(0, 9)
    Return()

    # Function_3_466 end

    def Function_4_46B(): pass

    label("Function_4_46B")

    Call(0, 7)
    Return()

    # Function_4_46B end

    def Function_5_470(): pass

    label("Function_5_470")

    Call(0, 8)
    Return()

    # Function_5_470 end

    def Function_6_475(): pass

    label("Function_6_475")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #0
        0xFE,
        (
            "不仅仅是这里，\x01",
            "王国各地的据点\x01",
            "全都处于警戒态势。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "例外的地方\x01",
            "也就只有沃尔费要塞了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "那里总是\x01",
            "有自己的一套方法。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_561")

    label("loc_50F")


    ChrTalk(    #3
        0xFE,
        (
            "王国各地的据点\x01",
            "全都处于警戒态势。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "例外的地方\x01",
            "也就只有沃尔费要塞了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561")

    Jump("loc_CF6")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62C")

    ChrTalk(    #5
        0xFE,
        (
            "哎呀，你们是游击士吧。\x01",
            "工作辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "虽然用分配的发生器\x01",
            "修复了通信机，\x01",
            "但是状况依然很严峻啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "现在粮食储备\x01",
            "也还充足……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "为了防止事态长期化，\x01",
            "必须尽快制订对策。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6B4")

    label("loc_62C")


    ChrTalk(    #9
        0xFE,
        (
            "现在，关所加强了警戒，\x01",
            "通行的审查也很严格……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "由于高层部门的命令，\x01",
            "游击士可以\x01",
            "自由通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "当然，也期待\x01",
            "你们有相应的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4")

    Jump("loc_CF6")

    label("loc_6B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_7C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_730")

    ChrTalk(    #12
        0xFE,
        (
            "互不侵犯条约也平安签订了，\x01",
            "洛连特的雾也都散去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "我也松了口气，\x01",
            "阿斯顿队长也是同样的想法吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE")

    label("loc_730")


    ChrTalk(    #14
        0xFE,
        (
            "互不侵犯条约也平安签订了，\x01",
            "洛连特的雾也都散去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "今天早上的太阳把两件烦心事\x01",
            "同时赶跑了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "这下就能安心\x01",
            "返回日常的任务了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7BE")

    Jump("loc_CF6")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_8B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_82C")

    ChrTalk(    #17
        0xFE,
        (
            "让人成长\x01",
            "最有效的药就是责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "威尔特桥的新兵们，\x01",
            "希望这次事件让他们脱胎换骨了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B4")

    label("loc_82C")


    ChrTalk(    #19
        0xFE,
        (
            "那么说来，阿斯顿队长\x01",
            "正为新兵教育而烦恼呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "让人成长\x01",
            "最有效的药就是责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "洛连特这里的警备任务\x01",
            "能让他们成长就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8B4")

    Jump("loc_CF6")

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_9BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_912")

    ChrTalk(    #22
        0xFE,
        (
            "威尔特桥的部队不久\x01",
            "也将到达洛连特吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "交给他们\x01",
            "应该就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BB")

    label("loc_912")


    ChrTalk(    #24
        0xFE,
        (
            "洛连特市似乎也发生了\x01",
            "令人担心的事件呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "王国军也为了市民的安全\x01",
            "决定派遣部队了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "威尔特桥的部队不久\x01",
            "也将到达洛连特吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "交给他们\x01",
            "应该就没问题了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9BB")

    Jump("loc_CF6")

    label("loc_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_A3C")

    ChrTalk(    #28
        0xFE,
        (
            "洛连特的雾\x01",
            "说不定还挺严重的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "雾可能也会\x01",
            "扩散到这附近来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "还是加强一下士兵们\x01",
            "的警戒比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA0")

    label("loc_A3C")


    ChrTalk(    #31
        0xFE,
        (
            "定期船赛希莉亚号\x01",
            "好像滞留在洛连特无法起航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "竟能让飞船无法出航，\x01",
            "这样的雾真是前所未见啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA0")

    Jump("loc_CF6")

    label("loc_AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B34")

    ChrTalk(    #33
        0xFE,
        (
            "飞在空中的巨大人偶，\x01",
            "我们的士兵好像也亲眼看到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "听说是向湖中央方向\x01",
            "飞去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "但连王国军自豪的警备艇\x01",
            "好像也找不到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_BBD")

    ChrTalk(    #36
        0xFE,
        "『结社』……吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "竟突然袭击警备本部 \x01",
            "所在的离宫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "虽不知道到底是个什么样的组织，\x01",
            "总之还是做好万全的准备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_BF4")

    ChrTalk(    #39
        0xFE,
        (
            "……完毕，请立即\x01",
            "组织巡回周游道的部队。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_C77")

    ChrTalk(    #40
        0xFE,
        (
            "格兰赛尔留驻的所有部队\x01",
            "都接到了强化警备的通知。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "签字仪式如能平安进行\x01",
            "是最好不过，但预防事态不测\x01",
            "是我们的工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #42
        0xFE,
        (
            "呀，你好。\x01",
            "现在大门四处都能自由参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "请自便。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_CF6")

    ChrTalk(    #44
        0xFE,
        "呀，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "想去洛连特时\x01",
            "请在接待处办手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF6")

    TalkEnd(0x8)
    Return()

    # Function_6_475 end

    def Function_7_CFA(): pass

    label("Function_7_CFA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_DFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D6A")

    ChrTalk(    #46
        0x9,
        (
            "听说在洛连特滞留的\x01",
            "定期船也恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "签字仪式的出席者们\x01",
            "也按照预定踏上了归途。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF8")

    label("loc_D6A")


    ChrTalk(    #48
        0x9,
        (
            "听说在洛连特滞留的\x01",
            "定期船也恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "签字仪式的出席者们\x01",
            "也按照预定踏上了归途。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "虽然令人捏了一把冷汗，\x01",
            "总算是平安结束了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DF8")

    Jump("loc_1320")

    label("loc_DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E72")

    ChrTalk(    #51
        0x9,
        (
            "威尔特桥那里\x01",
            "其实也有很好的钓鱼地点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "隐蔽在非常不在意的地方呢。\x01",
            "是懂的人才能找到的好地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F20")

    label("loc_E72")


    ChrTalk(    #53
        0x9,
        (
            "威尔特桥的守备队\x01",
            "据说已经开始对\x01",
            "洛连特市的警备了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "唔唔，话说回来\x01",
            "威尔特桥啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "……其实那里\x01",
            "也有很好的钓鱼地点哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "如果报名会不会\x01",
            "被编入补充部队呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F20")

    Jump("loc_1320")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F92")

    ChrTalk(    #57
        0x9,
        (
            "最近真是诸多事忙啊。\x01",
            "钓鱼的机会也减少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "等签字仪式结束了，\x01",
            "真想悠闲地垂钓一番啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1010")

    label("loc_F92")


    ChrTalk(    #59
        0x9,
        "雾越来越浓了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "签字仪式结束之后\x01",
            "虽然偷偷盘算着\x01",
            "去钓个鱼什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "唔唔，这么大的雾\x01",
            "附近的钓鱼场也去不了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1010")

    Jump("loc_1320")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_10DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_104B")

    ChrTalk(    #62
        0x9,
        (
            "外边好像挺热闹的……\x01",
            "有谁来了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D9")

    label("loc_104B")


    ChrTalk(    #63
        0x9,
        "明天就是签字仪式了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "回想百日战役的事，\x01",
            "简直像梦一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "嗯，这个先不提了，\x01",
            "目前的问题是这个雾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        "还好现在旅客比较少。\x02",
    )

    CloseMessageWindow()

    label("loc_10D9")

    Jump("loc_1320")

    label("loc_10DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_115A")

    ChrTalk(    #67
        0x9,
        (
            "迷雾峡谷的训练基地\x01",
            "好像被空贼袭击了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "看起来像是顺着格兰赛尔的事件\x01",
            "趁火打劫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        "唉，是我想太多了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_115A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_1183")

    ChrTalk(    #70
        0x9,
        (
            "……明白了，\x01",
            "我立即安排。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1218")

    ChrTalk(    #71
        0x9,
        (
            "收到了情报部余党\x01",
            "在柏斯出现的消息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "他们也有可能会\x01",
            "妨碍签字仪式……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "总之\x01",
            "我们的任务是守护这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "必须专心执行任务才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_12BC")

    ChrTalk(    #75
        0x9,
        (
            "帝国大使和共和国大使，\x01",
            "听说两人完全处不来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "因为原本就是两个水火不容的国家，\x01",
            "这也难怪，倒是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "那样的两国\x01",
            "真的能缔结\x01",
            "互不侵犯条约吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1320")

    ChrTalk(    #78
        0x9,
        "嗯？有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "现在正在做\x01",
            "警备的编成表呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "因为马上就是条约的签字仪式了嘛。\x02",
    )

    CloseMessageWindow()

    label("loc_1320")

    TalkEnd(0x9)
    Return()

    # Function_7_CFA end

    def Function_8_1324(): pass

    label("Function_8_1324")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_141E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C5")

    ChrTalk(    #81
        0xA,
        (
            "吃饭时的话题还是\x01",
            "那个浮游岛的事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "至今还不清楚那到底是什么。\x01",
            "真是令人害怕啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "虽然只是浮在那里，\x01",
            "但还是感到不安……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_141B")

    label("loc_13C5")


    ChrTalk(    #84
        0xA,
        (
            "浮游岛到底是什么，\x01",
            "好像还不清楚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "虽然只是浮在那里，\x01",
            "还是令人感到不安……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141B")

    Jump("loc_19FC")

    label("loc_141E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1536")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E7")

    ChrTalk(    #86
        0xA,
        (
            "最近那场雾就够惊人的了，\x01",
            "真是天外有天啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "导力器竟然不能使用，\x01",
            "怎么会发生这种事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "都是因为这个今天早上的点心，\x01",
            "感觉也没那么好吃了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "明明吃饭是\x01",
            "少有的乐趣……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1533")

    label("loc_14E7")


    ChrTalk(    #90
        0xA,
        (
            "食堂的亚米丽也因为\x01",
            "不能用炉子而发愁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "明明吃饭是\x01",
            "少有的乐趣……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1533")

    Jump("loc_19FC")

    label("loc_1536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_15A8")

    ChrTalk(    #92
        0xA,
        (
            "此次的互不侵犯条约使得外国来的\x01",
            "旅客也增加了不少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "可要妥善对待他们，\x01",
            "不能丢了利贝尔人的脸呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_15A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_160E")

    ChrTalk(    #94
        0xA,
        (
            "七耀教会的巡回神父\x01",
            "平安到达洛连特了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "这种时候还去洛连特\x01",
            "呀～真是有胆量的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_16E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1677")

    ChrTalk(    #96
        0xA,
        (
            "总，总觉得雾\x01",
            "好像越来越浓了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "今天是签字仪式的日子。\x01",
            "希望不要发生什么事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16E0")

    label("loc_1677")


    ChrTalk(    #98
        0xA,
        (
            "总，总觉得雾\x01",
            "好像越来越浓了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        "今天是签字仪式的重要日子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "拜、拜托\x01",
            "不要发生什么事啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_16E0")

    Jump("loc_19FC")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_178E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_1739")

    ChrTalk(    #101
        0xA,
        (
            "洛连特起的雾\x01",
            "好像比想象中的还厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        "旅客们都疲惫不堪了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_178B")

    label("loc_1739")


    ChrTalk(    #103
        0xA,
        (
            "许可证发下来之前\x01",
            "要稍微花费点时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "签字仪式快到了，\x01",
            "警备也越来越严了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178B")

    Jump("loc_19FC")

    label("loc_178E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1804")

    ChrTalk(    #105
        0xA,
        (
            "一开始，听说周游道出现的\x01",
            "是『结社』的手下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "结果竟然是特务兵\x01",
            "的余党嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "究竟是怎么回事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_1804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1828")

    ChrTalk(    #108
        0xA,
        "啊，副队长去了哪里？\x02",
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_1828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_1881")

    ChrTalk(    #109
        0xA,
        (
            "呀，来城墙\x01",
            "观赏晚霞吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "现在这个时期来看\x01",
            "是最美丽的。\x01",
            "慢慢欣赏好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_1881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1914")

    ChrTalk(    #111
        0xA,
        (
            "今天早上开始就一直在说\x01",
            "情报部余党的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "那些家伙，在柏斯地区\x01",
            "到底图谋着什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "不过，无论如何\x01",
            "他们也过不了这格鲁纳门的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_1914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_19A0")

    ChrTalk(    #114
        0xA,
        (
            "如果要上城墙上参观，\x01",
            "请务必小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "听说前几天，有游客\x01",
            "在圣海姆门的长城上\x01",
            "差点掉下去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        (
            "千万别受伤了，\x01",
            "要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FC")

    label("loc_19A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_19FC")

    ChrTalk(    #117
        0xA,
        "哎呀，要去洛连特吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "去洛连特请到这边\x01",
            "柜台办理手续。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        "……咦，不是吧？\x02",
    )

    CloseMessageWindow()

    label("loc_19FC")

    TalkEnd(0xA)
    Return()

    # Function_8_1324 end

    def Function_9_1A00(): pass

    label("Function_9_1A00")

    TalkBegin(0xB)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A20")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1A20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A31")
    TalkEnd(0xB)
    Return()

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1B28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACF")

    ChrTalk(    #120
        0xB,
        (
            "最近的大雾刚刚散去，\x01",
            "现在又是这样的紧急状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "害的我店里\x01",
            "生意惨淡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "呼，期待下次诞辰庆典啊，\x01",
            "真是的，现在就等不及了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1B25")

    label("loc_1ACF")


    ChrTalk(    #123
        0xB,
        (
            "最近我这里\x01",
            "生意惨淡啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "呼，期待下次诞辰庆典啊，\x01",
            "真是的，现在就等不及了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B25")

    Jump("loc_215B")

    label("loc_1B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B82")

    ChrTalk(    #125
        0xB,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "这个时候还旅行，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "好好休息吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1BB7")

    label("loc_1B82")


    ChrTalk(    #128
        0xB,
        (
            "这个时候还旅行，\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        "好好休息吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1BB7")

    Jump("loc_215B")

    label("loc_1BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1C8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C15")

    ChrTalk(    #130
        0xB,
        (
            "今天真是久违的\x01",
            "好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "我们的床单现在\x01",
            "也散发着太阳的气味哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C89")

    label("loc_1C15")


    ChrTalk(    #132
        0xB,
        (
            "哟，今天是久违的\x01",
            "好天气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "我们的床单现在\x01",
            "也散发着太阳的气味哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "还是干干爽爽的\x01",
            "床单感觉舒服啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1C89")

    Jump("loc_215B")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CE3")

    ChrTalk(    #135
        0xB,
        (
            "空气这么潮湿，\x01",
            "洗了的床单也干不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "干脆塞进\x01",
            "烤炉里算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D56")

    label("loc_1CE3")


    ChrTalk(    #137
        0xB,
        (
            "空气这么潮湿，\x01",
            "洗了的床单也干不了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "就算是这样，再不替换\x01",
            "一会可就要长霉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        "啊啊，蓝天真可爱。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D56")

    Jump("loc_215B")

    label("loc_1D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_1E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DAB")

    ChrTalk(    #140
        0xB,
        (
            "现在床位都空着，\x01",
            "可以随便选啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        "不介意的话就请休息吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E27")

    label("loc_1DAB")


    ChrTalk(    #142
        0xB,
        (
            "哟，现在床位都空着，\x01",
            "可以随便选啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        (
            "今天有签字仪式，\x01",
            "但是从早上开始就是这么大雾。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        (
            "这也难怪客人\x01",
            "都变少了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1E27")

    Jump("loc_215B")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_1E7E")

    ChrTalk(    #145
        0xB,
        "雾有那么厉害吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "这格鲁纳门附近\x01",
            "从早上开始就是好天气啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(    #147
        0xB,
        (
            "本旅店欢迎任何人。\x01",
            "店里招待所有来这里的旅行者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        (
            "如果想住宿\x01",
            "就跟我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2B")

    label("loc_1EDA")


    ChrTalk(    #149
        0xB,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xB,
        (
            "这里是所有人都\x01",
            "喜爱的旅店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "如果想住宿\x01",
            "就跟我说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1F2B")

    Jump("loc_215B")

    label("loc_1F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1FA4")

    ChrTalk(    #152
        0xB,
        (
            "最近，士兵们\x01",
            "看来又忙起来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "要准备签字仪式吧，\x01",
            "好像还不止这个呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xB,
        "是不是和王都事件有关啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_1FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1FE9")

    ChrTalk(    #155
        0xB,
        (
            "哟，两位客人。\x01",
            "要住宿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xB,
        "抱歉今天旅馆被包下了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_2031")

    ChrTalk(    #157
        0xB,
        (
            "嗯？感觉好像\x01",
            "很慌张的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "哈哈，约会\x01",
            "迟到了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2087")

    ChrTalk(    #159
        0xB,
        (
            "好，今天天气好，\x01",
            "床单也都干啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        (
            "想享受太阳的香味，\x01",
            "就住在这里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_2087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #161
        0xB,
        (
            "现在王国军为了互不侵犯条约\x01",
            "的准备好像忙得不可开交呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xB,
        (
            "不愧是国家性的签字仪式啊。\x01",
            "要是被情报部那些家伙\x01",
            "捣乱了那可有失颜面啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_215B")

    label("loc_2118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_215B")

    ChrTalk(    #163
        0xB,
        "哟，这里是格鲁纳门的旅店。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        "不介意的话，就住下吧。\x02",
    )

    CloseMessageWindow()

    label("loc_215B")

    TalkEnd(0xB)
    Return()

    # Function_9_1A00 end

    def Function_10_215F(): pass

    label("Function_10_215F")

    TalkBegin(0xC)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_217F")
    OP_0D()
    OP_A9(0xB)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_217F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2190")
    TalkEnd(0xC)
    Return()

    label("loc_2190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_22A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_224D")

    ChrTalk(    #165
        0xFE,
        (
            "现在正在考虑\x01",
            "明天的菜单……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "如果炉子不能使用，\x01",
            "干脆就全做冷菜好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "冷汤加沙拉，\x01",
            "再加点白汁红肉之类的怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "虽然像饭前零食一样，\x01",
            "但好像挺华丽的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_229D")

    label("loc_224D")


    ChrTalk(    #169
        0xFE,
        (
            "如果炉子不能使用，\x01",
            "干脆全做冷菜好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "怎样增加分量，\x01",
            "好像是个问题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229D")

    Jump("loc_2A2A")

    label("loc_22A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234C")

    ChrTalk(    #171
        0xFE,
        "唉，今天真是糟糕透顶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "炉子不能使用，\x01",
            "只能随便做点料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "虽然这里的士兵很善良，\x01",
            "都说好吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "但我知道那是强颜欢笑，\x01",
            "反而更加难过。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_238F")

    label("loc_234C")


    ChrTalk(    #175
        0xFE,
        "唉，今天真是糟糕透顶。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "炉子不能使用，\x01",
            "只能随便做点料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238F")

    Jump("loc_2A2A")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_246C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23F3")

    ChrTalk(    #177
        0xFE,
        (
            "士兵们的表情\x01",
            "也终于开朗了起来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "今天的吃饭时间\x01",
            "似乎也会热闹起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2469")

    label("loc_23F3")


    ChrTalk(    #179
        0xFE,
        (
            "士兵们的表情\x01",
            "也终于开朗了起来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "今天的吃饭时间\x01",
            "似乎也会热闹起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "呜呼呼，我也要\x01",
            "努力做饭才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2469")

    Jump("loc_2A2A")

    label("loc_246C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_25C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_24D7")

    ChrTalk(    #182
        0xFE,
        (
            "今天的午饭\x01",
            "是卢安风味的鱼料理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "参考东方料理的手法，\x01",
            "进行了改进的自信作品呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BD")

    label("loc_24D7")


    ChrTalk(    #184
        0xFE,
        (
            "今天的午饭\x01",
            "是卢安风味的鱼料理哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "用香味蔬菜增加香味，\x01",
            "再用蒸锅加热。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "参考东方料理的手法，\x01",
            "进行了改进的自信作品哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "签字仪式的警备加上雾的事件……\x01",
            "士兵们也真够辛苦的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "至少要努力让他们\x01",
            "吃得开心才是。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_25BD")

    Jump("loc_2A2A")

    label("loc_25C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_264F")

    ChrTalk(    #189
        0xFE,
        (
            "东方料理的烹调法\x01",
            "有不少值得参考的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "如果能好好利用\x01",
            "应该也能用于利贝尔料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "并不是单纯的模仿，\x01",
            "而是要取其精粹哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2A")

    label("loc_264F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_27C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_26B7")

    ChrTalk(    #192
        0xFE,
        (
            "客人们看来\x01",
            "都是历经艰苦\x01",
            "才好不容易到了这里的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "得让他们\x01",
            "吃上好吃的东西才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BE")

    label("loc_26B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_271D")

    ChrTalk(    #194
        0xFE,
        (
            "最近，我买了本书\x01",
            "正在学习东方料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "为了学习到更多的料理手艺，\x01",
            "只有不断的挑战哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BE")

    label("loc_271D")


    ChrTalk(    #196
        0xFE,
        (
            "最近，我买了本书\x01",
            "正在学习东方料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "最感头痛的\x01",
            "是调味料不同呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "虽然找了相似的东西\x01",
            "尝试着做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "但是，东方来的客人\x01",
            "却说味道完全不一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_27BE")

    Jump("loc_2A2A")

    label("loc_27C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_28C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2872")

    ChrTalk(    #200
        0xFE,
        (
            "最近，对自己的\x01",
            "手艺感到不满啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "最大的原因还是\x01",
            "觉得菜式固定化了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "虽然以前也经常\x01",
            "挑战新的料理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "但是还要吸收\x01",
            "更多更多的要素才行吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_28C0")

    label("loc_2872")


    ChrTalk(    #204
        0xFE,
        (
            "虽然以前也经常\x01",
            "挑战新的料理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "但是还要吸收\x01",
            "更多更多的要素才行吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C0")

    Jump("loc_2A2A")

    label("loc_28C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_28FA")

    ChrTalk(    #206
        0xFE,
        (
            "副队长他们突然就走了，\x01",
            "发生什么事了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2A")

    label("loc_28FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_295C")

    ChrTalk(    #207
        0xFE,
        (
            "队长和副队长一脸严肃地\x01",
            "在开会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "发生什么事了呢？\x01",
            "连我也不知不觉紧张起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2A")

    label("loc_295C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_29AA")

    ChrTalk(    #209
        0xFE,
        (
            "嗯～这个味道\x01",
            "也差不多快吃腻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "士兵们好像\x01",
            "也不太喜欢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A2A")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2A00")
    TurnDirection(0xFE, 0x12F, 400)

    ChrTalk(    #211
        0xFE,
        (
            "哎呀，小姐，\x01",
            "白裙子非常适合你哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "不介意的话，吃点什么吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A2A")

    label("loc_2A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2A2A")

    ChrTalk(    #213
        0xFE,
        (
            "欢迎～\x01",
            "欢迎来到格鲁纳门食堂！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2A")

    TalkEnd(0xC)
    Return()

    # Function_10_215F end

    def Function_11_2A2E(): pass

    label("Function_11_2A2E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2AAB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "对话\x01",      # 0
            "报告\x01",      # 1
            "离开\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A94")
    Call(0, 12)
    Jump("loc_2AA8")

    label("loc_2A94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA8")
    Call(1, 3)
    Jump("loc_2AA8")

    label("loc_2AA8")

    Jump("loc_2AD2")

    label("loc_2AAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2ACE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2AC7")
    Call(1, 1)
    Jump("loc_2ACB")

    label("loc_2AC7")

    Call(1, 0)

    label("loc_2ACB")

    Jump("loc_2AD2")

    label("loc_2ACE")

    Call(0, 12)

    label("loc_2AD2")

    TalkEnd(0xD)
    Return()

    # Function_11_2A2E end

    def Function_12_2AD6(): pass

    label("Function_12_2AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2B0E")

    ChrTalk(    #214
        0xFE,
        "那么，就拜托各位了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "可不要出事故哦。\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_2B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2C62")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2B8C")

    ChrTalk(    #216
        0xFE,
        "钓鱼场的调查有进展吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "雾也散了，\x01",
            "应该容易很多了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "之前去不了的地方\x01",
            "麻烦特别仔细调查哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5F")

    label("loc_2B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2BD4")

    ChrTalk(    #219
        0xFE,
        (
            "那么……\x01",
            "总算雾也散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "我差不多\x01",
            "也该准备出发了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C5F")

    label("loc_2BD4")

    OP_A2(0xA)

    ChrTalk(    #221
        0xFE,
        (
            "那么……\x01",
            "总算雾也散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "我差不多\x01",
            "也该准备出发了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "由于雾调查的计划\x01",
            "大幅度延迟了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "再不努力调查\x01",
            "团长可要发火了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5F")

    Jump("loc_2E87")

    label("loc_2C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2D32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2CDD")

    ChrTalk(    #225
        0xFE,
        (
            "洛连特周边\x01",
            "好像还是有很厉害的雾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "钓鱼场的调查\x01",
            "别着急慢慢来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "脚踏实地地\x01",
            "做就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D2F")

    label("loc_2CDD")


    ChrTalk(    #228
        0xFE,
        (
            "洛连特周边的雾\x01",
            "好像还没散去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "真是的，那种状态\x01",
            "到底要持续到什么时候呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2F")

    Jump("loc_2E87")

    label("loc_2D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2DD1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2D82")

    ChrTalk(    #230
        0xFE,
        (
            "游击士们\x01",
            "也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "今天早上雾好像\x01",
            "还是很大。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DCE")

    label("loc_2D82")


    ChrTalk(    #232
        0xFE,
        (
            "听说今天早上的雾\x01",
            "比昨天更厉害了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "这下要\x01",
            "去街道上实在是太勉强了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DCE")

    Jump("loc_2E87")

    label("loc_2DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2E87")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_2E29")

    ChrTalk(    #234
        0xFE,
        (
            "哟，怎样？\x01",
            "调查有进展吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "雾好像很厉害，\x01",
            "不着急慢慢来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E87")

    label("loc_2E29")


    ChrTalk(    #236
        0xFE,
        "唉……真无聊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "可是，起这么大雾，\x01",
            "钓鱼也太勉强了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "现在就赏赏花\x01",
            "消遣消遣吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E87")

    Return()

    # Function_12_2AD6 end

    def Function_13_2E88(): pass

    label("Function_13_2E88")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0xFE,
        "呀，艾丝蒂尔你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "委托者们好像比想象中的\x01",
            "更加疲惫啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "决定今天就在格鲁纳门这休息，\x01",
            "明天再出发去王都。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2E88 end

    def Function_14_2F07(): pass

    label("Function_14_2F07")

    TalkBegin(0xFE)

    ChrTalk(    #242
        0xFE,
        (
            "想着雾中不知何时\x01",
            "会有魔兽来袭，\x01",
            "真是吓得要死……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "好不容易来到这里，\x01",
            "已经精疲力竭了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2F07 end

    def Function_15_2F6D(): pass

    label("Function_15_2F6D")

    TalkBegin(0xFE)

    ChrTalk(    #244
        0xFE,
        "呼，总算镇定下来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "心宽下来，\x01",
            "肚子就饿了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2F6D end

    def Function_16_2FAB(): pass

    label("Function_16_2FAB")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        (
            "呼，那个雾\x01",
            "到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "要是没有游击士陪同，\x01",
            "实在太危险了，根本出不去啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2FAB end

    def Function_17_3008(): pass

    label("Function_17_3008")

    TalkBegin(0xFE)

    ChrTalk(    #248
        0xFE,
        (
            "雾散了的时候\x01",
            "真是松了口气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "到了这里，似乎离王都\x01",
            "就很近了，可以放心了吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_3008 end

    def Function_18_3065(): pass

    label("Function_18_3065")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_6D(-16190, 4000, 40000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_22(0xC6, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x109, 0x1, 0x0, 0x13)
    Sleep(1800)
    OP_43(0x101, 0x1, 0x0, 0x14)
    OP_6D(-20500, 4000, 40500, 2000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #250
        0x101,
        (
            "#1005F等一下！\x01",
            "到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #251
        0x109,
        (
            "#1066F#5P啊～……\x01",
            "还是不能接受？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1019F那、那还用说！\x02\x03",

            "#1005F你……\x01",
            "到底是什么人！？\x02\x03",

            "知道我们的活动\x01",
            "和『结社』的事……\x02\x03",

            "真的只是个单纯的神父而已！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x109,
        (
            "#1060F#5P真真正正，七耀教会的神父哟。\x02\x03",

            "不过确实……\x01",
            "暂时知道我不只是个单纯的神父就行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        "#1009F那这是怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x109,
        (
            "#1065F#5P这个稍后再解释吧。\x02\x03",

            "#1063F刚才也说过\x01",
            "现在应该赶紧回协会才是。\x02\x03",

            "说不定发生了\x01",
            "不得了的大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        (
            "#1020F不得了的大事……\x02\x03",

            "#1007F啊啊受不了……脑子\x01",
            "现在一片混乱了！\x02\x03",

            "#1027F为什么……\x02\x03",

            "为什么本该能见到约修亚的，\x01",
            "却变成这样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x109,
        (
            "#1063F#5P这是你那男朋友\x01",
            "留下的信……\x02\x03",

            "那个，真的是你男朋友写的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1004F啊……？\x02\x03",

            "#1026F唔，嗯。\x01",
            "从转交信的孩子的描述看来\x01",
            "只可能是约修亚……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x109,
        (
            "#1063F#5P那孩子应该不\x01",
            "认识你男朋友吧？\x02\x03",

            "这样的话，别人故意准备\x01",
            "一个特征相似的人来也是可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1026F但、但是……\x01",
            "这很像约修亚的字……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x109,
        (
            "#1065F#5P笔迹这种东西\x01",
            "某种程度是能模仿的。\x02\x03",

            "要骗骗动摇中的人\x01",
            "是很简单的。\x02\x03",

            "#1063F请看看我从大圣堂\x01",
            "收到的信。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #262
        "\x07\x05凯文神父从怀中取出一封信。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240097, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(380, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #263
        "\x07\x00#1020F啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #264
        0x109,
        (
            "#1060F#5P嘿嘿，看来\x01",
            "好像是同样的信封呢。\x02\x03",

            "信的内容里说\x01",
            "能提供我正在\x01",
            "调查的事情的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#1020F这么说来……\x01",
            "是同一人干的？\x02\x03",

            "到底是谁，为什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x109,
        (
            "#1067F#5P这我也不清楚。\x02\x03",

            "#1068F能确定的……\x01",
            "就是我们都被算计了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1020F……………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 5)
    OP_0D()
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #268
        0x101,
        "#1022F……别开……玩笑了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x109,
        "#1064F#5P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1022F虽然不知道是什么人，\x01",
            "但别开玩笑了……\x02\x03",

            "装作约修亚\x01",
            "把我叫出来？\x02\x03",

            "#1027F不能原谅……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #271
        0x101,
        "#1023F#3S绝对不能原谅！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #272
        0x109,
        (
            "#1070F#5P呼啊……\x01",
            "冷静点，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #273
        0x109,
        (
            "#1065F#5P在这里生气，\x01",
            "简直是正中对方下怀。\x02\x03",

            "#1060F总之先回协会\x01",
            "整理情报吧？\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #274
        0x101,
        (
            "#1007F明白了……\x02\x03",

            "#1019F但是凯文先生……\x01",
            "我还是不能完全相信你。\x02\x03",

            "如果骗我……\x01",
            "就真的会打飞你哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x109,
        (
            "#1062F#5P啊啊，没关系。\x02\x03",

            "被艾丝蒂尔\x01",
            "打飞也是我的宿愿。\x02\x03",

            "#1061F为了喜欢的女孩，\x01",
            "我可是做好了粉身碎骨的准备⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1013F说、说什么呢。\x02\x03",

            "#1007F真是的……\x01",
            "真会得意忘形。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x109,
        (
            "#1061F#5P治愈系是我的目标嘛。\x02\x03",

            "#1060F那么艾丝蒂尔。\x01",
            "赶快返回协会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        "#1002F嗯，知道了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1638)
    OP_28(0x8D, 0x1, 0x4)
    OP_28(0x8D, 0x1, 0x8)
    OP_28(0x8D, 0x1, 0x10)
    OP_28(0x8D, 0x1, 0x20)
    OP_28(0x8D, 0x4, 0x10)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0x10)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_3065 end

    def Function_19_3970(): pass

    label("Function_19_3970")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -15020, 4000, 36500, 0)

    def lambda_3997():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3997)
    OP_8E(0xFE, 0xFFFFC554, 0xFA0, 0x9BFA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAE66, 0xFA0, 0x9BFA, 0x7D0, 0x0)
    Return()

    # Function_19_3970 end

    def Function_20_39CC(): pass

    label("Function_20_39CC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -15020, 4000, 36500, 0)

    def lambda_39F3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39F3)
    OP_8E(0xFE, 0xFFFFC554, 0xFA0, 0x9BFA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFB794, 0xFA0, 0x9BFA, 0x9C4, 0x0)
    Return()

    # Function_20_39CC end

    def Function_21_3A28(): pass

    label("Function_21_3A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3CB9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A9E")

    ChrTalk(    #279
        0x108,
        (
            "#070F虽说徒步行走是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去柏斯的话，\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0E")

    label("loc_3A9E")


    ChrTalk(    #280
        0x108,
        (
            "#070F这里是洛连特地区吧。\x02\x03",

            "虽说徒步行走是修行，\x01",
            "但那样太浪费时间。\x02\x03",

            "要去柏斯的话，\x01",
            "还是用定期船比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_3B0E")

    Jump("loc_3C9B")

    label("loc_3B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3BDD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2E")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3B35")

    label("loc_3B2E")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3B91")

    ChrTalk(    #281
        0x106,
        (
            "#053F……要走过去\x01",
            "说实话太浪费时间。\x02\x03",

            "#050F要去柏斯，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BDA")

    label("loc_3B91")


    ChrTalk(    #282
        0x106,
        (
            "#050F这里是洛连特地区吧。\x02\x03",

            "要去柏斯的话，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3BDA")

    Jump("loc_3C9B")

    label("loc_3BDD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BF3")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3BFA")

    label("loc_3BF3")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3C56")

    ChrTalk(    #283
        0x103,
        (
            "#026F……要走过去\x01",
            "说实话是浪费时间。\x02\x03",

            "#020F要去柏斯，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C9B")

    label("loc_3C56")


    ChrTalk(    #284
        0x103,
        (
            "#020F这里是洛连特地区吧。\x02\x03",

            "要去柏斯，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3C9B")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3F19")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_3D53")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D04")

    ChrTalk(    #285
        0x101,
        (
            "#1002F没时间闲逛了。\x01",
            "……要赶快返回协会才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D35")

    label("loc_3D04")


    ChrTalk(    #286
        0x109,
        (
            "#1063F没时间闲逛了。\x01",
            "……赶紧去王都协会吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D35")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3F19")

    label("loc_3D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_END)), "loc_3DBA")
    EventBegin(0x1)

    ChrTalk(    #287
        0x101,
        (
            "#1003F（……我真是的，要去哪里啊。\x01",
            "  约修亚在长城上面哦？)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_3F19")

    label("loc_3DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3F19")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1E")

    ChrTalk(    #288
        0x108,
        (
            "#070F噢，这前面是洛连特地区吧。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFE")

    label("loc_3E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E8F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3B")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3E42")

    label("loc_3E3B")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3E42")


    ChrTalk(    #289
        0x106,
        (
            "#050F这里是洛连特地区吧。\x02\x03",

            "没时间去别的地方了。\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EFE")

    label("loc_3E8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA5")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_3EAC")

    label("loc_3EA5")

    TurnDirection(0x103, 0x0, 400)

    label("loc_3EAC")


    ChrTalk(    #290
        0x103,
        (
            "#020F这里出去就是洛连特地区吧。\x02\x03",

            "没时间去其它的地方了，\x01",
            "现在还是乖乖回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EFE")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3F19")

    Return()

    # Function_21_3A28 end

    def Function_22_3F1A(): pass

    label("Function_22_3F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_411F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3F8E")

    ChrTalk(    #291
        0x108,
        (
            "#070F……通过这里好像\x01",
            "是往柏斯的方向啊。\x02\x03",

            "要离开洛连特，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4002")

    label("loc_3F8E")


    ChrTalk(    #292
        0x108,
        (
            "#070F这边是格兰赛尔地区吧。\x02\x03",

            "……通过这里到底是\x01",
            "是不是往柏斯方向啊。\x02\x03",

            "要离开洛连特，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_4002")

    Jump("loc_4101")

    label("loc_4005")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4022")

    label("loc_401B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4089")

    ChrTalk(    #293
        0x103,
        (
            "#020F……通过这里的话，\x01",
            "那就没有去柏斯的时间啊。\x02\x03",

            "要离开洛连特，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4101")

    label("loc_4089")


    ChrTalk(    #294
        0x103,
        (
            "#020F这边是格兰赛尔地区吧。\x02\x03",

            "……通过这里的话，\x01",
            "那就没有去柏斯的时间啊。\x02\x03",

            "要离开洛连特，\x01",
            "还是去定期船飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4101")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4456")

    label("loc_411F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_4212")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4183")

    ChrTalk(    #295
        0x108,
        (
            "#070F噢，这边是格兰赛尔地区吧。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41F4")

    label("loc_4183")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4199")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_41A0")

    label("loc_4199")

    TurnDirection(0x103, 0x0, 400)

    label("loc_41A0")


    ChrTalk(    #296
        0x103,
        (
            "#022F这前面是格兰赛尔地区哦。\x02\x03",

            "……没空绕道去王都了。\x01",
            "赶紧去东边的神秘森林吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F4")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4456")

    label("loc_4212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_4378")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4231")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_4238")

    label("loc_4231")

    TurnDirection(0x103, 0x0, 400)

    label("loc_4238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4288")

    ChrTalk(    #297
        0x103,
        (
            "#022F这前面是格兰赛尔地区哦。\x02\x03",

            "绕道就算了吧，\x01",
            "赶紧去帕赛尔农场。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_435A")

    label("loc_4288")


    ChrTalk(    #298
        0x103,
        (
            "#022F这前面是格兰赛尔地区哦。\x02\x03",

            "绕道就算了吧，\x01",
            "赶紧去帕赛尔农场。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42FE")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #299
        0x101,
        "#1002F啊，嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_42FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4329")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #300
        0x105,
        "#042F是，对啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4329")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435A")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #301
        0x107,
        "#062F是、是，明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_435A")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_4456")

    label("loc_4378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4456")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43DC")

    ChrTalk(    #302
        0x108,
        (
            "#070F噢，这边是格兰赛尔地区吧。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443B")

    label("loc_43DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F2")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_43F9")

    label("loc_43F2")

    TurnDirection(0x103, 0x0, 400)

    label("loc_43F9")


    ChrTalk(    #303
        0x103,
        (
            "#020F穿过这里就是格兰赛尔地区了。\x02\x03",

            "没空绕道了。\x01",
            "赶快回头吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443B")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_4456")

    Return()

    # Function_22_3F1A end

    def Function_23_4457(): pass

    label("Function_23_4457")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_23_4457 end

    SaveToFile()

Try(main)
