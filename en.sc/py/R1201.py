from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Krone Trail',                          # 9
        'Ravennue Trail',                       # 10
        'Bose',                                 # 11
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
        "Function_4_47A",          # 04, 4
        "Function_5_A55",          # 05, 5
        "Function_6_DF9",          # 06, 6
        "Function_7_F57",          # 07, 7
        "Function_8_FAD",          # 08, 8
        "Function_9_101B",         # 09, 9
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_479")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_408")
    TurnDirection(0x106, 0x1, 400)

    ChrTalk(    #0
        0x106,
        (
            "#552FRavennue Village is this way.\x02\x03",

            "I'll go once we hit a break in work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45E")

    label("loc_408")


    ChrTalk(    #1
        0x106,
        (
            "#555FHey. Ravennue is that way.\x02\x03",

            "I said I'll go once we've got some time.\x01",
            "C'mon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45E")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_479")

    Return()

    # Function_3_396 end

    def Function_4_47A(): pass

    label("Function_4_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F1")

    ChrTalk(    #2
        0x101,
        (
            "#1002FWhoops, went too far.\x02\x03",

            "#1002FRavennue is to the north just\x01",
            "before this bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF")

    label("loc_4F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_577")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_51C")

    label("loc_515")

    TurnDirection(0x103, 0x0, 400)

    label("loc_51C")


    ChrTalk(    #3
        0x103,
        (
            "#022FWe've gone a bit too far.\x02\x03",

            "Ravennue is to the north,\x01",
            "just before this bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF")

    label("loc_577")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594")
    Jump("loc_59B")

    label("loc_594")

    TurnDirection(0x104, 0x0, 400)

    label("loc_59B")


    ChrTalk(    #4
        0x104,
        (
            "#030FI believe we have gone a bridge too far.\x02\x03",

            "Fair Ravennue lies to the north...\x01",
            "just BEFORE this bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF")

    label("loc_60E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6AF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62B")
    Jump("loc_632")

    label("loc_62B")

    TurnDirection(0x108, 0x0, 400)

    label("loc_632")


    ChrTalk(    #5
        0x108,
        (
            "#070FSay, haven't we gone too far?\x02\x03",

            "If I remember the map correctly,\x01",
            "Ravennue is to the north, just before\x01",
            "this bridge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AF")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_6CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A54")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_86D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75A")

    ChrTalk(    #6
        0x106,
        (
            "#050FIf we're heading to Ravennue, it's to\x01",
            "the north. We don't have time to be\x01",
            "wanderin' around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_75A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AD")

    ChrTalk(    #7
        0x103,
        (
            "#025FRavennue is to the north.\x01",
            "We don't have time for detours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_7AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F")

    ChrTalk(    #8
        0x108,
        (
            "#072FRavennue is to the north. I don't\x01",
            "think this is the time for side trips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86A")

    label("loc_80F")


    ChrTalk(    #9
        0x101,
        (
            "#1015FRavennue is to the north.\x01",
            "This isn't the time to be making\x01",
            "side trips, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86A")

    Jump("loc_A39")

    label("loc_86D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E1")

    ChrTalk(    #10
        0x106,
        (
            "#053FRavennue is to the north.\x02\x03",

            "#050FWe don't have time to be wanderin'\x01",
            "around the countryside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A36")

    label("loc_8E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A")

    ChrTalk(    #11
        0x103,
        (
            "#025FRavennue is to the north, Estelle.\x02\x03",

            "I don't think we have time for\x01",
            "any detours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A36")

    label("loc_94A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C8")

    ChrTalk(    #12
        0x108,
        (
            "#073FEr, isn't Ravennue to the north?\x02\x03",

            "#070FUnfortunately, I don't think we have\x01",
            "the time for side trips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A36")

    label("loc_9C8")


    ChrTalk(    #13
        0x101,
        (
            "#1015FEr, oops, I think Ravennue is\x01",
            "to the north.\x02\x03",

            "I guess we don't have much time \x01",
            "for side trips, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A36")

    OP_A2(0x0)

    label("loc_A39")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A54")

    Return()

    # Function_4_47A end

    def Function_5_A55(): pass

    label("Function_5_A55")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BD4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACB")

    ChrTalk(    #14
        0x106,
        (
            "#050FRavennue's to the north.\x01",
            "We don't have time to be wanderin'\x01",
            "around the countryside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD1")

    label("loc_ACB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B25")

    ChrTalk(    #15
        0x103,
        (
            "#020FRavennue is to the north.\x01",
            "We don't really have time\x01",
            "for detours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD1")

    label("loc_B25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")

    ChrTalk(    #16
        0x108,
        (
            "#070FRavennue is to the north.\x01",
            "Sadly, I don't think this is the\x01",
            "time for side trips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD1")

    label("loc_B8E")


    ChrTalk(    #17
        0x101,
        (
            "#1000FRavennue is to the north.\x01",
            "Side trips can wait, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD1")

    Jump("loc_D95")

    label("loc_BD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C43")

    ChrTalk(    #18
        0x106,
        (
            "#050FRavennue is to the north.\x02\x03",

            "We don't have time to be wanderin'\x01",
            "around the countryside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_C43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAC")

    ChrTalk(    #19
        0x103,
        (
            "#020FRavennue is to the north,\x01",
            "Estelle.\x02\x03",

            "I don't think we have time for\x01",
            "any detours.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_CAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D25")

    ChrTalk(    #20
        0x108,
        (
            "#070FEr, isn't Ravennue to the north?\x02\x03",

            "Unfortunately, I don't think we have\x01",
            "the time for side trips.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D92")

    label("loc_D25")


    ChrTalk(    #21
        0x101,
        (
            "#1000FEr, oops, I think Ravennue\x01",
            "is to the north.\x02\x03",

            "I guess we don't have much\x01",
            "time for side trips, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D92")

    OP_A2(0x0)

    label("loc_D95")

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

    # Function_5_A55 end

    def Function_6_DF9(): pass

    label("Function_6_DF9")

    OP_EA(0x2, 0xCC, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x360, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_E6A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "Found \x1F\xF9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B05)
    Jump("loc_ECE")

    label("loc_E6A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "Found \x1F\xF9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_ECE")

    Jump("loc_F49")

    label("loc_ED1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05Ever notice nobody else is running around\x01",
            "looting these things? Why do you think that is?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_F49")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_DF9 end

    def Function_7_F57(): pass

    label("Function_7_F57")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #25
        "\x07\x05North: Ravennue Village - 147 selge\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_F57 end

    def Function_8_FAD(): pass

    label("Function_8_FAD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        (
            "\x07\x05East: City of Bose - 140 selge\x01",
            "West: Krone Pass - 301 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_FAD end

    def Function_9_101B(): pass

    label("Function_9_101B")

    EventBegin(0x1)

    ChrTalk(    #27
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_1047():
        OP_6D(-270600, 50, -15450, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1047)

    def lambda_105F():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_105F)

    def lambda_106F():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_106F)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1115")
    OP_C0(0xE, 0xB, 0xFFFBE9B6, 0xA, 0xFFFFC590, 0xE1, 0xFFFBDE3A, 0xFFFFFC18, 0xFFFFBDD4)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_1124")

    label("loc_1115")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1124")
    EventEnd(0x1)

    label("loc_1124")

    Return()

    # Function_9_101B end

    SaveToFile()

Try(main)
