from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'レオ－ルガンイージ',                   # 9
        'ヴォーグル赤',                         # 10
        'ヴォーグル赤',                         # 11
        'ヴォーグル青',                         # 12
        'ヴォーグル青',                         # 13
        'Don',                                  # 14
        'Sky Bandit Dino',                      # 15
        'Sky Bandit Ryan',                      # 16
        'ターゲットキャラ',                     # 17
        'Residential Block - Cradle I',         # 18
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
        "Function_3_E0C",          # 03, 3
        "Function_4_13CB",         # 04, 4
        "Function_5_1734",         # 05, 5
        "Function_6_173D",         # 06, 6
        "Function_7_2501",         # 07, 7
        "Function_8_2E6A",         # 08, 8
        "Function_9_2F25",         # 09, 9
        "Function_10_2FD0",        # 0A, 10
        "Function_11_3089",        # 0B, 11
        "Function_12_3134",        # 0C, 12
        "Function_13_31DF",        # 0D, 13
        "Function_14_393B",        # 0E, 14
        "Function_15_3A59",        # 0F, 15
        "Function_16_3AEC",        # 10, 16
        "Function_17_3B2E",        # 11, 17
        "Function_18_3C0A",        # 12, 18
        "Function_19_3D24",        # 13, 19
        "Function_20_3EBB",        # 14, 20
        "Function_21_3ED2",        # 15, 21
        "Function_22_3F58",        # 16, 22
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_84B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_789")
    TurnDirection(0xD, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FB")

    ChrTalk(    #0
        0xD,
        (
            "#490FHey, Josette.\x02\x03",

            "I was just about to get on to the\x01",
            "wing to fix it.\x02\x03",

            "The men are finally getting around to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10B,
        (
            "#210FThe repairs look like they're going well!\x02\x03",

            "Hopefully the Bobcat'll be ready to roar\x01",
            "again soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xD,
        (
            "#490FLeave it to us!\x02\x03",

            "The Bobcat will be running better\x01",
            "than new by the time you return.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CB)
    Jump("loc_77F")

    label("loc_6FB")


    ChrTalk(    #3
        0xD,
        (
            "#490FWe're going to give these repairs\x01",
            "everything we have.\x02\x03",

            "The Bobcat will be running better\x01",
            "than new by the time you return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F")

    OP_8C(0xD, 90, 0)
    Jump("loc_848")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_819")

    ChrTalk(    #4
        0xD,
        (
            "#196FCOME ON, PUT YOUR BACKS INTO IT,\x01",
            "YOU SLUGS!\x02\x03",

            "You might manage to lift a BABY that way,\x01",
            "but not a ship! Try harder!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_A2(0x0)
    Jump("loc_848")

    label("loc_819")


    ChrTalk(    #5
        0xD,
        "#196FONE! MORE! TIME! Backs into it!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)

    label("loc_848")

    Jump("loc_E08")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_E08")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x452, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5E")
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #6
        0xD,
        (
            "#490FJosette!\x02\x03",

            "How are you? Doing all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10B,
        (
            "#210FNo problems here!\x02\x03",

            "Looks like that might not be true\x01",
            "with the repairs, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xD,
        (
            "#197FYes, well, if we needed to get airborne,\x01",
            "we could, but...\x02\x03",

            "The damage to the internals means\x01",
            "we wouldn't get very far.\x02\x03",

            "Until we're done with the repairs here,\x01",
            "we wouldn't be able to land even if we\x01",
            "escaped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10B,
        (
            "#212FI see...\x02\x03",

            "#210FWell, you need anything, give the word.\x02\x03",

            "I'll go 'excuse' myself with whatever\x01",
            "we need from the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xD,
        (
            "#191FBwahaha! That's the baby sister I know\x01",
            "and love! I'll be counting on you.\x02\x03",

            "#490FListen up, Josette.\x02\x03",

            "You run into any trouble, you call us right\x01",
            "away.\x02\x03",

            "I can still coax some life out of this old\x01",
            "cat. We'll come running no matter where\x01",
            "you are.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x2297)
    Jump("loc_C96")

    label("loc_B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BD7")
    TurnDirection(0xD, 0x10B, 0)

    ChrTalk(    #11
        0xD,
        (
            "#490FSee you, Josette. Stay safe.\x02\x03",

            "If things get dangerous, call us.\x01",
            "We'll be there in an instant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_BD7")


    ChrTalk(    #12
        0xD,
        (
            "#197FIf it came down to it, I could get us\x01",
            "airborne, but...\x02\x03",

            "The damage to the internals means\x01",
            "we wouldn't get very far.\x02\x03",

            "We won't be kissing this place goodbye\x01",
            "until we get that fixed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C96")

    Jump("loc_E08")

    label("loc_C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D66")

    ChrTalk(    #13
        0xD,
        (
            "#197FIf it came down to it, I could get us\x01",
            "airborne, but...\x02\x03",

            "The damage to the internals means\x01",
            "we wouldn't get very far.\x02\x03",

            "We won't be kissing this place goodbye\x01",
            "until we get that fixed.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_E08")

    label("loc_D66")


    ChrTalk(    #14
        0xD,
        (
            "#190FI'm repairing the Bobcat's structure.\x01",
            "The internals, I've left to Kyle.\x02\x03",

            "He has a good head for that sort of thing.\x01",
            "Much better with the finer details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E08")

    TalkEnd(0xFE)
    Return()

    # Function_2_57B end

    def Function_3_E0C(): pass

    label("Function_3_E0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_10A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9E")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F14")

    ChrTalk(    #15
        0xFE,
        "Hey, thanks for helping us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "We're doing what we can to fix\x01",
            "this strut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I-I'm not sure just the two of us\x01",
            "can lift it, to tell you the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "But, don't worry! We'll lift it for you,\x01",
            "your ladyship!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_F9B")

    label("loc_F14")


    ChrTalk(    #19
        0xFE,
        (
            "We're doing what we can to fix\x01",
            "this strut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'm not sure we can do it, but I'll try my\x01",
            "very hardest for you, your ladyship!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9B")

    Jump("loc_10A3")

    label("loc_F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1055")

    ChrTalk(    #21
        0xFE,
        (
            "We're doing what we can to fix\x01",
            "this strut...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I-I'm not sure just the two of us\x01",
            "can lift it, to tell you the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I wish the boss would offer to help...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_10A3")

    label("loc_1055")


    ChrTalk(    #24
        0xFE,
        "So we gotta lift this strut?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I wish the boss would offer to help...\x02",
    )

    CloseMessageWindow()

    label("loc_10A3")

    Jump("loc_13C7")

    label("loc_10A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_13C7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_128E")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1210")

    ChrTalk(    #26
        0xE,
        "Oh, your ladyship! You're back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10B,
        (
            "#210FUh-huh, just wanted to check on stuff.\x02\x03",

            "How's the ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        (
            "One of the struts is bent, but everything\x01",
            "else is pretty much intact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xE,
        (
            "It'll really depend on the internals,\x01",
            "but sounds like it'll be fixed soon-ish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10B,
        "#210FGood. Keep it up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        "Your wish is my command!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22CC)
    Jump("loc_128B")

    label("loc_1210")


    ChrTalk(    #32
        0xE,
        (
            "It'll really depend on the internals,\x01",
            "but sounds like it'll be fixed soon-ish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xE,
        "I'll do everything I can for her!\x02",
    )

    CloseMessageWindow()

    label("loc_128B")

    Jump("loc_13C7")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1349")

    ChrTalk(    #34
        0xE,
        (
            "Oh, thanks for saving us earlier,\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        (
            "We're trying to get some repairs\x01",
            "done to our ship here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        (
            "We don't want to leave it all alone\x01",
            "in a place like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_13C7")

    label("loc_1349")


    ChrTalk(    #37
        0xE,
        (
            "We're trying to get some repairs\x01",
            "done to our ship here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        (
            "The problem is figuring out what\x01",
            "to do about our internals.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C7")

    TalkEnd(0xFE)
    Return()

    # Function_3_E0C end

    def Function_4_13CB(): pass

    label("Function_4_13CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1621")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1554")
    TurnDirection(0xFE, 0x10B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E7")

    ChrTalk(    #39
        0xF,
        (
            "There's no way we're gonna lift this,\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xF,
        (
            "Your ladyship, pleeeeeeease,\x01",
            "say something to the boss!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10B,
        (
            "#212FI don't wanna hear any whining!\x02\x03",

            "Ain't you a man? Show some guts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xF,
        (
            "Your ladyyyyyshiiiip, pleeeeease,\x01",
            "gimme a break!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1551")

    label("loc_14E7")


    ChrTalk(    #43
        0xF,
        (
            "There's no way we're gonna lift this,\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "Your ladyship, pleeeease,\x01",
            "say something to the boss!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1551")

    Jump("loc_161E")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C0")

    ChrTalk(    #45
        0xF,
        (
            "There's no way we're gonna lift this,\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xF,
        (
            "*sigh* The boss asks way too\x01",
            "much of us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_161E")

    label("loc_15C0")


    ChrTalk(    #47
        0xF,
        (
            "How the hell are we supposed\x01",
            "to lift this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xF,
        (
            "The boss really asks way too\x01",
            "much of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161E")

    Jump("loc_1730")

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_1730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16C9")

    ChrTalk(    #49
        0xF,
        "Ahhhh, man! This is hopeless!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "It would've been easier if it'd just\x01",
            "broken clean off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        (
            "I have no idea how we'll fix a bend\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1730")

    label("loc_16C9")


    ChrTalk(    #52
        0xF,
        (
            "Okay, how're we gonna go about\x01",
            "repairing this wing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        "I need to talk to the boss about this...\x02",
    )

    CloseMessageWindow()

    label("loc_1730")

    TalkEnd(0xFE)
    Return()

    # Function_4_13CB end

    def Function_5_1734(): pass

    label("Function_5_1734")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_1734 end

    def Function_6_173D(): pass

    label("Function_6_173D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1754")
    Call(0, 21)
    Call(0, 22)

    label("loc_1754")

    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_17A1"),
        (5, "loc_17B8"),
        (3, "loc_17CF"),
        (4, "loc_17E6"),
        (6, "loc_17FD"),
        (7, "loc_1814"),
        (8, "loc_182B"),
        (SWITCH_DEFAULT, "loc_1842"),
    )


    label("loc_17A1")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_1842")

    label("loc_17B8")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_1842")

    label("loc_17CF")

    OP_D2(0x701E8, 0x701F4, 0xE)
    OP_D2(0x701E9, 0x701F5, 0xF)
    Jump("loc_1842")

    label("loc_17E6")

    OP_D2(0x27036E, 0x27037B, 0xE)
    OP_D2(0x27036F, 0x27037C, 0xF)
    Jump("loc_1842")

    label("loc_17FD")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_1842")

    label("loc_1814")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_1842")

    label("loc_182B")

    OP_D2(0x270176, 0x270183, 0xE)
    OP_D2(0x270177, 0x270184, 0xF)
    Jump("loc_1842")

    label("loc_1842")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1867"),
        (5, "loc_187E"),
        (3, "loc_1895"),
        (4, "loc_18AC"),
        (6, "loc_18C3"),
        (7, "loc_18DA"),
        (8, "loc_18F1"),
        (SWITCH_DEFAULT, "loc_1908"),
    )


    label("loc_1867")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_1908")

    label("loc_187E")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_1908")

    label("loc_1895")

    OP_D2(0x701E8, 0x701F4, 0x10)
    OP_D2(0x701E9, 0x701F5, 0x11)
    Jump("loc_1908")

    label("loc_18AC")

    OP_D2(0x27036E, 0x27037B, 0x10)
    OP_D2(0x27036F, 0x27037C, 0x11)
    Jump("loc_1908")

    label("loc_18C3")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_1908")

    label("loc_18DA")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_1908")

    label("loc_18F1")

    OP_D2(0x270176, 0x270183, 0x10)
    OP_D2(0x270177, 0x270184, 0x11)
    Jump("loc_1908")

    label("loc_1908")

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

    def lambda_1AB4():

        label("loc_1AB4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1AB4")

    QueueWorkItem2(0x8, 3, lambda_1AB4)

    def lambda_1AC7():

        label("loc_1AC7")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1AC7")

    QueueWorkItem2(0x9, 3, lambda_1AC7)

    def lambda_1ADA():

        label("loc_1ADA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1ADA")

    QueueWorkItem2(0xA, 3, lambda_1ADA)

    def lambda_1AED():

        label("loc_1AED")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1AED")

    QueueWorkItem2(0xB, 3, lambda_1AED)

    def lambda_1B00():

        label("loc_1B00")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1B00")

    QueueWorkItem2(0xC, 3, lambda_1B00)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 19)
    SoundLoad(503)
    LoadEffect(0x0, "map\\mp003_00.eff")
    LoadEffect(0x1, "monster\\msc0331.eff")
    LoadEffect(0x2, "battle\\btbomb00.eff")
    OP_20(0x3E8)
    FadeToBright(1000, 0)
    OP_E3(0x0, 0x9, 0x0, 0x0)
    OP_E3(0x0, 0xA, 0x0, 0x0)
    OP_E3(0x0, 0xB, 0x0, 0x0)
    OP_E3(0x0, 0xC, 0x0, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BDB")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C19")

    label("loc_1BDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C02")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C19")

    label("loc_1C02")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1C19")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C45")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C83")

    label("loc_1C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1C83")

    label("loc_1C6C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1C83")

    Sleep(1000)

    ChrTalk(    #54
        0x101,
        "#1004F#5PJoshua, look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x102,
        (
            "#1044F#6PI see it. Why the heck is--\x02\x03",

            "#1042FTch!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x29)
    Sleep(500)

    def lambda_1CEC():
        OP_6D(-64629, 0, -63910, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CEC)

    def lambda_1D04():
        OP_67(0, 6510, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D04)

    def lambda_1D1C():
        OP_6B(4510, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D1C)

    def lambda_1D2C():
        OP_6C(296000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1D2C)
    OP_6E(453, 7000)
    Sleep(500)
    Fade(500)
    OP_6D(-64629, 0, -62690, 0)
    OP_67(0, 4370, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(307000, 0)
    OP_6E(333, 0)
    OP_0D()

    def lambda_1D8D():
        OP_8E(0xFE, 0xFFFF0A74, 0x0, 0xFFFF0C22, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1D8D)
    Sleep(50)

    def lambda_1DAD():
        OP_8E(0xFE, 0xFFFF09F2, 0x0, 0xFFFEFF16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1DAD)
    Sleep(50)

    def lambda_1DCD():
        OP_8E(0xFE, 0xFFFF08BC, 0x0, 0xFFFF074A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_1DCD)
    Sleep(50)

    def lambda_1DED():
        OP_8E(0xFE, 0xFFFF09CA, 0x0, 0xFFFF02C2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1DED)
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
            "#214FDON'T GET ANY CLOSER, YOU!\x02\x03",

            "I won't let you hurt the Bobcat anymore!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E81():
        OP_6D(-70470, 0, -61640, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E81)

    def lambda_1E99():
        OP_67(0, 4130, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E99)

    def lambda_1EB1():
        OP_6B(2890, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EB1)
    OP_8F(0x8, 0xFFFEF228, 0x3E8, 0xFFFF0876, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    SetChrChipByIndex(0x8, 29)
    OP_0D()
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    PlayEffect(0x1, 0x0, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x10, -1000, 0, 0, 0)

    def lambda_1F2D():
        OP_6D(-70470, 1500, -61640, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F2D)
    Sleep(1000)

    def lambda_1F4A():
        OP_6D(-67470, 0, -61640, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F4A)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2, 0x1, 0xFF, -59210, 0, -63960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 22)

    def lambda_1FAF():
        OP_96(0xFE, 0xFFFF2798, 0x0, 0xFFFF07D6, 0x514, 0x1388)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_1FAF)
    OP_7C(0x190, 0x190, 0xBB8, 0x1F4)
    Fade(500)
    OP_6D(-54060, 0, -63310, 0)
    OP_67(0, 5630, -10000, 0)
    OP_6B(2390, 0)
    OP_6C(67000, 0)
    OP_6E(401, 0)
    SetChrChipByIndex(0x8, 0)
    WaitChrThread(0x146, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 20)

    def lambda_203D():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x146, 1, lambda_203D)

    ChrTalk(    #57
        0x146,
        "#216F#5PAaaaah!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x146, 0x1)
    Sleep(500)

    def lambda_206C():
        OP_6D(-58360, 0, -63110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_206C)

    def lambda_2084():
        OP_8E(0xFE, 0xFFFF1604, 0x0, 0xFFFF10DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2084)
    Sleep(100)

    def lambda_20A4():
        OP_8E(0xFE, 0xFFFF12E4, 0x0, 0xFFFF0A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20A4)
    Sleep(150)

    def lambda_20C4():
        OP_8E(0xFE, 0xFFFF12C6, 0x0, 0xFFFF04C1, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20C4)
    Sleep(140)

    def lambda_20E4():
        OP_8E(0xFE, 0xFFFF15B4, 0x0, 0xFFFEFF20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20E4)
    Sleep(800)

    def lambda_2104():
        OP_8E(0xFE, 0xFFFF027C, 0x3E8, 0xFFFF066E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2104)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x8, 0x1)
    SetMapFlags(0x10)

    ChrTalk(    #58
        0x146,
        (
            "#413FNoooo... Kyle... Don...\x02\x03",

            "#215FJoshua...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, -77950, 0, -65650, 90)

    NpcTalk(    #59
        0x101,
        "Girl's Voice",
        "Looks like someone's in over their head!\x02",
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

    def lambda_222A():
        OP_6D(-66700, 0, -62400, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_222A)

    def lambda_2242():
        OP_67(0, 5450, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2242)

    def lambda_225A():
        OP_6B(2390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_225A)

    def lambda_226A():
        OP_6C(54000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_226A)

    def lambda_227A():
        OP_6E(417, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_227A)

    def lambda_228A():
        OP_8C(0xFE, 270, 200)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_228A)
    Sleep(100)

    def lambda_229D():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_229D)

    def lambda_22AB():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_22AB)
    Sleep(100)

    def lambda_22BE():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_22BE)

    def lambda_22CC():
        OP_8C(0xFE, 270, 300)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_22CC)
    WaitChrThread(0x102, 0x2)
    Sleep(500)

    ChrTalk(    #60
        0x146,
        "#213F#6PAirhead girl?! And...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1019F#5PI can always poke a nice big air hole in\x01",
            "YOUR head with my staff, you grimy tomboy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#1046F#5PTalk later!\x01",
            "We have a fight on our hands first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x146,
        "#414F#6PY-Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1007F#5POh, brother...\x02",
    )

    CloseMessageWindow()
    OP_99(0x146, 0x2, 0x0, 0x3E8)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x146, 19)
    SetChrSubChip(0x146, 0)
    OP_0D()
    Sleep(500)

    def lambda_23FC():
        OP_6D(-62330, 0, -62850, 450)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23FC)

    def lambda_2414():
        OP_67(0, 6930, -10000, 450)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2414)

    def lambda_242C():
        OP_6B(2000, 450)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_242C)

    def lambda_243C():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_243C)
    Sleep(30)

    def lambda_245C():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_245C)

    def lambda_2477():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_2477)
    Sleep(30)

    def lambda_2497():
        OP_91(0xFE, 0x1770, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_2497)
    Sleep(80)
    SetChrChipByIndex(0x146, 18)
    SetChrFlags(0x146, 0x1000)

    def lambda_24C1():
        OP_91(0xFE, 0xFFFFF060, 0x0, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_24C1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_44(0x146, 0xFF)
    OP_B6(0x45, 0x1)
    Battle(0x50E, 0x300019, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_173D end

    def Function_7_2501(): pass

    label("Function_7_2501")

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

    def lambda_2604():
        OP_6B(2300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2604)
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
            "#1007F#4PPhew! Okay, that's that.\x02\x03",

            "#1002FNearly bent my staff on that big one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#1035F#4PThat was one of the society's heavy-weight\x01",
            "archaism weapons, the Leor Gun-EZ.\x02\x03",

            "#1043FIt's meant to be used for location\x01",
            "defense, though, not assault...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_274A():
        OP_6D(-61840, 0, -65830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_274A)

    def lambda_2762():
        OP_8E(0xFE, 0xFFFF0EA2, 0x0, 0xFFFF059D, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2762)
    Sleep(100)

    def lambda_2782():
        OP_8E(0xFE, 0xFFFF0E0C, 0x0, 0xFFFF006A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2782)
    Sleep(80)

    def lambda_27A2():
        OP_8E(0xFE, 0xFFFF07B8, 0x0, 0xFFFEFEB2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_27A2)
    Sleep(120)

    def lambda_27C2():
        OP_8E(0xFE, 0xFFFF08C6, 0x0, 0xFFFF0498, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_27C2)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #67
        0x102,
        (
            "#1040F#4PWe can wonder about that later.\x01",
            "I'm glad you're safe, Josette.\x02\x03",

            "But what are the Capuas doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x146,
        (
            "#215F#5PYeah, um...\x02\x03",

            "#413FAfter you left, we hid out near the border.\x02\x03",

            "But then this weird thing appeared in\x01",
            "the sky, and when we tried checking\x01",
            "it out the Bobcat's power cut out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#4PAaaand so you guys cratered.\x02\x03",

            "#1004FThough, hang on...\x02",
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
            "#1015F#4PShouldn't your brothers be here?\x02\x03",

            "#1016FYou guys are usually all together.\x01",
            "Did they head out to scout or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x146, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #71
        0x146,
        (
            "#215F#5PMy...br...\x02\x03",

            "#413F*sniffle* Myyyyy...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #72
        0x101,
        "#1020F#4PWhoa, whoa, hey! What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        (
            "#1035F#4PJosette, please, calm down.\x02\x03",

            "#1040FWe're here, don't worry.\x01",
            "Take your time and tell us what happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x146, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #74
        0x146,
        (
            "#417F#5P*sob*...\x02\x03",

            "#418FJoshua... Joshuaaaaaaa!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B62():

        label("loc_2B62")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2B62")

    QueueWorkItem2(0x101, 2, lambda_2B62)

    def lambda_2B73():

        label("loc_2B73")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2B73")

    QueueWorkItem2(0x102, 2, lambda_2B73)

    def lambda_2B84():

        label("loc_2B84")

        TurnDirection(0xFE, 0x146, 400)
        OP_48()
        Jump("loc_2B84")

    QueueWorkItem2(0xF8, 2, lambda_2B84)

    def lambda_2B95():
        TurnDirection(0xFE, 0x146, 0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2B95)

    def lambda_2BA3():
        OP_6D(-62450, 0, -65050, 1500)
        ExitThread()

    QueueWorkItem(0x146, 3, lambda_2BA3)
    SetChrFlags(0x146, 0x40)

    def lambda_2BC0():
        OP_8E(0x146, 0xFFFF0FF6, 0x0, 0xFFFF059D, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x146, 0, lambda_2BC0)
    WaitChrThread(0x146, 0x0)

    def lambda_2BE0():

        label("loc_2BE0")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_2BE0")

    QueueWorkItem2(0x101, 2, lambda_2BE0)
    SetChrFlags(0x146, 0x2)
    SetChrSubChip(0x146, 0)
    SetChrChipByIndex(0x146, 23)

    def lambda_2C00():
        OP_8F(0xFE, 0xFFFF0DD0, 0x0, 0xFFFF059D, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2C00)
    WaitChrThread(0x102, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C9B")

    label("loc_2C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C84")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2C9B")

    label("loc_2C84")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2C9B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC7")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D05")

    label("loc_2CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEE")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2D05")

    label("loc_2CEE")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2D05")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D2B")

    ChrTalk(    #75
        0x105,
        "#1164FOh, my!\x02",
    )

    CloseMessageWindow()

    label("loc_2D2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4A")

    ChrTalk(    #76
        0x107,
        "#065FWaaah!\x02",
    )

    CloseMessageWindow()

    label("loc_2D4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D6E")

    ChrTalk(    #77
        0x104,
        "#037FWell, then.\x02",
    )

    CloseMessageWindow()

    label("loc_2D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D90")

    ChrTalk(    #78
        0x103,
        "#027FOh, MY...\x02",
    )

    CloseMessageWindow()

    label("loc_2D90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DB3")

    ChrTalk(    #79
        0x109,
        "#1064FEr, whoa.\x02",
    )

    CloseMessageWindow()

    label("loc_2DB3")


    ChrTalk(    #80
        0x101,
        "#1020F#3PWha, er, hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x146,
        (
            "#418F#6PThose creeps took my family!\x02\x03",

            "Kyle and Don baited them so\x01",
            "I could get away...\x02\x03",

            "#417FJoshuaaaaaa...what do I do?!\x02",
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

    # Function_7_2501 end

    def Function_8_2E6A(): pass

    label("Function_8_2E6A")

    OP_8C(0xFE, 315, 500)

    def lambda_2E77():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E77)
    Sleep(300)
    OP_44(0x8, 0x0)
    OP_43(0x9, 0x0, 0x0, 0x9)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 225, 500)

    def lambda_2EA3():
        OP_99(0xFE, 0x0, 0x7, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2EA3)
    Sleep(300)
    OP_44(0xC, 0x0)
    OP_43(0xC, 0x0, 0x0, 0xC)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 270, 500)

    def lambda_2ECF():
        OP_99(0xFE, 0x0, 0x4, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ECF)
    Sleep(200)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0xA)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 270, 500)
    Sleep(200)

    def lambda_2F00():
        OP_99(0xFE, 0x0, 0x6, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F00)
    OP_44(0xB, 0x0)
    OP_43(0xB, 0x0, 0x0, 0xB)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_2E6A end

    def Function_9_2F25(): pass

    label("Function_9_2F25")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)

    def lambda_2F85():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2F85)
    OP_8F(0xFE, 0xFFFEFB38, 0x0, 0xFFFF171C, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 23)

    def lambda_2FC2():

        label("loc_2FC2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2FC2")

    QueueWorkItem2(0xFE, 3, lambda_2FC2)
    Return()

    # Function_9_2F25 end

    def Function_10_2FD0(): pass

    label("Function_10_2FD0")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)

    def lambda_3030():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3030)

    def lambda_304A():
        OP_8C(0xFE, 135, 0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_304A)
    OP_8F(0xFE, 0xFFFEF750, 0x0, 0xFFFF101E, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 23)

    def lambda_307B():

        label("loc_307B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_307B")

    QueueWorkItem2(0xFE, 3, lambda_307B)
    Return()

    # Function_10_2FD0 end

    def Function_11_3089(): pass

    label("Function_11_3089")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)

    def lambda_30E9():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_30E9)
    OP_8F(0xFE, 0xFFFEF836, 0x0, 0xFFFEFE3A, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)

    def lambda_3126():

        label("loc_3126")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3126")

    QueueWorkItem2(0xFE, 3, lambda_3126)
    Return()

    # Function_11_3089 end

    def Function_12_3134(): pass

    label("Function_12_3134")

    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0xFE, 0, 300, -300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x32, 0x32, 0xBB8, 0x64)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)

    def lambda_3194():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3194)
    OP_8F(0xFE, 0xFFFEFBE2, 0x0, 0xFFFEF6E2, 0x3E80, 0x0)
    WaitChrThread(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 26)

    def lambda_31D1():

        label("loc_31D1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_31D1")

    QueueWorkItem2(0xFE, 3, lambda_31D1)
    Return()

    # Function_12_3134 end

    def Function_13_31DF(): pass

    label("Function_13_31DF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31F6")
    Call(0, 21)
    Call(0, 15)

    label("loc_31F6")

    OP_6D(-83690, 0, -60600, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -84410, 0, -62530, 0)
    SetChrPos(0x102, -83090, 0, -61240, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3287")
    SetChrPos(0xF9, -85770, 0, -61600, 90)
    SetChrPos(0x10B, -84210, 0, -59930, 180)
    Jump("loc_32DB")

    label("loc_3287")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B9")
    SetChrPos(0xF8, -85770, 0, -61600, 90)
    SetChrPos(0x10B, -84210, 0, -59930, 180)
    Jump("loc_32DB")

    label("loc_32B9")

    SetChrPos(0xF8, -84210, 0, -59930, 180)
    SetChrPos(0xF9, -85770, 0, -61600, 90)

    label("loc_32DB")

    OP_31(0xFF, 0xFE, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37D5")

    ChrTalk(    #82
        0x101,
        (
            "#1006FRight, then. Let's get back to it.\x02\x03",

            "#1004FSo, Josette.\x02\x03",

            "Do you know of any other exits to\x01",
            "other parts of the city around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10B,
        (
            "#413F#6PNo... I'm afraid I don't.\x02\x03",

            "#212FIn a way, it's kinda weird. All the bridges\x01",
            "to the other city sections have collapsed,\x01",
            "but I don't think the society did it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1007FMmm... Well, that's kind of an\x01",
            "issue for us, either way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1040FIt may be worth our time to\x01",
            "search this district again.\x02\x03",

            "We may be able to find a\x01",
            "clue of some sort.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34ED():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34ED)
    Sleep(50)
    TurnDirection(0x10B, 0x102, 400)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#1019F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10B,
        "#212F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#1048FAnd, um, on another note...\x02\x01",

            "#1052F... Please forgive me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1001F#5PForgive you? Whatever for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10B,
        (
            "#211F#6PJoshua, if you're not sure something's\x01",
            "wrong, just act normal, y'knoooow?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_362F")

    ChrTalk(    #91
        0x107,
        "#067F#5P(Aww, I kinda feel bad for him...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_362F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3676")

    ChrTalk(    #92
        0x106,
        "#551F#5P(Well, that's a bed of needles he's on.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_3676")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36C1")

    ChrTalk(    #93
        0x109,
        (
            "#1068F#5P(Endure the pain, Joshua!\x01",
            "Endure the pain!)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_36C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FB")

    ChrTalk(    #94
        0x108,
        "#070F#1P(Ah, to be that age again.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_36FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_373A")

    ChrTalk(    #95
        0x103,
        "#027F#5P(A lesson learned the hard way.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_373A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_378E")

    ChrTalk(    #96
        0x105,
        (
            "#1380F#5P(At this point, I do feel\x01",
            "a little sorry for him...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37D2")

    label("loc_378E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37D2")

    ChrTalk(    #97
        0x104,
        "#031F#5P(Ahhh, what fun! The trials of youth...)\x02",
    )

    CloseMessageWindow()

    label("loc_37D2")

    Jump("loc_392F")

    label("loc_37D5")


    ChrTalk(    #98
        0x101,
        (
            "#1006FRight, then. Let's get back to it.\x02\x03",

            "#1015FBefore she left, Josette said she\x01",
            "hadn't found any other ways out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#1035FYes, the bridges to the neighboring sectors\x01",
            "seem to have collapsed some time ago.\x02\x03",

            "#1040FIt may be worth our time to search\x01",
            "this district again.\x02\x03",

            "We may be able to find a\x01",
            "clue of some sort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006FRoger that.\x02",
    )

    CloseMessageWindow()

    label("loc_392F")

    OP_A2(0x2219)
    OP_28(0x9D, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_13_31DF end

    def Function_14_393B(): pass

    label("Function_14_393B")

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

    def lambda_39E3():
        OP_6D(-84570, 2000, -53000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_39E3)

    def lambda_39FB():
        OP_67(0, 6500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_39FB)

    def lambda_3A13():
        OP_6B(6500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3A13)

    def lambda_3A23():
        OP_6C(327000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3A23)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5810   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_393B end

    def Function_15_3A59(): pass

    label("Function_15_3A59")

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

    # Function_15_3A59 end

    def Function_16_3AEC(): pass

    label("Function_16_3AEC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05The door is firmly locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_3AEC end

    def Function_17_3B2E(): pass

    label("Function_17_3B2E")

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

    # Function_17_3B2E end

    def Function_18_3C0A(): pass

    label("Function_18_3C0A")

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

    def lambda_3CC3():
        OP_6D(-101850, 50000, -104940, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CC3)

    def lambda_3CDB():
        OP_67(0, 10680, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CDB)

    def lambda_3CF3():
        OP_6C(50000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CF3)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C6001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3C0A end

    def Function_19_3D24(): pass

    label("Function_19_3D24")

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

    def lambda_3DE0():
        OP_6D(-101850, 2000, -104940, 10500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DE0)

    def lambda_3DF8():
        OP_67(0, 6500, -10000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DF8)

    def lambda_3E10():
        OP_6C(45000, 10500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3E10)
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

    # Function_19_3D24 end

    def Function_20_3EBB(): pass

    label("Function_20_3EBB")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_3EBB end

    def Function_21_3ED2(): pass

    label("Function_21_3ED2")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F4B"),
        (1, "loc_3F51"),
        (SWITCH_DEFAULT, "loc_3F57"),
    )


    label("loc_3F4B")

    OP_A2(0x1200)
    Jump("loc_3F57")

    label("loc_3F51")

    OP_A2(0x1201)
    Jump("loc_3F57")

    label("loc_3F57")

    Return()

    # Function_21_3ED2 end

    def Function_22_3F58(): pass

    label("Function_22_3F58")

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

    # Function_22_3F58 end

    SaveToFile()

Try(main)
