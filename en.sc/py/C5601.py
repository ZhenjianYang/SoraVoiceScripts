from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5601   ._SN',
        MapName             = 'Other',
        Location            = 'C5601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        'Silver-Haired Youth',                  # 9
        'Weissmann',                            # 10
        'Renne',                                # 11
        'Renne',                                # 12
        'Estelle',                              # 13
        'Campanella',                           # 14
        '結社艇',                               # 15
        '結社艇（影）',                         # 16
        '結社艇（ライト）',                     # 17
        'Pater-Mater',                          # 18
        'Boat',                                 # 19
        'Boat （ダミー）',                      # 20
        'Targeting Camera',                     # 21
        'Grant',                                # 22
        'Carna',                                # 23
        'Anelace',                              # 24
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
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00053 ._CH',             # 02
        'ED6_DT07/CH00033 ._CH',             # 03
        'ED6_DT07/CH00043 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT27/CH03083 ._CH',             # 07
        'ED6_DT07/CH02040 ._CH',             # 08
        'ED6_DT27/CH03550 ._CH',             # 09
        'ED6_DT27/CH03510 ._CH',             # 0A
        'ED6_DT27/CH03004 ._CH',             # 0B
        'ED6_DT29/CH12570 ._CH',             # 0C
        'ED6_DT29/CH12571 ._CH',             # 0D
        'ED6_DT27/CH03600 ._CH',             # 0E
        'ED6_DT26/CH20295 ._CH',             # 0F
        'ED6_DT26/CH20379 ._CH',             # 10
        'ED6_DT07/CH01260 ._CH',             # 11
        'ED6_DT07/CH01240 ._CH',             # 12
        'ED6_DT07/CH01630 ._CH',             # 13
        'ED6_DT26/CH20288 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00053P._CP',             # 02
        'ED6_DT07/CH00033P._CP',             # 03
        'ED6_DT07/CH00043P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT27/CH03083P._CP',             # 07
        'ED6_DT07/CH02040P._CP',             # 08
        'ED6_DT27/CH03550P._CP',             # 09
        'ED6_DT27/CH03510P._CP',             # 0A
        'ED6_DT27/CH03004P._CP',             # 0B
        'ED6_DT29/CH12570P._CP',             # 0C
        'ED6_DT29/CH12571P._CP',             # 0D
        'ED6_DT27/CH03600P._CP',             # 0E
        'ED6_DT26/CH20295P._CP',             # 0F
        'ED6_DT26/CH20379P._CP',             # 10
        'ED6_DT07/CH01260P._CP',             # 11
        'ED6_DT07/CH01240P._CP',             # 12
        'ED6_DT07/CH01630P._CP',             # 13
        'ED6_DT26/CH20288P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x188,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1E5,
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
        NpcIndex            = 0x84,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6510,
        Z                   = -6050,
        Y                   = -26680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -6770,
        Z                   = -5970,
        Y                   = -27880,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -6380,
        Z                   = -5900,
        Y                   = -28820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 9520,
        TriggerZ            = 9000,
        TriggerY            = 6150,
        TriggerRange        = 1000,
        ActorX              = 9960,
        ActorZ              = 9000,
        ActorY              = 6600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15010,
        TriggerZ            = 0,
        TriggerY            = -3880,
        TriggerRange        = 800,
        ActorX              = -15010,
        ActorZ              = 1000,
        ActorY              = -3880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4500,
        TriggerZ            = -6000,
        TriggerY            = -27040,
        TriggerRange        = 1000,
        ActorX              = -4500,
        ActorZ              = -5000,
        ActorY              = -27040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3BE",          # 00, 0
        "Function_1_4AD",          # 01, 1
        "Function_2_590",          # 02, 2
        "Function_3_6F1",          # 03, 3
        "Function_4_7DB",          # 04, 4
        "Function_5_84A",          # 05, 5
        "Function_6_9EF",          # 06, 6
        "Function_7_14E7",         # 07, 7
        "Function_8_155D",         # 08, 8
        "Function_9_15BF",         # 09, 9
        "Function_10_1635",        # 0A, 10
        "Function_11_1697",        # 0B, 11
        "Function_12_1875",        # 0C, 12
        "Function_13_192C",        # 0D, 13
        "Function_14_19ED",        # 0E, 14
        "Function_15_2297",        # 0F, 15
        "Function_16_22F2",        # 10, 16
        "Function_17_2341",        # 11, 17
        "Function_18_2388",        # 12, 18
        "Function_19_241D",        # 13, 19
        "Function_20_24B7",        # 14, 20
        "Function_21_2518",        # 15, 21
        "Function_22_25BB",        # 16, 22
        "Function_23_260F",        # 17, 23
        "Function_24_2652",        # 18, 24
        "Function_25_4451",        # 19, 25
        "Function_26_44DA",        # 1A, 26
        "Function_27_4537",        # 1B, 27
        "Function_28_45BD",        # 1C, 28
        "Function_29_45C9",        # 1D, 29
    )


    def Function_0_3BE(): pass

    label("Function_0_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 7)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_401")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_3E1")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_401")

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_3F5")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_401")

    label("loc_3F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 0)), scpexpr(EXPR_END)), "loc_401")
    ClearChrFlags(0x15, 0x80)

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_409")

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_438")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10)
    OP_11(0x81, 0x99, 0xCF, 0x186A0, 0x493E0, 0x0)
    Event(0, 6)
    Jump("loc_4AC")

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_456")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    OP_64(0x0, 0x1)
    Event(0, 12)
    Jump("loc_4AC")

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_474")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    OP_64(0x0, 0x1)
    Event(0, 13)
    Jump("loc_4AC")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_493")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_4AC")

    label("loc_493")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AC")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)

    label("loc_4AC")

    Return()

    # Function_0_3BE end

    def Function_1_4AD(): pass

    label("Function_1_4AD")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFE3AE0, 0x230073)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    OP_6F(0x1, 0)
    Jump("loc_4DD")

    label("loc_4D6")

    OP_6F(0x1, 60)

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 7)), scpexpr(EXPR_END)), "loc_4FF")
    OP_10(0x0, 0x1)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    OP_64(0x1, 0x1)
    Jump("loc_502")

    label("loc_4FF")

    OP_10(0x0, 0x0)

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_END)), "loc_51F")
    OP_A1(0x12, 0x3)
    SetChrPos(0x12, -8590, -8500, -33600, 90)

    label("loc_51F")

    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_1C(0x5, 0x0, 0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_586")
    LoadEffect(0x6, "map\\\\mp027_00.eff")
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Jump("loc_58F")

    label("loc_586")

    OP_71(0x1D, 0x4)
    OP_64(0x2, 0x1)

    label("loc_58F")

    Return()

    # Function_1_4AD end

    def Function_2_590(): pass

    label("Function_2_590")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_610")

    ChrTalk(    #0
        0x15,
        (
            "#822FI'm pretty sure we'll get reinforcements\x01",
            "from the guild and army soon...\x02\x03",

            "Don't go crazy just yet, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED")

    label("loc_610")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_669")

    ChrTalk(    #1
        0x15,
        (
            "#824FJust Anelace left now, huh?\x02\x03",

            "#822FSorry. I'm counting on you guys...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6ED")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 0)), scpexpr(EXPR_END)), "loc_6ED")

    ChrTalk(    #2
        0x15,
        (
            "#826FAgh...!\x02\x03",

            "#824FDon't... Don't worry about me,\x01",
            "darn it. Keep investigating.\x02\x03",

            "Carna and Anelace're...in your hands...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ED")

    TalkEnd(0x15)
    Return()

    # Function_2_590 end

    def Function_3_6F1(): pass

    label("Function_3_6F1")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_779")

    ChrTalk(    #3
        0x16,
        (
            "#833FI can't believe that black-haired boy\x01",
            "managed to get so far in on his own...\x02\x03",

            "#834FI hope he's safe, at least...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D7")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_7D7")

    ChrTalk(    #4
        0x16,
        (
            "#836FNgh... Don't mind me.\x02\x03",

            "#835FI can take care of myself...\x01",
            "even like this. Go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7")

    TalkEnd(0x16)
    Return()

    # Function_3_6F1 end

    def Function_4_7DB(): pass

    label("Function_4_7DB")

    TalkBegin(0x17)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #5
        0x17,
        (
            "#813FI think...Joshua probably headed\x01",
            "for the roof.\x02\x03",

            "#812FEstelle, be careful, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    TalkEnd(0x17)
    Return()

    # Function_4_7DB end

    def Function_5_84A(): pass

    label("Function_5_84A")

    OP_EA(0x2, 0x9E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_922")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E9, 1)"), scpexpr(EXPR_END)), "loc_8BB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xE9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D28)
    Jump("loc_91F")

    label("loc_8BB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xE9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_91F")

    Jump("loc_960")

    label("loc_922")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Sorry, but I'm cutting you off.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_960")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x43)"), scpexpr(EXPR_END)), "loc_97F")
    Jump("loc_9E6")

    label("loc_97F")


    AnonymousTalk(    #9
        (
            "\x07\x00Found a scrap of paper with a [ #489i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x07\x00Learned [ #489i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_9E6")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_84A end

    def Function_6_9EF(): pass

    label("Function_6_9EF")

    EventBegin(0x0)
    OP_DB()
    OP_E8(0x88, 0x13, 0x0, 0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A1B")
    ClearMapFlags(0x10)
    Call(0, 25)
    Call(0, 26)
    SetMapFlags(0x10)

    label("loc_A1B")

    OP_6D(31040, -6770, 3020, 0)
    OP_67(0, 11880, -10000, 0)
    OP_6B(13600, 0)
    OP_6C(351000, 0)
    OP_6E(410, 0)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x2)
    OP_71(0x3, 0x40)
    OP_A1(0x12, 0x3)
    SetChrPos(0x12, 70630, -7500, 40480, 45)
    SetChrFlags(0x12, 0x40)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, 70320, -7500, 39620, 225)
    OP_89(0x109, 69800, -7500, 40000, 225)
    OP_89(0xF8, 71200, -7500, 40440, 225)
    OP_89(0xF9, 70680, -7500, 40990, 225)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x109, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B2F")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 1)

    label("loc_B2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B47")
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 2)

    label("loc_B47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5F")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 3)

    label("loc_B5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B77")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 4)

    label("loc_B77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8F")
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 5)

    label("loc_B8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA7")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 6)

    label("loc_BA7")

    LoadEffect(0x0, "map\\\\mp013_02.eff")
    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_01.eff")
    PlayEffect(0x1, 0x1, 0x12, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x12, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_72(0x1B, 0x4)
    OP_71(0x3, 0x20)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    OP_22(0xDA, 0x1, 0x28)
    StopSound(0x88B8, 0x927C0, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_C9F():
        OP_6D(11950, -8800, -2530, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C9F)

    def lambda_CB7():
        OP_6C(3000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CB7)

    def lambda_CC7():
        OP_8F(0x12, 0x2828, 0xFFFFDECC, 0xFFFF7CF2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CC7)
    Sleep(6000)
    OP_C4(0x0, 0x40)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_44(0x12, 0x0)
    StopSound(0x88B8, 0x1D4C0, 0x0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(3000, 0)
    OP_6E(597, 0)
    OP_69(0x12, 0x0)
    OP_6A(0x12)

    def lambda_D3F():
        OP_8F(0x12, 0x2828, 0xFFFFDECC, 0xFFFF7CF2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_D3F)
    FadeToBright(500, 0)
    OP_24(0xDA, 0x4B)
    OP_0D()
    Sleep(500)
    OP_E8(0xE8, 0x3, 0x0, 0x0)

    ChrTalk(    #11 op#A op#5
        0x101,
        "#1004F#6P#5AHey!\x05\x02",
    )

    OP_56(0x0)
    OP_59()
    Sleep(300)

    ChrTalk(    #12 op#A op#5
        0x109,
        "#1063F#5P#14ALooks like we made it through.\x05\x02",
    )

    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    Fade(500)
    OP_6D(-9850, -6060, -34780, 0)
    OP_67(0, 10860, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_C4(0x1, 0x40)
    WaitChrThread(0x12, 0x0)

    def lambda_E21():
        OP_8C(0xFE, 90, 0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_E21)

    def lambda_E2F():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E2F)

    def lambda_E3D():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E3D)

    def lambda_E4B():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_E4B)

    def lambda_E59():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_E59)

    def lambda_E67():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E67)
    Sleep(400)
    OP_23(0xDA)
    OP_22(0xD4, 0x0, 0x64)
    Sleep(2600)

    def lambda_E94():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E94)
    Sleep(1500)

    def lambda_EB4():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EB4)
    Sleep(1000)

    def lambda_ED4():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_ED4)
    Sleep(1000)

    def lambda_EF4():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_EF4)
    WaitChrThread(0x12, 0x1)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    PlayEffect(0x0, 0x0, 0x12, 0, -180, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_DC()

    ChrTalk(    #13
        0x101,
        "#1006F#5PAll right, we've arrived.\x02",
    )

    CloseMessageWindow()

    def lambda_F7D():
        OP_6D(-8500, -5850, -29870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F7D)

    def lambda_F95():
        OP_67(0, 7820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F95)

    def lambda_FAD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FAD)

    def lambda_FBD():
        OP_6B(3310, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_FBD)
    OP_43(0x109, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(500)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_82(0x0, 0x2)

    ChrTalk(    #14
        0x101,
        (
            "#1002F#5PI don't see anyone around,\x01",
            "but, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1063F#6PYeah, nobody let your guard down.\x02\x03",

            "First order of business, I think,\x01",
            "is giving that building ahead\x01",
            "a scouting out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114B")

    ChrTalk(    #16
        0x108,
        (
            "#074F#6PLet us not forget who our enemies are.\x02\x03",

            "#072FIf we feel we are in danger, we should\x01",
            "not hesitate to retreat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1393")

    label("loc_114B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DD")

    ChrTalk(    #17
        0x103,
        (
            "#025F#6PWe shouldn't forget who our\x01",
            "enemies are, either.\x02\x03",

            "#022FIf we get in over our heads,\x01",
            "we shouldn't hesitate to leave.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1393")

    label("loc_11DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125B")

    ChrTalk(    #18
        0x106,
        (
            "#053F#6PDon't forget who we're fightin' here,\x01",
            "either.\x02\x03",

            "#050FThings go south, we should get out,\x01",
            "pronto.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1393")

    label("loc_125B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #19
        0x104,
        (
            "#032F#6PWe must not forget who our foes are.\x02\x03",

            "Should we encounter particular danger,\x01",
            "we should not hesitate to leave the\x01",
            "stage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1393")

    label("loc_12F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1393")

    ChrTalk(    #20
        0x105,
        (
            "#047F#6PI think it would be wise to remember who\x01",
            "we are up against, as well.\x02\x03",

            "#042FIf we encounter especially great danger,\x01",
            "we should retreat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1403")

    ChrTalk(    #21
        0x101,
        (
            "#1010F#5PYeah... You're right.\x02\x03",

            "#1006FTita. Do your best to keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        "#062F#6PI will!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1425")

    label("loc_1403")


    ChrTalk(    #23
        0x101,
        "#1006F#5PYeah... Good point!\x02",
    )

    CloseMessageWindow()

    label("loc_1425")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-9590, -5860, -29950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -9590, -5860, -29950, 270)
    SetChrPos(0x1, -9590, -5860, -29950, 270)
    SetChrPos(0x2, -9590, -5860, -29950, 270)
    SetChrPos(0x3, -9590, -5860, -29950, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x1C04)
    OP_28(0x97, 0x4, 0x10)
    OP_28(0x97, 0x4, 0x20)
    OP_28(0x98, 0x4, 0x2)
    OP_28(0x98, 0x4, 0x8)
    OP_28(0x98, 0x1, 0x1)
    OP_28(0x98, 0x1, 0x2)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_9EF end

    def Function_7_14E7(): pass

    label("Function_7_14E7")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDBF2, 0xFFFFDECC, 0xFFFF7E32, 0xBB8, 0x0)
    OP_96(0xFE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFD88C, 0xFFFFE886, 0xFFFF881E, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_14E7 end

    def Function_8_155D(): pass

    label("Function_8_155D")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_96(0xFE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFD922, 0xFFFFE8E0, 0xFFFF8EB8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_155D end

    def Function_9_15BF(): pass

    label("Function_9_15BF")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDF58, 0xFFFFDECC, 0xFFFF7E78, 0xBB8, 0x0)
    OP_96(0xFE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFE05C, 0xFFFFE8AE, 0xFFFF88BE, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_15BF end

    def Function_10_1635(): pass

    label("Function_10_1635")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_96(0xFE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFDF30, 0xFFFFE8EA, 0xFFFF8EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_10_1635 end

    def Function_11_1697(): pass

    label("Function_11_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182A")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        "\x07\x05The gate is sealed fast.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(-14880, 0, -4710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(26000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -14410, 0, -7130, 0)
    SetChrPos(0x109, -15440, 0, -7210, 0)
    SetChrPos(0xF8, -13390, 0, -6670, 0)
    SetChrPos(0xF9, -16400, 0, -6540, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BB")

    ChrTalk(    #25
        0x101,
        "#1007F#5PNo good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1067F#5PWe'll need to find another entrance.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1822")

    label("loc_17BB")


    ChrTalk(    #27
        0x101,
        "#1002F#5PNo good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1068F#5PLooks like we'll have to go in through\x01",
            "that other way we found.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1822")

    OP_A2(0x1C05)
    EventEnd(0x0)
    Jump("loc_1874")

    label("loc_182A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05The gate is sealed fast.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_1874")

    Return()

    # Function_11_1697 end

    def Function_12_1875(): pass

    label("Function_12_1875")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1875 end

    def Function_13_192C(): pass

    label("Function_13_192C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_192C end

    def Function_14_19ED(): pass

    label("Function_14_19ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A12")
    Call(0, 25)
    Call(0, 26)
    RemoveParty(0x0, 0xFF)

    label("loc_1A12")

    OP_6D(-7800, 15000, 15500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    OP_6D(-7430, 15000, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, -6230, 15000, 20660, 0)
    SetChrPos(0xF8, -6230, 15000, 20660, 0)
    SetChrPos(0xF9, -6230, 15000, 20660, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1200)
    OP_A1(0xE, 0x0)
    SetChrPos(0xE, -25800, 15150, 11920, 0)
    OP_72(0x1B, 0x4)
    OP_A1(0xF, 0x1B)
    SetChrPos(0xF, -25800, 15250, 11920, 0)
    OP_72(0x1C, 0x4)
    OP_72(0x1C, 0x20)
    OP_6F(0x1C, 1200)
    OP_A1(0x10, 0x1C)
    SetChrPos(0x10, -25800, 15150, 11920, 0)
    OP_48()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    OP_89(0x8, -25470, 18450, 9290, 90)
    OP_89(0x9, -23100, 18450, 9890, 90)
    OP_89(0xA, -23140, 18450, 8530, 90)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)
    OP_22(0x75, 0x1, 0x46)
    OP_79(0xC, 0x2)
    OP_7B()
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x6, 0x10)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x6)
    Sleep(200)
    OP_43(0x109, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0xF9, 0x1)
    Sleep(1000)

    ChrTalk(    #30
        0x109,
        "#1069F#5PAh, crap!\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (6, "loc_1C29"),
        (4, "loc_1C3D"),
        (2, "loc_1C4F"),
        (5, "loc_1C62"),
        (3, "loc_1C7B"),
        (7, "loc_1C8C"),
        (SWITCH_DEFAULT, "loc_1CA0"),
    )


    label("loc_1C29")


    ChrTalk(    #31
        0x107,
        "#065FAaaah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C3D")


    ChrTalk(    #32
        0x105,
        "#043FAah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C4F")


    ChrTalk(    #33
        0x103,
        "#523FErgh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C62")


    ChrTalk(    #34
        0x106,
        "#057FFrickin'...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C7B")


    ChrTalk(    #35
        0x104,
        "#039FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1C8C")


    ChrTalk(    #36
        0x108,
        "#077FBlast!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CA0")

    label("loc_1CA0")

    OP_DB()

    def lambda_1CA7():
        OP_6D(-18050, 24180, 6110, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1CA7)

    def lambda_1CBF():
        OP_67(0, 5750, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1CBF)

    def lambda_1CD7():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1CD7)

    def lambda_1CE7():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1CE7)

    def lambda_1CF7():
        OP_6B(1850, 3500)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_1CF7)
    Sleep(3000)
    SetChrPos(0x14, -18050, 24180, 6110, 0)

    def lambda_1D1D():

        label("loc_1D1D")

        OP_69(0x14, 0x0)
        OP_48()
        Jump("loc_1D1D")

    QueueWorkItem2(0x14, 2, lambda_1D1D)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 361)
    OP_70(0x0, 0x230)
    Sleep(500)
    OP_22(0x76, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_73(0x0)
    Sleep(500)
    OP_43(0x109, 0x2, 0x0, 0x14)
    OP_E8(0xDC, 0x5, 0x0, 0x0)
    LoadEffect(0x0, "map\\mp021_00.eff")
    PlayEffect(0x0, 0x0, 0xF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x75)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 561)
    OP_70(0x0, 0x28A)
    OP_B0(0x1C, 0x1E)
    OP_6F(0x1C, 561)
    OP_70(0x1C, 0x28A)

    def lambda_1DE5():
        OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1DE5)

    def lambda_1E00():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E00)

    def lambda_1E1B():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E1B)

    def lambda_1E36():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1E36)
    WaitChrThread(0xE, 0x1)

    def lambda_1E56():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1E56)

    def lambda_1E71():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1E71)

    def lambda_1E8C():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E8C)
    WaitChrThread(0xE, 0x1)

    def lambda_1EAC():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1EAC)

    def lambda_1EC7():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EC7)

    def lambda_1EE2():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1EE2)
    WaitChrThread(0xE, 0x1)

    def lambda_1F02():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F02)

    def lambda_1F1D():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1F1D)

    def lambda_1F38():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F38)
    WaitChrThread(0xE, 0x1)

    def lambda_1F58():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1F58)

    def lambda_1F73():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1F73)

    def lambda_1F8E():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F8E)
    WaitChrThread(0xE, 0x1)

    def lambda_1FAE():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1FAE)

    def lambda_1FC9():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1FC9)

    def lambda_1FE4():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1FE4)
    WaitChrThread(0xE, 0x1)

    def lambda_2004():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2004)

    def lambda_201F():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_201F)

    def lambda_203A():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_203A)
    WaitChrThread(0xE, 0x1)
    OP_82(0x0, 0x2)
    OP_44(0x14, 0x2)
    OP_43(0xE, 0x3, 0x0, 0x10)
    OP_43(0xE, 0x2, 0x0, 0x16)

    def lambda_206F():
        OP_6D(-5580, 30000, 22960, 7000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_206F)

    def lambda_2087():
        OP_6C(95000, 7000)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_2087)

    def lambda_2097():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2097)

    def lambda_20B3():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_20B3)

    def lambda_20CF():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_20CF)
    OP_43(0x9, 0x0, 0x0, 0xF)
    Sleep(3000)
    OP_CA(0x1B, 0x1, 0x12C)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xF, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2116():
        OP_6D(16140, 40000, 5000, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_2116)

    def lambda_212E():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_212E)

    def lambda_213E():
        OP_67(0, 6750, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_213E)

    def lambda_2156():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2156)

    def lambda_216C():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_216C)

    def lambda_2182():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2182)
    Sleep(500)

    def lambda_219D():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_219D)

    def lambda_21B3():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21B3)

    def lambda_21C9():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21C9)
    Sleep(500)

    def lambda_21E4():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21E4)

    def lambda_21FA():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21FA)

    def lambda_2210():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2210)
    Sleep(500)

    def lambda_222B():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_222B)

    def lambda_2241():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2241)

    def lambda_2257():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2257)
    OP_43(0xE, 0x3, 0x0, 0x17)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_E8(0xE8, 0x3, 0x0, 0x0)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_19ED end

    def Function_15_2297(): pass

    label("Function_15_2297")

    Sleep(1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 4)
    Sleep(50)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 4)
    Sleep(50)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 4)
    Sleep(1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 3)
    Sleep(50)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 3)
    Sleep(50)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 3)
    Return()

    # Function_15_2297 end

    def Function_16_22F2(): pass

    label("Function_16_22F2")

    OP_73(0x0)
    OP_73(0x1C)
    OP_6F(0x0, 651)
    OP_70(0x0, 0x2A8)
    OP_6F(0x1C, 651)
    OP_70(0x1C, 0x2A8)
    OP_73(0x0)
    OP_73(0x1C)
    OP_71(0x0, 0x20)
    OP_71(0x1C, 0x20)
    OP_6F(0x0, 680)
    OP_70(0x0, 0x30C)
    OP_6F(0x1C, 680)
    OP_70(0x1C, 0x30C)
    Return()

    # Function_16_22F2 end

    def Function_17_2341(): pass

    label("Function_17_2341")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDD82, 0x3A98, 0x3B10, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_17_2341 end

    def Function_18_2388(): pass

    label("Function_18_2388")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE0AC, 0x3A98, 0x3656, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23DE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_241C")

    label("loc_23DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2405")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_241C")

    label("loc_2405")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_241C")

    Return()

    # Function_18_2388 end

    def Function_19_241D(): pass

    label("Function_19_241D")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE084, 0x3A98, 0x3F84, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2478")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_24B6")

    label("loc_2478")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_249F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_24B6")

    label("loc_249F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_24B6")

    Return()

    # Function_19_241D end

    def Function_20_24B7(): pass

    label("Function_20_24B7")

    Sleep(500)

    def lambda_24C2():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_24C2)
    Sleep(100)

    def lambda_24E2():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_24E2)
    Sleep(100)

    def lambda_2502():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2502)
    Return()

    # Function_20_24B7 end

    def Function_21_2518(): pass

    label("Function_21_2518")

    Sleep(2000)

    def lambda_2523():
        OP_8E(0xFE, 0x1D4C, 0x3A98, 0x39B2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2523)
    Sleep(200)

    def lambda_2543():
        OP_8E(0xFE, 0x1A72, 0x3A98, 0x35FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_2543)
    Sleep(200)

    def lambda_2563():
        OP_8E(0xFE, 0x1626, 0x3A98, 0x32DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2563)
    WaitChrThread(0x109, 0x1)

    def lambda_2583():

        label("loc_2583")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_2583")

    QueueWorkItem2(0x109, 1, lambda_2583)
    WaitChrThread(0xF8, 0x1)

    def lambda_2599():

        label("loc_2599")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_2599")

    QueueWorkItem2(0xF8, 1, lambda_2599)
    WaitChrThread(0xF9, 0x1)

    def lambda_25AF():

        label("loc_25AF")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_25AF")

    QueueWorkItem2(0xF9, 1, lambda_25AF)
    Return()

    # Function_21_2518 end

    def Function_22_25BB(): pass

    label("Function_22_25BB")

    OP_73(0x0)
    OP_73(0x1C)
    OP_22(0x79, 0x0, 0x64)
    OP_6F(0x0, 651)
    OP_70(0x0, 0x2A8)
    OP_6F(0x1C, 651)
    OP_70(0x1C, 0x2A8)
    OP_73(0x0)
    OP_73(0x1C)
    OP_71(0x0, 0x20)
    OP_71(0x1C, 0x20)
    OP_6F(0x0, 680)
    OP_70(0x0, 0x30C)
    OP_6F(0x1C, 680)
    OP_70(0x1C, 0x30C)
    Return()

    # Function_22_25BB end

    def Function_23_260F(): pass

    label("Function_23_260F")

    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_23(0x79)
    Return()

    # Function_23_260F end

    def Function_24_2652(): pass

    label("Function_24_2652")

    EventBegin(0x0)
    OP_C4(0x0, 0x2)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266C")
    Call(0, 27)

    label("loc_266C")

    LoadEffect(0x1, "map\\\\mp064_01.eff")
    LoadEffect(0x2, "map\\\\mp065_01.eff")
    LoadEffect(0x3, "map\\\\mp064_00.eff")
    LoadEffect(0x4, "map\\\\mp065_00.eff")
    LoadEffect(0x5, "map\\\\mp021_00.eff")
    OP_71(0x1B, 0x4)
    OP_71(0x0, 0x4)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xD, -26000, 18450, 11200, 180)
    OP_A1(0x11, 0x2)
    OP_71(0x2, 0x20)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 501)
    OP_70(0x2, 0x208)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    OP_CF(0xA, 0x2, "Frame85__ren")
    SetChrSubChip(0xA, 1)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 21380, 20000, -38500, 0)
    OP_97(0x11, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)
    PlayEffect(0x1, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_28F6():
        OP_6D(-23510, 15200, 14990, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28F6)

    def lambda_290E():
        OP_67(0, 7830, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_290E)

    def lambda_2926():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2926)

    def lambda_2936():
        OP_6B(4200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2936)
    OP_22(0x113, 0x1, 0x32)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)
    OP_97(0x11, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0x11, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0x11, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0x11, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    PlayEffect(0x3, 0x6, 0x11, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x11, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x11, 0, 400)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x6, 0x11, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x7, 0x11, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x1E1)

    def lambda_2ACD():
        OP_8F(0xFE, 0xFFFF9B38, 0x4E20, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2ACD)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Sleep(500)
    OP_22(0x116, 0x0, 0x64)
    Sleep(500)
    WaitChrThread(0x11, 0x1)

    def lambda_2B13():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B13)
    Sleep(500)
    SetChrSubChip(0xA, 2)
    Sleep(500)
    SetChrSubChip(0xA, 3)
    Sleep(500)
    SetChrSubChip(0xA, 4)
    Sleep(500)
    SetChrSubChip(0xA, 5)
    WaitChrThread(0x11, 0x1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x11, -24960, 18450, 7270, 90)
    SetChrFlags(0x11, 0x1)
    ClearChrFlags(0x11, 0x80)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)

    def lambda_2BF2():
        OP_8F(0xFE, 0xFFFF9F20, 0x3BC4, 0x1C34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BF2)
    PlayEffect(0x5, 0x0, 0x11, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_70(0x2, 0x1CC)
    OP_0D()
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_82(0x0, 0x2)
    OP_82(0x6, 0x2)
    OP_82(0x7, 0x2)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xFA0, 0x1F4)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 421)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0xA, 0x1)
    Sleep(2000)
    OP_DB()

    ChrTalk(    #37
        0xA,
        (
            "#263FHooray! Those silly little flying machines\x01",
            "were no match for us!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_8C(0xA, 180, 0)
    OP_8C(0xA, 270, 400)
    Sleep(500)

    ChrTalk(    #38
        0xA,
        (
            "#1306FThanks, Pater-Mater! You go sleep for a\x01",
            "bit, okay?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(2000)
    SetChrPos(0x8, -12840, 14800, 9830, 270)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #39
        0x8,
        "Man's Voice",
        "#1PWelcome back, Renne.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2DB8():
        OP_6D(-20330, 15000, 9930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DB8)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_8C(0xA, 180, 400)

    def lambda_2DE1():
        OP_8E(0xFE, 0xFFFFC252, 0x3A98, 0x23D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DE1)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #40
        0xA,
        "#265F#6PLoewe!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_CF(0xA, 0x2, "Frame86__ren")
    OP_8C(0xA, 90, 0)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x2)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2E7D():
        OP_99(0xFE, 0x2, 0x5, 0x28A)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2E7D)
    OP_96(0xA, 0xFFFFAFC4, 0x3A98, 0x240E, 0x258, 0x9C4)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xA, 0x0)

    def lambda_2EC4():
        OP_99(0xFE, 0x6, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2EC4)
    WaitChrThread(0xA, 0x0)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 0)

    def lambda_2EE8():
        OP_8E(0xFE, 0xFFFFBCB2, 0x3A98, 0x2350, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2EE8)

    def lambda_2F03():
        OP_6D(-17430, 15000, 9790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F03)

    def lambda_2F1B():
        OP_67(0, 5290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F1B)

    def lambda_2F33():
        OP_6B(3420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F33)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #41
        0xA,
        (
            "#261F#6PI'm back, I'm back!\x02\x03",

            "I went and did that experiment,\x01",
            "just like you asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#123FI know. You did a very good job.\x02\x03",

            "You got a little creative with it, too.\x01",
            "A 'tea party'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#266F#6PIt's 'cause you told me not to kill\x01",
            "anyone this time.\x02\x03",

            "#1306FI had to do SOMETHING to make it\x01",
            "a little less boring, and I thought a\x01",
            "tea party would be lots of fun.\x02\x03",

            "And it was! We had tea and crumpets\x01",
            "and explosions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#124FHow...ladylike, Renne.\x02\x03",

            "#120FSo, how did the experiment itself go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#263F#6PI think it went okay.\x02\x03",

            "#260FThat mean guy from the church kinda\x01",
            "spoiled it with a nasty trick...\x02\x03",

            "But it was fine, otherwise! We can use\x01",
            "them in real combat if we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#124FVery good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#267F#6PI thought we couldn't make lots of\x01",
            "Gospels, though.\x02\x03",

            "How are we gonna use them as\x01",
            "weapons if we can't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#120FMass production of them isn't necessary.\x02\x03",

            "These tests are simply to determine the\x01",
            "full capabilities of the Gospels.\x02\x03",

            "We aren't trying to make a weapon out\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#264F#6PReally?\x02\x03",

            "#263FWell, whatever. Doesn't matter to me\x01",
            "either way.\x02\x03",

            "#265FHave you found Joshua yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#124FI think we have.\x02\x03",

            "#120FA number of the dolls we sent out to\x01",
            "act as a diversion were destroyed.\x02\x03",

            "It's very likely he's responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#262F#6PSo he's still hiding? Aww.\x02\x03",

            "I'm good at playing hide and seek, but\x01",
            "even I'm not as good as Joshua...\x02\x03",

            "#268FMmmmmm, I hate this!\x02\x03",

            "Why's he being so stubborn? Why can't\x01",
            "he just come back home to the society?\x01",
            "To us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#124FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#267F#6PIt's weird, too. The professor said it's\x01",
            "all Estelle's fault Joshua won't come\x01",
            "back.\x02\x03",

            "But she told me she's been looking for\x01",
            "Joshua, too!\x02\x03",

            "Why would she say that if she's keeping\x01",
            "Joshua from coming back to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#120F...Renne.\x02\x03",

            "I wouldn't be so quick to accept everything\x01",
            "the professor says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "#264F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#124FTruth can change depending on one's\x01",
            "perspective.\x02\x03",

            "Just as how people can see different\x01",
            "shapes on the same moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#265F#6PYou mean like how some people see\x01",
            "a face and others see a crab?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#120FThat's right.\x02\x03",

            "The professor's truth may be different\x01",
            "from your truth.\x02\x03",

            "You need to reach for your own truth\x01",
            "based on what you yourself see and\x01",
            "feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#265F#6PUm... Sounds confusing, but I think I get it.\x02\x03",

            "#261FI really like Estelle! I liked everyone, actually.\x01",
            "They're nice, and they gave me snacks.\x01",
            "Tita was fun to play with, too.\x02\x03",

            "I don't even feel like murdering them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "#124FVery good.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_8E(0x8, 0xFFFFBF8C, 0x3A98, 0x2328, 0x5DC, 0x0)
    Sleep(500)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x2, 0x3E8)
    OP_99(0x8, 0x3, 0x6, 0x3E8)
    OP_99(0x8, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #61
        0x8,
        "#123F#4PYou're a good girl, Renne.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "#261F#6PHeeheehee.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -7420, 15000, 13980, 270)
    SetChrPos(0xD, -7990, 15000, 14810, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)

    NpcTalk(    #63
        0x9,
        "Man's Voice",
        (
            "#1PIndeed, you're a very good girl, Renne.\x01",
            "And a very good worker!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 1500, 0x26, 0x27, 0x64, 0x0)
    Sleep(500)
    OP_63(0xA)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_3A25():
        OP_8E(0xFE, 0xFFFFBC9E, 0x3A98, 0x1EDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A25)

    def lambda_3A40():
        OP_8E(0xFE, 0xFFFFC3C4, 0x3A98, 0x215C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A40)
    Sleep(500)

    def lambda_3A60():
        OP_8E(0xFE, 0xFFFFC43C, 0x3A98, 0x2684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3A60)

    def lambda_3A7B():
        OP_6D(-16030, 15000, 9710, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A7B)

    def lambda_3A93():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A93)

    def lambda_3AA3():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AA3)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #64
        0xA,
        "#265F#6POh, hi, Professor...and Campanella!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "#853FHello there, Renne!\x02\x03",

            "#850FLooks like you had a good time in\x01",
            "Grancel, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#261F#6PYeah, kinda.\x02\x03",

            "#265FAwww, if I knew you were coming,\x01",
            "I would've invited you!\x02\x03",

            "It was a lot of fun, you know!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C79")

    ChrTalk(    #67
        0xD,
        (
            "#851FHaha. Now I feel bad that I missed it.\x02\x03",

            "I had to put on a nice little puppet show\x01",
            "for some lady bracers...\x02\x03",

            "It wasn't nearly as enjoyable as what\x01",
            "you did, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D28")

    label("loc_3C79")


    ChrTalk(    #68
        0xD,
        (
            "#851FHaha. Now I feel bad that I missed it.\x02\x03",

            "I had to put on a nice little puppet show\x01",
            "for a big burly bracer...\x02\x03",

            "It wasn't nearly as enjoyable as what\x01",
            "you did, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D28")


    ChrTalk(    #69
        0x9,
        (
            "#1154F#4PHaha... Perhaps you should have reserved\x01",
            "the better seat ahead of time, Campenella.\x02\x03",

            "#1151FBy the way, Renne...\x02\x03",

            "I couldn't help but overhear. You said\x01",
            "you're rather fond of Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "#263F#6PHaha, sure am.\x02\x03",

            "#260FShe wasn't nearly as nasty a person\x01",
            "as you said, Professor! She's nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#1150F#4PAh-ah, Renne! It's not nice to put words\x01",
            "in peoples' mouths. I never said she was\x01",
            "a bad person.\x02\x03",

            "If anything, I agree with you. She is both\x01",
            "a charming and fascinating young lady.\x02\x03",

            "#1154FI simply said that she's part of the reason\x01",
            "Joshua has yet to return to us.\x02\x03",

            "Wouldn't you agree, Loewe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#124F#6PI won't deny that she's part of the reason,\x01",
            "yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#1151F#4PWell, then, that should clear things up.\x01",
            "What do you think, Renne?\x02\x03",

            "Given the circumstances, shouldn't we\x01",
            "make Estelle one of our friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "#126FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#264F#6PMake Estelle one of our friends...?\x02\x03",

            "#263FYeah... Yeah! That sounds like a lot of fun!\x02\x03",

            "#265FShe's kind of on the weak side right now,\x01",
            "but if we teach her how to kill right, I bet\x01",
            "she'd be really powerful!\x02\x03",

            "And if Estelle joins us, Joshua will come\x01",
            "back, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#1151F#4PI think it's safe to assume as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xD,
        (
            "#851F#4PHahaha! Oh, Professor, I always knew\x01",
            "you had great taste. Delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#124F#6PThat's going a little too far with your\x01",
            "'jokes,' Professor.\x02\x03",

            "#121FRemember, 'All who serve the society\x01",
            "must do so of their own free will.'\x02\x03",

            "That is one of the core laws of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#1151F#4PYou need not remind me of the\x01",
            "Grandmaster's edicts, Loewe.\x02\x03",

            "Do you really think that I, an Anguis,\x01",
            "would break such a law?\x02\x03",

            "Neither you nor Joshua were forced\x01",
            "into anything, were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "#120F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "#1154F#4PIn any case, breaking her will would be\x01",
            "so dissatisfying.\x02\x03",

            "When she joins us...it will be entirely of\x01",
            "her own volition.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C4(0x1, 0x2)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2652 end

    def Function_25_4451(): pass

    label("Function_25_4451")

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
        (0, "loc_44CD"),
        (1, "loc_44D3"),
        (SWITCH_DEFAULT, "loc_44D9"),
    )


    label("loc_44CD")

    OP_A2(0x1200)
    Jump("loc_44D9")

    label("loc_44D3")

    OP_A2(0x1201)
    Jump("loc_44D9")

    label("loc_44D9")

    Return()

    # Function_25_4451 end

    def Function_26_44DA(): pass

    label("Function_26_44DA")

    ClearMapFlags(0x1)
    OP_6D(-136530, -6000, 47970, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_26_44DA end

    def Function_27_4537(): pass

    label("Function_27_4537")

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
        (0, "loc_45B0"),
        (1, "loc_45B6"),
        (SWITCH_DEFAULT, "loc_45BC"),
    )


    label("loc_45B0")

    OP_A2(0x1200)
    Jump("loc_45BC")

    label("loc_45B6")

    OP_A2(0x1201)
    Jump("loc_45BC")

    label("loc_45BC")

    Return()

    # Function_27_4537 end

    def Function_28_45BD(): pass

    label("Function_28_45BD")

    TalkBegin(0xFF)
    OP_22(0x6D, 0x0, 0x64)
    TalkEnd(0xFF)
    Return()

    # Function_28_45BD end

    def Function_29_45C9(): pass

    label("Function_29_45C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462F")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_47EA")

    label("loc_462F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47CF")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x6, 0x2)
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x32)
    OP_73(0x1D)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x7, "map\\\\mp027_01.eff")
    PlayEffect(0x7, 0x7, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x7, 0x2)
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_47CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_47E9")

    Return()

    label("loc_47EA")

    Return()

    # Function_29_45C9 end

    SaveToFile()

Try(main)
