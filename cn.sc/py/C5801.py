from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5801   ._SN',
        MapName             = 'Other',
        Location            = 'C5801.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '莱奥尔刚依吉',                         # 9
        '哨兵红',                               # 10
        '哨兵红',                               # 11
        '哨兵蓝',                               # 12
        '哨兵蓝',                               # 13
        '多伦',                                 # 14
        '空贼蒂诺',                             # 15
        '空贼罗尔',                             # 16
        '目标角色',                             # 17
        '居住区域『克雷德尔』１',               # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
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
        'ED6_DT29/CH12310 ._CH',             # 00
        'ED6_DT29/CH12311 ._CH',             # 01
        'ED6_DT29/CH12060 ._CH',             # 02
        'ED6_DT29/CH12061 ._CH',             # 03
        'ED6_DT29/CH12190 ._CH',             # 04
        'ED6_DT29/CH12191 ._CH',             # 05
        'ED6_DT29/CH12970 ._CH',             # 06
        'ED6_DT29/CH12971 ._CH',             # 07
        'ED6_DT27/CH03760 ._CH',             # 08
        'ED6_DT07/CH01380 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12310P._CP',             # 00
        'ED6_DT29/CH12311P._CP',             # 01
        'ED6_DT29/CH12060P._CP',             # 02
        'ED6_DT29/CH12061P._CP',             # 03
        'ED6_DT29/CH12190P._CP',             # 04
        'ED6_DT29/CH12191P._CP',             # 05
        'ED6_DT29/CH12970P._CP',             # 06
        'ED6_DT29/CH12971P._CP',             # 07
        'ED6_DT27/CH03760P._CP',             # 08
        'ED6_DT07/CH01380P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47010,
        Z                   = 0,
        Y                   = -69580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -48100,
        Z                   = 0,
        Y                   = -71060,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -49550,
        Z                   = 3400,
        Y                   = -69030,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -137160,
        Z                   = 0,
        Y                   = -63670,
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
        X                   = -99450,
        Z                   = 0,
        Y                   = -40530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -95800,
        Z                   = 0,
        Y                   = -68900,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -69300,
        Z                   = 0,
        Y                   = -39890,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -57180,
        Z                   = 0,
        Y                   = -118140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -112940,
        Z                   = 0,
        Y                   = -110020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x50C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -102000,
        Y                   = 2000,
        Z                   = -105000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -47500,
        Y                   = 4000,
        Z                   = -65140,
        Range               = -45500,
        Unknown_10          = 0x1770,
        Unknown_14          = 0xFFFF0574,
        Unknown_18          = 0x0,
        Unknown_1C          = 20,
    )


    DeclActor(
        TriggerX            = -100970,
        TriggerZ            = -7920,
        TriggerY            = -119660,
        TriggerRange        = 800,
        ActorX              = -100500,
        ActorZ              = -6520,
        ActorY              = -119000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_401",          # 01, 1
        "Function_2_57B",          # 02, 2
        "Function_3_B83",          # 03, 3
        "Function_4_FD4",          # 04, 4
        "Function_5_1276",         # 05, 5
        "Function_6_127F",         # 06, 6
        "Function_7_1FD0",         # 07, 7
        "Function_8_2859",         # 08, 8
        "Function_9_2914",         # 09, 9
        "Function_10_29BF",        # 0A, 10
        "Function_11_2A78",        # 0B, 11
        "Function_12_2B23",        # 0C, 12
        "Function_13_2BCE",        # 0D, 13
        "Function_14_3168",        # 0E, 14
        "Function_15_3277",        # 0F, 15
        "Function_16_330A",        # 10, 16
        "Function_17_3340",        # 11, 17
        "Function_18_341C",        # 12, 18
        "Function_19_352C",        # 13, 19
        "Function_20_36C3",        # 14, 20
        "Function_21_36DA",        # 15, 21
        "Function_22_3761",        # 16, 22
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_376")
    SetChrPos(0xD, -48740, 3410, -69080, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xE, -46920, 0, -70650, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xF, -47070, 0, -68910, 90)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_391")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_391")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3A7")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_400")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3B8")
    OP_A3(0x10F1)
    Event(0, 19)
    Jump("loc_400")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_3CE")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_400")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_3DF")
    OP_A3(0x10F3)
    Event(0, 13)
    Jump("loc_400")

    label("loc_3DF")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3EB"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_400")

    Return()

    # Function_0_32A end

    def Function_1_401(): pass

    label("Function_1_401")

    OP_16(0x2, 0xFA0, 0xFFFCC3E0, 0xFFFCCF98, 0x230078)
    OP_22(0x1C7, 0x0, 0x64)
    OP_51(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x2, 0x0)
    OP_72(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 4)), scpexpr(EXPR_END)), "loc_446")
    OP_71(0x4, 0x10)
    OP_64(0x0, 0x1)
    OP_71(0x8, 0x4)

    label("loc_446")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x50E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57A")
    OP_D2(0x270110, 0x270120, 0x12)
    OP_D2(0x270130, 0x270140, 0x13)
    OP_D2(0x702B6, 0x702BD, 0x14)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_495"),
        (5, "loc_4A2"),
        (3, "loc_4AF"),
        (4, "loc_4BC"),
        (6, "loc_4C9"),
        (7, "loc_4D6"),
        (8, "loc_4E3"),
        (SWITCH_DEFAULT, "loc_4F0"),
    )


    label("loc_495")

    OP_D2(0x701D0, 0x701DC, 0x15)
    Jump("loc_4F0")

    label("loc_4A2")

    OP_D2(0x70218, 0x70224, 0x15)
    Jump("loc_4F0")

    label("loc_4AF")

    OP_D2(0x701E8, 0x701F4, 0x15)
    Jump("loc_4F0")

    label("loc_4BC")

    OP_D2(0x27036E, 0x27037B, 0x15)
    Jump("loc_4F0")

    label("loc_4C9")

    OP_D2(0x70230, 0x7023C, 0x15)
    Jump("loc_4F0")

    label("loc_4D6")

    OP_D2(0x70248, 0x70254, 0x15)
    Jump("loc_4F0")

    label("loc_4E3")

    OP_D2(0x270176, 0x270183, 0x15)
    Jump("loc_4F0")

    label("loc_4F0")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_515"),
        (5, "loc_522"),
        (3, "loc_52F"),
        (4, "loc_53C"),
        (6, "loc_549"),
        (7, "loc_556"),
        (8, "loc_563"),
        (SWITCH_DEFAULT, "loc_570"),
    )


    label("loc_515")

    OP_D2(0x701D0, 0x701DC, 0x16)
    Jump("loc_570")

    label("loc_522")

    OP_D2(0x70218, 0x70224, 0x16)
    Jump("loc_570")

    label("loc_52F")

    OP_D2(0x701E8, 0x701F4, 0x16)
    Jump("loc_570")

    label("loc_53C")

    OP_D2(0x27036E, 0x27037B, 0x16)
    Jump("loc_570")

    label("loc_549")

    OP_D2(0x70230, 0x7023C, 0x16)
    Jump("loc_570")

    label("loc_556")

    OP_D2(0x70248, 0x70254, 0x16)
    Jump("loc_570")

    label("loc_563")

    OP_D2(0x270176, 0x270183, 0x16)
    Jump("loc_570")

    label("loc_570")

    OP_D2(0x260187, 0x26018C, 0x17)

    label("loc_57A")

    Return()

    # Function_1_401 end

    def Function_2_57B(): pass

    label("Function_2_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_590")
    SetChrFlags(0xD, 0x10)

    label("loc_590")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_77B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E9")
    TurnDirection(0xD, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")

    ChrTalk(    #0
        0xD,
        (
            "#490F哦，是乔丝特啊。\x02\x03",

            "现在要开始\x01",
            "修复翼端了。\x02\x03",

            "我正在鼓舞这些\x01",
            "小子们的士气哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#210F修理工作看来很顺利呢。\x02\x03",

            "希望『山猫号』也能\x01",
            "早点恢复正常状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xD,
        (
            "#490F交给我们吧。\x02\x03",

            "等你回来的时候，\x01",
            "它就像新的一样了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CB)
    Jump("loc_6DF")

    label("loc_696")


    ChrTalk(    #3
        0xD,
        (
            "#490F我们也会\x01",
            "拚命进行修理的。\x02\x03",

            "等你回来的时候，\x01",
            "它就像新的一样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DF")

    OP_8C(0xD, 90, 0)
    Jump("loc_778")

    label("loc_6E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751")

    ChrTalk(    #4
        0xD,
        (
            "#196F喂，你们几个！\x01",
            "再加把劲啊！\x02\x03",

            "老是这副模样的话，\x01",
            "能举起的东西都抬不起来了！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_A2(0x0)
    Jump("loc_778")

    label("loc_751")


    ChrTalk(    #5
        0xD,
        (
            "#196F好，再来一次！\x01",
            "加把劲！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_778")

    Jump("loc_B7F")

    label("loc_77B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_B7F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97F")
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #6
        0xD,
        (
            "#490F哦，乔丝特。\x02\x03",

            "怎么样？\x01",
            "还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10B,
        (
            "#210F我没问题。\x02\x03",

            "不过，修理的情况如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#197F现在勉强让它飞的话\x01",
            "还是能飞的……\x02\x03",

            "但是因为内部结构受了损伤，\x01",
            "完全无法进行长距离的飞行。\x02\x03",

            "如果不解决这个问题，\x01",
            "就算逃出去也无法支撑到降落。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10B,
        (
            "#212F这样啊……\x02\x03",

            "#210F要是有什么需要的东西\x01",
            "就尽管跟我说吧。\x02\x03",

            "我会从『埃尔赛尤』那边\x01",
            "偷偷拿过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "#191F哈哈，全靠你了。\x02\x03",

            "#490F那么回头见，乔丝特。\x02\x03",

            "遇到麻烦的话\x01",
            "一定要马上叫我们啊。\x02\x03",

            "不管在什么地方，\x01",
            "我们都会赶过去的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x2297)
    Jump("loc_A79")

    label("loc_97F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9E5")
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #11
        0xD,
        (
            "#490F回头见，乔丝特。\x01",
            "好好加油哦。\x02\x03",

            "遇到麻烦时记得叫我们。\x01",
            "我们会马上赶过去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_9E5")


    ChrTalk(    #12
        0xD,
        (
            "#197F现在勉强让它飞的话\x01",
            "还是能飞的……\x02\x03",

            "但是因为内部结构受了损伤，\x01",
            "完全无法进行长距离的飞行。\x02\x03",

            "在修好那个部分之前，\x01",
            "根本不可能离开这个地方的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A79")

    Jump("loc_B7F")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1E")

    ChrTalk(    #13
        0xD,
        (
            "#197F现在勉强让它飞的话\x01",
            "还是能飞的……\x02\x03",

            "但是因为内部结构受了损伤，\x01",
            "完全无法进行长距离的飞行。\x02\x03",

            "在修好那个部分之前，\x01",
            "根本不可能离开这个地方的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_B7F")

    label("loc_B1E")


    ChrTalk(    #14
        0xD,
        (
            "#190F我负责修理船体，\x01",
            "结构方面都交给吉尔处理了。\x02\x03",

            "那家伙的脑袋很灵光，\x01",
            "适合做这种细部工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7F")

    TalkEnd(0xFE)
    Return()

    # Function_2_57B end

    def Function_3_B83(): pass

    label("Function_3_B83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_D84")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9D")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(    #15
        0xFE,
        "啊，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "现、现在要开始\x01",
            "修理这条脚架……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "虽、虽然我们两个人\x01",
            "要把它抬起来\x01",
            "好像非常困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "不、不过为了小姐，\x01",
            "我们会努力完成的！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_C9A")

    label("loc_C48")


    ChrTalk(    #19
        0xFE,
        (
            "现、现在要开始\x01",
            "修理这条脚架……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然很困难，\x01",
            "不过我们会为了小姐努力的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9A")

    Jump("loc_D81")

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(    #21
        0xFE,
        (
            "现、现在要开始\x01",
            "修理这条脚架……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "虽、虽然我们两个人\x01",
            "要把它抬起来\x01",
            "好像非常困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "可恶，至少多伦老大\x01",
            "也来帮忙一下啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_D81")

    label("loc_D2F")


    ChrTalk(    #24
        0xFE,
        (
            "现、现在要把\x01",
            "这条脚架抬起来吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "大、大哥他们至少\x01",
            "能不能来帮忙一下啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D81")

    Jump("loc_FD0")

    label("loc_D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_FD0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF5")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E96")

    ChrTalk(    #26
        0xE,
        (
            "啊，小姐……\x01",
            "回来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10B,
        (
            "#210F我来看看情况的。\x02\x03",

            "飞船的状态怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        (
            "脚架虽然断了，\x01",
            "不过其它部分几乎没受到损伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xE,
        (
            "就看内部结构的状况如何了，\x01",
            "但似乎很快就能修好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10B,
        (
            "#210F是吗……\x01",
            "嗯，好好加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        "是、是！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22CC)
    Jump("loc_EF2")

    label("loc_E96")


    ChrTalk(    #32
        0xE,
        (
            "就看内部结构的状况如何了，\x01",
            "但似乎很快就能修好了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xE,
        (
            "为了小姐，\x01",
            "我们会拚命努力的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF2")

    Jump("loc_FD0")

    label("loc_EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7C")

    ChrTalk(    #34
        0xE,
        (
            "哦，你们几个……\x01",
            "谢谢你们救了我们大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "目前这里也正在\x01",
            "卯足全力修理飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        (
            "我们可不想\x01",
            "孤零零地被抛在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_FD0")

    label("loc_F7C")


    ChrTalk(    #37
        0xE,
        (
            "目前这里也正在\x01",
            "卯足全力修理飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        (
            "不过要如何修理内部结构\x01",
            "还是一个大问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD0")

    TalkEnd(0xFE)
    Return()

    # Function_3_B83 end

    def Function_4_FD4(): pass

    label("Function_4_FD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_119C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10FE")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AF")

    ChrTalk(    #39
        0xF,
        (
            "要把这个抬起来，\x01",
            "根本就是不可能的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xF,
        (
            "小姐请你帮忙\x01",
            "向老大求情吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10B,
        (
            "#212F我可不想听\x01",
            "这些丧气话。\x02\x03",

            "你们是男人吧？\x01",
            "让我看看你们的毅力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xF,
        (
            "小、小姐……\x01",
            "不会吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_10FB")

    label("loc_10AF")


    ChrTalk(    #43
        0xF,
        (
            "要把这个抬起来，\x01",
            "根本就是不可能的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "小姐请你帮忙\x01",
            "向老大求情吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FB")

    Jump("loc_1199")

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115A")

    ChrTalk(    #45
        0xF,
        (
            "要把这种东西抬起来，\x01",
            "根本就是不可能的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xF,
        (
            "唉，多伦老大\x01",
            "也真是乱来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1199")

    label("loc_115A")


    ChrTalk(    #47
        0xF,
        (
            "要把这个抬起来，\x01",
            "根本就不可能啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xF,
        "大哥也真是乱来。\x02",
    )

    CloseMessageWindow()

    label("loc_1199")

    Jump("loc_1272")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122C")

    ChrTalk(    #49
        0xF,
        (
            "唉唉～真的\x01",
            "硬生生断掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "一般情况下断得彻底些\x01",
            "还比较容易修理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "不过这种程度的话，\x01",
            "还真要想想该怎么修了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1272")

    label("loc_122C")


    ChrTalk(    #52
        0xF,
        (
            "唔～这个翼端\x01",
            "要怎么修理呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        (
            "得先和多伦老大\x01",
            "商量一下才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")

    TalkEnd(0xFE)
    Return()

    # Function_4_FD4 end

    def Function_5_1276(): pass

    label("Function_5_1276")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_1276 end

    def Function_6_127F(): pass

    label("Function_6_127F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1296")
    Call(0, 21)
    Call(0, 22)

    label("loc_1296")

    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_12E3"),
        (5, "loc_12FA"),
        (3, "loc_1311"),
        (4, "loc_1328"),
        (6, "loc_133F"),
        (7, "loc_1356"),
        (8, "loc_136D"),
        (SWITCH_DEFAULT, "loc_1384"),
    )


    label("loc_12E3")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_1384")

    label("loc_12FA")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_1384")

    label("loc_1311")

    OP_D2(0x701E8, 0x701F4, 0xE)
    OP_D2(0x701E9, 0x701F5, 0xF)
    Jump("loc_1384")

    label("loc_1328")

    OP_D2(0x27036E, 0x27037B, 0xE)
    OP_D2(0x27036F, 0x27037C, 0xF)
    Jump("loc_1384")

    label("loc_133F")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_1384")

    label("loc_1356")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_1384")

    label("loc_136D")

    OP_D2(0x270176, 0x270183, 0xE)
    OP_D2(0x270177, 0x270184, 0xF)
    Jump("loc_1384")

    label("loc_1384")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_13A9"),
        (5, "loc_13C0"),
        (3, "loc_13D7"),
        (4, "loc_13EE"),
        (6, "loc_1405"),
        (7, "loc_141C"),
        (8, "loc_1433"),
        (SWITCH_DEFAULT, "loc_144A"),
    )


    label("loc_13A9")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_144A")

    label("loc_13C0")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_144A")

    label("loc_13D7")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_144A")

    label("loc_13EE")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_144A")

    label("loc_1405")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_144A")

    label("loc_141C")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_144A")

    label("loc_1433")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_144A")

    label("loc_144A")

    OP_D2(0x702B5, 0x702BC, 0x12)
    OP_D2(0x702B6, 0x702BD, 0x13)
    OP_D2(0x702B8, 0x702BF, 0x14)
    OP_D2(0x2700A0, 0x2700A4, 0x15)
    OP_D2(0x702B7, 0x702BE, 0x16)
    OP_D2(0x290160, 0x290164, 0x17)
    OP_D2(0x290161, 0x290165, 0x18)
    OP_D2(0x290168, 0x290169, 0x19)
    OP_D2(0x290160, 0x290164, 0x1A)
    OP_D2(0x290161, 0x290165, 0x1B)
    OP_D2(0x290168, 0x290169, 0x1C)
    OP_D2(0x29013A, 0x29013E, 0x1D)
    AddParty(0x45, 0xFA, 0xFF)
    OP_6D(-120860, 0, -62110, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(299000, 0)
    OP_6E(309, 0)
    SetChrPos(0x101, -119030, 0, -63460, 90)
    SetChrPos(0x102, -119050, 0, -62270, 90)
    SetChrPos(0xF8, -120560, 0, -63510, 90)
    SetChrPos(0xF9, -120770, 0, -62110, 90)
    SetChrPos(0x146, -59210, 0, -63960, 270)
    SetChrPos(0x10, -59210, 0, -63960, 270)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, -72000, 1000, -62940, 90)
    SetChrPos(0x9, -66760, 0, -59620, 135)
    SetChrPos(0xA, -68280, 0, -62740, 90)
    SetChrPos(0xB, -68300, 0, -64590, 90)
    SetChrPos(0xC, -66590, 0, -67870, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x9, 23)
    SetChrChipByIndex(0xA, 23)
    SetChrChipByIndex(0xB, 26)
    SetChrChipByIndex(0xC, 26)

    def lambda_15F6():

        label("loc_15F6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_15F6")

    QueueWorkItem2(0x8, 3, lambda_15F6)

    def lambda_1609():

        label("loc_1609")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1609")

    QueueWorkItem2(0x9, 3, lambda_1609)

    def lambda_161C():

        label("loc_161C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_161C")

    QueueWorkItem2(0xA, 3, lambda_161C)

    def lambda_162F():

        label("loc_162F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_162F")

    QueueWorkItem2(0xB, 3, lambda_162F)

    def lambda_1642():

        label("loc_1642")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1642")

    QueueWorkItem2(0xC, 3, lambda_1642)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 19)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_20(0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DB")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1719")

    label("loc_16DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1702")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1719")

    label("loc_1702")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1719")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1745")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1783")

    label("loc_1745")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1783")

    label("loc_176C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1783")

    Sleep(1000)

    ChrTalk(    #54
        0x101,
        "#1004F#5P约修亚，看那个……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1044F#5P……嗯。\x01",
            "怎么会出现在这里……\x02\x03",

            "#1042F！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x29)
    Sleep(500)

    def lambda_17F5():
        OP_6D(-64629, 0, -63910, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17F5)

    def lambda_180D():
        OP_67(0, 6510, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_180D)

    def lambda_1825():
        OP_6B(4510, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1825)

    def lambda_1835():
        OP_6C(296000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1835)
    OP_6E(453, 7000)
    Sleep(500)
    Fade(500)
    OP_6D(-64629, 0, -62690, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(307000, 0)
    OP_6E(333, 0)
    OP_0D()

    def lambda_1896():
        OP_8E(0xFE, 0xFFFF0A74, 0x0, 0xFFFF0C22, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1896)
    Sleep(50)

    def lambda_18B6():
        OP_8E(0xFE, 0xFFFF09F2, 0x0, 0xFFFEFF16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_18B6)
    Sleep(50)

    def lambda_18D6():
        OP_8E(0xFE, 0xFFFF08BC, 0x0, 0xFFFF074A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_18D6)
    Sleep(50)

    def lambda_18F6():
        OP_8E(0xFE, 0xFFFF09CA, 0x0, 0xFFFF02C2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_18F6)
    Sleep(50)
    OP_43(0x146, 0x0, 0x0, 0x8)
    WaitChrThread(0x146, 0x0)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0xA, 0x0)
    WaitChrThread(0xB, 0x0)
    WaitChrThread(0xC, 0x0)
    Sleep(500)

    ChrTalk(    #56
        0x146,
        (
            "#214F别、别过来！\x02\x03",

            "如果再继续伤害『山猫号』的话，\x01",
            "我是绝对不会放过你们的！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_198B():
        OP_6D(-67470, 0, -61640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_198B)

    def lambda_19A3():
        OP_67(0, 4130, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A3)

    def lambda_19BB():
        OP_6B(2890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19BB)
    OP_8F(0x8, 0xFFFEF228, 0x3E8, 0xFFFF0876, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    SetChrChipByIndex(0x8, 29)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    LoadEffect(0x1, "monster\\\\msc0331.eff")
    LoadEffect(0x2, "battle\\\\btbomb00.eff")
    PlayEffect(0x1, 0x0, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x10, -1000, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0xFF, -59210, 0, -63960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 22)

    def lambda_1AA9():
        OP_96(0xFE, 0xFFFF2798, 0x0, 0xFFFF07D6, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1AA9)
    OP_7C(0x190, 0x190, 0xBB8, 0x1F4)
    Fade(500)
    OP_6D(-54060, 0, -63310, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(67000, 0)
    OP_6E(401, 0)
    SetChrChipByIndex(0x8, 0)
    WaitChrThread(0x146, 0x1)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 20)

    def lambda_1B2E():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1B2E)

    ChrTalk(    #57
        0x146,
        "#216F#5P啊呜……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x146, 0x1)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1B69():
        OP_6D(-58360, 0, -63110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B69)

    def lambda_1B81():
        OP_8E(0xFE, 0xFFFF1604, 0x0, 0xFFFF10DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B81)
    Sleep(100)

    def lambda_1BA1():
        OP_8E(0xFE, 0xFFFF12E4, 0x0, 0xFFFF0A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BA1)
    Sleep(150)

    def lambda_1BC1():
        OP_8E(0xFE, 0xFFFF12C6, 0x0, 0xFFFF04C1, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1BC1)
    Sleep(140)

    def lambda_1BE1():
        OP_8E(0xFE, 0xFFFF15B4, 0x0, 0xFFFEFF20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BE1)
    Sleep(800)

    def lambda_1C01():
        OP_8E(0xFE, 0xFFFF027C, 0x3E8, 0xFFFF066E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C01)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x8, 0x1)
    SetMapFlags(0x10)

    ChrTalk(    #58
        0x146,
        (
            "#413F呜呜……\x01",
            "吉尔哥……多伦哥……\x02\x03",

            "#215F………约修亚…………\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -77950, 0, -65650, 90)

    NpcTalk(    #59
        0x101,
        "女孩的声音",
        "哼哼，看来你遇到麻烦了呢。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrPos(0x101, -72190, 0, -64099, 90)
    SetChrPos(0x102, -72080, 0, -62770, 90)
    SetChrPos(0xF8, -73710, 0, -64580, 90)
    SetChrPos(0xF9, -73670, 0, -62730, 90)
    OP_62(0x146, 0xFFFFFF38, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x146, 2)
    Sleep(500)

    def lambda_1D28():
        OP_6D(-66700, 0, -62400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D28)

    def lambda_1D40():
        OP_67(0, 5450, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D40)

    def lambda_1D58():
        OP_6B(2390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D58)

    def lambda_1D68():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D68)

    def lambda_1D78():
        OP_6E(417, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D78)

    def lambda_1D88():
        OP_8C(0xFE, 270, 200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D88)
    Sleep(100)

    def lambda_1D9B():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D9B)

    def lambda_1DA9():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1DA9)
    Sleep(100)

    def lambda_1DBC():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1DBC)

    def lambda_1DCA():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DCA)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #60
        0x146,
        (
            "#213F#6P是无脑女！？\x01",
            "……还、还有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1019F#5P我～说～啊，\x01",
            "你说谁是无脑女啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#1046F#5P有话待会儿再说！\x01",
            "先解决掉它们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x146,
        "#414F#6P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1007F#5P真受不了……烦人的家伙。\x02",
    )

    CloseMessageWindow()
    OP_99(0x146, 0x2, 0x0, 0x3E8)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 19)
    SetChrSubChip(0x146, 0)
    OP_0D()
    Sleep(500)

    def lambda_1ECB():
        OP_6D(-62330, 0, -62850, 450)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1ECB)

    def lambda_1EE3():
        OP_67(0, 6930, -10000, 450)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EE3)

    def lambda_1EFB():
        OP_6B(2000, 450)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1EFB)

    def lambda_1F0B():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F0B)
    Sleep(30)

    def lambda_1F2B():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F2B)

    def lambda_1F46():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1F46)
    Sleep(30)

    def lambda_1F66():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1F66)
    Sleep(80)
    SetChrChipByIndex(0x146, 18)
    SetChrFlags(0x146, 0x1000)

    def lambda_1F90():
        OP_91(0xFE, 0xFFFFF060, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_1F90)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x146, 0xFF)
    OP_B6(0x45, 0x1)
    Battle(0x50E, 0x300019, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_127F end

    def Function_7_1FD0(): pass

    label("Function_7_1FD0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    OP_44(0x146, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_6D(-63860, 0, -65590, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(225000, 0)
    OP_6E(382, 0)
    SetChrChipByIndex(0x101, 18)
    SetChrChipByIndex(0x102, 19)
    SetChrChipByIndex(0x146, 20)
    SetChrChipByIndex(0xF8, 21)
    SetChrChipByIndex(0xF9, 22)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x146, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, -66370, 0, -65450, 90)
    SetChrPos(0x102, -66310, 0, -64010, 90)
    SetChrPos(0xF8, -67990, 0, -65870, 90)
    SetChrPos(0xF9, -67870, 0, -64340, 90)
    SetChrPos(0x146, -58480, 0, -64450, 270)

    def lambda_20D3():
        OP_6B(2300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_20D3)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    Sleep(100)
    SetChrChipByIndex(0x146, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #65
        0x101,
        (
            "#1007F#6P呼……\x01",
            "总算摆平了呢。\x02\x03",

            "#1002F那个大家伙\x01",
            "还真难对付……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#1035F#4P那是结社的重型人形兵器，\x01",
            "『据点武装者』。\x02\x03",

            "#1043F一般都是拿来\x01",
            "防卫据点用的……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21C1():
        OP_6D(-61840, 0, -65830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21C1)

    def lambda_21D9():
        OP_8E(0xFE, 0xFFFF0EA2, 0x0, 0xFFFF059D, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_21D9)
    Sleep(100)

    def lambda_21F9():
        OP_8E(0xFE, 0xFFFF0E0C, 0x0, 0xFFFF006A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21F9)
    Sleep(80)

    def lambda_2219():
        OP_8E(0xFE, 0xFFFF07B8, 0x0, 0xFFFEFEB2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2219)
    Sleep(120)

    def lambda_2239():
        OP_8E(0xFE, 0xFFFF08C6, 0x0, 0xFFFF0498, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2239)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #67
        0x102,
        (
            "#1040F#2P总之……\x01",
            "你没事真是太好了。\x02\x03",

            "不过，为什么你们\x01",
            "会在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x146,
        (
            "#215F#6P嗯、嗯……\x02\x03",

            "#413F自从我们和你分开后，\x01",
            "就一直潜伏在国境附近……\x02\x03",

            "不过天空中突然出现了奇怪的东西，\x01",
            "于是我们就飞过去看个究竟，\x01",
            "然后山猫号的导力就停止了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#5P所以就坠落下来了是吧。\x02\x03",

            "#1004F对了，说到这个……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #70
        0x101,
        (
            "#1015F#5P……你那些\x01",
            "哥哥们怎么样了？\x02\x03",

            "#1016F完全没看到他们，\x01",
            "是不是出去了？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x146, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #71
        0x146,
        (
            "#215F#6P…………………\x02\x03",

            "#413F呜呜……呜呜………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #72
        0x101,
        "#1020F#5P哇呀，你、你怎么了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#1035F#2P乔丝特……冷静一点。\x02\x03",

            "#1040F能不能慢慢地\x01",
            "把事情说给我们听？\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x146, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #74
        0x146,
        (
            "#417F#6P呜呜……\x02\x03",

            "#418F约修亚……约修亚～！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2536():

        label("loc_2536")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2536")

    QueueWorkItem2(0x101, 2, lambda_2536)

    def lambda_2547():

        label("loc_2547")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2547")

    QueueWorkItem2(0x102, 2, lambda_2547)

    def lambda_2558():

        label("loc_2558")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2558")

    QueueWorkItem2(0xF8, 2, lambda_2558)

    def lambda_2569():
        TurnDirection(0xFE, 0x146, 0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2569)

    def lambda_2577():
        OP_6D(-62450, 0, -65050, 1500)
        ExitThread()

    QueueWorkItem(0x146, 3, lambda_2577)
    SetChrFlags(0x146, 0x40)

    def lambda_2594():
        OP_8E(0x146, 0xFFFF0FF6, 0x0, 0xFFFF059D, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_2594)
    WaitChrThread(0x146, 0x0)

    def lambda_25B4():

        label("loc_25B4")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_25B4")

    QueueWorkItem2(0x101, 2, lambda_25B4)
    SetChrFlags(0x146, 0x2)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 23)

    def lambda_25D4():
        OP_8F(0xFE, 0xFFFF0DD0, 0x0, 0xFFFF059D, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_25D4)
    WaitChrThread(0x102, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2631")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_266F")

    label("loc_2631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2658")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_266F")

    label("loc_2658")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_266F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269B")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_26D9")

    label("loc_269B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C2")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_26D9")

    label("loc_26C2")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_26D9")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_270E")

    ChrTalk(    #75
        0x105,
        "#1164F………啊…………………\x02",
    )

    CloseMessageWindow()

    label("loc_270E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2735")

    ChrTalk(    #76
        0x107,
        "#065F……啊啊………\x02",
    )

    CloseMessageWindow()

    label("loc_2735")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_275A")

    ChrTalk(    #77
        0x104,
        "#037F哎呀哎呀……\x02",
    )

    CloseMessageWindow()

    label("loc_275A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_277D")

    ChrTalk(    #78
        0x103,
        "#027F哎呀呀……\x02",
    )

    CloseMessageWindow()

    label("loc_277D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279F")

    ChrTalk(    #79
        0x109,
        "#1064F哎哟……\x02",
    )

    CloseMessageWindow()

    label("loc_279F")


    ChrTalk(    #80
        0x101,
        "#1020F#5P什、什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x146,
        (
            "#418F#6P哥、哥哥他们\x01",
            "被结社那些家伙抓走了！\x02\x03",

            "大家为了掩护我逃走，\x01",
            "特意去引诱敌人……\x02\x03",

            "#417F约修亚……\x01",
            "我该……怎么办才好！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1FD0 end

    def Function_8_2859(): pass

    label("Function_8_2859")

    OP_8C(0xFE, 315, 500)

    def lambda_2866():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2866)
    Sleep(300)
    OP_44(0x8, 0x0)
    OP_43(0x9, 0x0, 0x0, 0x9)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 225, 500)

    def lambda_2892():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2892)
    Sleep(300)
    OP_44(0xC, 0x0)
    OP_43(0xC, 0x0, 0x0, 0xC)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 270, 500)

    def lambda_28BE():
        OP_99(0xFE, 0x0, 0x4, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28BE)
    Sleep(200)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0xA)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 270, 500)
    Sleep(200)

    def lambda_28EF():
        OP_99(0xFE, 0x0, 0x6, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28EF)
    OP_44(0xB, 0x0)
    OP_43(0xB, 0x0, 0x0, 0xB)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_2859 end

    def Function_9_2914(): pass

    label("Function_9_2914")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)

    def lambda_2974():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2974)
    OP_8F(0xFE, 0xFFFEFB38, 0x0, 0xFFFF171C, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 23)

    def lambda_29B1():

        label("loc_29B1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_29B1")

    QueueWorkItem2(0xFE, 3, lambda_29B1)
    Return()

    # Function_9_2914 end

    def Function_10_29BF(): pass

    label("Function_10_29BF")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)

    def lambda_2A1F():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2A1F)

    def lambda_2A39():
        OP_8C(0xFE, 135, 0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A39)
    OP_8F(0xFE, 0xFFFEF750, 0x0, 0xFFFF101E, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 23)

    def lambda_2A6A():

        label("loc_2A6A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2A6A")

    QueueWorkItem2(0xFE, 3, lambda_2A6A)
    Return()

    # Function_10_29BF end

    def Function_11_2A78(): pass

    label("Function_11_2A78")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)

    def lambda_2AD8():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2AD8)
    OP_8F(0xFE, 0xFFFEF836, 0x0, 0xFFFEFE3A, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)

    def lambda_2B15():

        label("loc_2B15")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2B15")

    QueueWorkItem2(0xFE, 3, lambda_2B15)
    Return()

    # Function_11_2A78 end

    def Function_12_2B23(): pass

    label("Function_12_2B23")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)

    def lambda_2B83():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2B83)
    OP_8F(0xFE, 0xFFFEFBE2, 0x0, 0xFFFEF6E2, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)

    def lambda_2BC0():

        label("loc_2BC0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2BC0")

    QueueWorkItem2(0xFE, 3, lambda_2BC0)
    Return()

    # Function_12_2B23 end

    def Function_13_2BCE(): pass

    label("Function_13_2BCE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BE5")
    Call(0, 21)
    Call(0, 15)

    label("loc_2BE5")

    OP_6D(-83690, 0, -60600, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -84410, 0, -62530, 0)
    SetChrPos(0x102, -83090, 0, -61240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C76")
    SetChrPos(0xF9, -85770, 0, -61600, 90)
    SetChrPos(0x10B, -84210, 0, -59930, 180)
    Jump("loc_2CCA")

    label("loc_2C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA8")
    SetChrPos(0xF8, -85770, 0, -61600, 90)
    SetChrPos(0x10B, -84210, 0, -59930, 180)
    Jump("loc_2CCA")

    label("loc_2CA8")

    SetChrPos(0xF8, -84210, 0, -59930, 180)
    SetChrPos(0xF9, -85770, 0, -61600, 90)

    label("loc_2CCA")

    OP_31(0xFF, 0xFE, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3066")

    ChrTalk(    #82
        0x101,
        (
            "#1006F那么……\x01",
            "要继续探索吗？\x02\x03",

            "#1004F……对了，乔丝特。\x02\x03",

            "在这附近有没有\x01",
            "通往其它地方的出口？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10B,
        (
            "#413F#5P嗯……\x01",
            "我没有看到呢。\x02\x03",

            "#212F通向隔壁街区的桥梁\x01",
            "也完全崩塌了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1007F唔……这可伤脑筋了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1040F总之先调查一下\x01",
            "街上的情况吧。\x02\x03",

            "或许会发现\x01",
            "什么线索也说不定。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E09():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E09)
    Sleep(50)
    TurnDirection(0x10B, 0x102, 400)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#1019F#6P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10B,
        "#212F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#1048F那个，我……#3810W #20W \x01",
            "#1052F…………对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1001F#6P咦，为什么要道歉？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10B,
        (
            "#211F#5P没线索\x01",
            "又不是你的错。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F18")

    ChrTalk(    #91
        0x107,
        "#067F#6P（真、真可怜……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F51")

    ChrTalk(    #92
        0x106,
        "#551F#6P（看上去是如坐针毡啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8B")

    ChrTalk(    #93
        0x109,
        "#1068F#6P（真挺得住啊，约修亚……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2F8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC2")

    ChrTalk(    #94
        0x108,
        "#070F#6P（真是的，还年轻啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FFF")

    ChrTalk(    #95
        0x103,
        "#027F#6P（呵呵，这也是青春的一面吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_2FFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3033")

    ChrTalk(    #96
        0x105,
        "#1380F#6P（还真是可怜啊……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3063")

    label("loc_3033")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3063")

    ChrTalk(    #97
        0x104,
        "#031F#6P（呵呵～很有意思。）\x02",
    )

    CloseMessageWindow()

    label("loc_3063")

    Jump("loc_315C")

    label("loc_3066")


    ChrTalk(    #98
        0x101,
        (
            "#1006F那么，接下来\x01",
            "要继续探索这个区域吗？\x02\x03",

            "#1015F据乔丝特所说，\x01",
            "好像还没有找到\x01",
            "通往其它地方的出口……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#1035F嗯，而且通往隔壁\x01",
            "街区的桥梁也完全崩塌了。\x02\x03",

            "#1040F总之先调查一下\x01",
            "街上的情况吧。\x02\x03",

            "或许会发现\x01",
            "什么线索也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006F了解。\x02",
    )

    CloseMessageWindow()

    label("loc_315C")

    OP_A2(0x2219)
    OP_28(0x9D, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_13_2BCE end

    def Function_14_3168(): pass

    label("Function_14_3168")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    StopSound(0xD6D8, 0x61A80, 0x0)
    OP_6D(-42870, 0, -61220, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(8000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xE, -46920, 0, -70650, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xF, -47070, 0, -68910, 90)
    ClearChrFlags(0xF, 0x80)
    FadeToBright(1000, 0)
    StopSound(0xD6D8, 0x30D40, 0x1F40)

    def lambda_3210():
        OP_6D(-84570, 2000, -53000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3210)

    def lambda_3228():
        OP_67(0, 6500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3228)

    def lambda_3240():
        OP_6B(6500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3240)

    def lambda_3250():
        OP_6C(327000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3250)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5810   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3168 end

    def Function_15_3277(): pass

    label("Function_15_3277")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_15_3277 end

    def Function_16_330A(): pass

    label("Function_16_330A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_330A end

    def Function_17_3340(): pass

    label("Function_17_3340")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-101730, 2000, -104530, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(-103060, -8000, -116730, 7000)
    Fade(500)
    OP_6D(-103060, -8000, -116730, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xAA, 0x0, 0x64)
    OP_71(0x8, 0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3340 end

    def Function_18_341C(): pass

    label("Function_18_341C")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-101850, 2000, -104940, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x101, -101000, 2000, -105000, 90)
    OP_89(0x102, -102000, 2000, -104000, 90)
    OP_89(0xF8, -103000, 2000, -105000, 90)
    OP_89(0xF9, -102000, 2000, -106000, 90)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x4B0)
    StopSound(0xD6D8, 0x6DDD0, 0x1F40)

    def lambda_34D5():
        OP_6D(-101850, 50000, -104940, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34D5)

    def lambda_34ED():
        OP_67(0, 10680, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34ED)

    def lambda_3505():
        OP_6C(50000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3505)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_341C end

    def Function_19_352C(): pass

    label("Function_19_352C")

    EventBegin(0x0)
    OP_6D(-101850, 60000, -104940, 0)
    OP_67(0, 10680, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(50000, 0)
    OP_6E(262, 0)
    OP_11(0xED, 0xFF, 0xEE, 0xD6D8, 0x6DDD0, 0x0)
    OP_6F(0x5, 600)
    OP_48()
    OP_89(0x101, -101000, 80000, -105000, 90)
    OP_89(0x102, -102000, 80000, -104000, 90)
    OP_89(0xF8, -103000, 80000, -105000, 90)
    OP_89(0xF9, -102000, 80000, -106000, 90)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)
    StopSound(0xD6D8, 0x186A0, 0x2328)

    def lambda_35E8():
        OP_6D(-101850, 2000, -104940, 10500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35E8)

    def lambda_3600():
        OP_67(0, 6500, -10000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3600)

    def lambda_3618():
        OP_6C(45000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3618)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(-100250, 2009, -105250, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -100250, 2009, -105250, 90)
    SetChrPos(0x1, -100250, 2009, -105250, 90)
    SetChrPos(0x2, -100250, 2009, -105250, 90)
    SetChrPos(0x3, -100250, 2009, -105250, 90)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_19_352C end

    def Function_20_36C3(): pass

    label("Function_20_36C3")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_36C3 end

    def Function_21_36DA(): pass

    label("Function_21_36DA")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_3754"),
        (1, "loc_375A"),
        (SWITCH_DEFAULT, "loc_3760"),
    )


    label("loc_3754")

    OP_A2(0x1200)
    Jump("loc_3760")

    label("loc_375A")

    OP_A2(0x1201)
    Jump("loc_3760")

    label("loc_3760")

    Return()

    # Function_21_36DA end

    def Function_22_3761(): pass

    label("Function_22_3761")

    FadeToDark(0, 0, -1)
    OP_6D(-182260, 0, -191970, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_22_3761 end

    SaveToFile()

Try(main)
