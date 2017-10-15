from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0311   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Tita',                                 # 9
        'Kloe',                                 # 10
        'Scherazard',                           # 11
        'Tarot Card',                           # 12
        'Tarot Card',                           # 13
        'Tarot Card',                           # 14
        'Tarot Card',                           # 15
        'Tarot Card',                           # 16
        'Tarot Card',                           # 17
        'Glass',                                # 18
        'Photo',                                # 19
        'Lena',                                 # 20
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
        'ED6_DT06/CH20008 ._CH',             # 00
        'ED6_DT26/CH20230 ._CH',             # 01
        'ED6_DT26/CH20226 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT06/CH20133 ._CH',             # 04
        'ED6_DT26/CH20328 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT26/CH20338 ._CH',             # 07
        'ED6_DT26/CH20333 ._CH',             # 08
        'ED6_DT26/CH20315 ._CH',             # 09
        'ED6_DT26/CH20278 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT06/CH20008P._CP',             # 00
        'ED6_DT26/CH20230P._CP',             # 01
        'ED6_DT26/CH20226P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT06/CH20133P._CP',             # 04
        'ED6_DT26/CH20328P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT26/CH20338P._CP',             # 07
        'ED6_DT26/CH20333P._CP',             # 08
        'ED6_DT26/CH20315P._CP',             # 09
        'ED6_DT26/CH20278P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 589834,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 327686,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 786438,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E6,
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


    DeclEvent(
        X                   = 250,
        Y                   = 0,
        Z                   = -4510,
        Range               = 1700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x2BC,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 146350,
        TriggerZ            = 0,
        TriggerY            = 144640,
        TriggerRange        = 800,
        ActorX              = 147980,
        ActorZ              = 1200,
        ActorY              = 145500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72740,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 73030,
        ActorZ              = 1200,
        ActorY              = 72380,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8470,
        TriggerZ            = 0,
        TriggerY            = 67050,
        TriggerRange        = 1200,
        ActorX              = 8470,
        ActorZ              = 500,
        ActorY              = 67050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9830,
        TriggerZ            = 0,
        TriggerY            = 70700,
        TriggerRange        = 800,
        ActorX              = 9830,
        ActorZ              = 800,
        ActorY              = 70700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_332",          # 00, 0
        "Function_1_35B",          # 01, 1
        "Function_2_49F",          # 02, 2
        "Function_3_9CD",          # 03, 3
        "Function_4_C82",          # 04, 4
        "Function_5_F23",          # 05, 5
        "Function_6_1010",         # 06, 6
        "Function_7_1061",         # 07, 7
        "Function_8_32A4",         # 08, 8
    )


    def Function_0_332(): pass

    label("Function_0_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_343")
    OP_A3(0x10F0)
    Event(0, 2)
    Jump("loc_35A")

    label("loc_343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_35A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 8)

    label("loc_35A")

    Return()

    # Function_0_332 end

    def Function_1_35B(): pass

    label("Function_1_35B")

    OP_78(0x8C, 0x8C, 0xB4)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_79(0x0, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E")
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 148300, 400, 144950, 180)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 72990, 450, 72950, 270)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 1)), scpexpr(EXPR_END)), "loc_433")
    OP_6F(0x6, 10)
    OP_70(0x6, 0xA)
    Jump("loc_441")

    label("loc_433")

    OP_6F(0x6, 15)
    OP_70(0x6, 0xF)

    label("loc_441")

    OP_72(0x2, 0x10)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 2)), scpexpr(EXPR_END)), "loc_477")
    OP_6F(0x0, 12)
    OP_70(0x0, 0xC)
    Jump("loc_49E")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    OP_6F(0x0, 12)
    OP_70(0x0, 0xC)
    Jump("loc_49E")

    label("loc_490")

    OP_6F(0x0, 50)
    OP_70(0x0, 0x32)

    label("loc_49E")

    Return()

    # Function_1_35B end

    def Function_2_49F(): pass

    label("Function_2_49F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(144440, 0, 145300, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_BB(0x0, 0x1, 0x43)
    OP_BD()
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x40)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    SetChrPos(0x8, 148300, 400, 144950, 180)
    SetChrPos(0x101, 147700, 450, 145270, 180)
    ClearChrFlags(0x8, 0x80)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x0, 11)
    OP_70(0x0, 0xB)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_6D(148090, 0, 145410, 2500)
    OP_0D()
    OP_22(0x7, 0x0, 0x46)
    Sleep(1000)
    OP_62(0x101, 0xFFFFFDDA, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_6F(0x0, 11)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x7, 0x320)
    Sleep(200)

    ChrTalk(    #0
        0x101,
        "#1340F#6PMmmnnn...?\x02",
    )

    SetChrSubChip(0x101, 17)
    CloseMessageWindow()
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 23)
    Sleep(500)
    SetChrSubChip(0x101, 20)
    Sleep(500)
    SetChrSubChip(0x101, 23)
    OP_99(0x101, 0x12, 0x13, 0x320)
    SetChrSubChip(0x101, 17)

    ChrTalk(    #1
        0x101,
        (
            "#1335FWuzzat...?\x02\x03",

            "#451F...A door?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrPos(0x101, 146350, 0, 144660, 270)
    OP_6D(146930, 0, 144820, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x8,
        "#8P#40WNn...\x02",
    )

    CloseMessageWindow()
    OP_6F(0x0, 20)
    OP_70(0x0, 0x32)
    OP_99(0x8, 0x0, 0x9, 0x258)
    OP_8C(0x101, 90, 400)
    SetChrSubChip(0x8, 10)
    Sleep(300)

    ChrTalk(    #3
        0x8,
        (
            "#1252F#8P#40WHuuuh...\x02\x03",

            "Estelle...mmmm... What...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1336F#6POh! Sorry to wake you, Tita.\x02\x03",

            "#1333FI'm just gonna make sure I locked up\x01",
            "properly, okay?\x02\x03",

            "I'll be right back, so you just snuggle up\x01",
            "and go back to sleep, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1250F#8P#40WNnn'kay...\x02\x03",

            "#1251FC'back soon...'Stelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0xB, 0x13, 0x320)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#1336F#6PHeehee, she's so cute.\x02\x03",

            "#1331FMust...fight...cheek-pinching urges!\x02\x03",

            "#455F...Actually, that would be kind of cruel,\x01",
            "so let's not.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x23CF8, 0x0, 0x235AA, 0x1F4, 0x0)
    Sleep(500)
    OP_6F(0x0, 50)
    OP_70(0x0, 0xC)
    OP_73(0x0)
    Sleep(1000)
    OP_8F(0x101, 0x23BAE, 0x0, 0x23514, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    ClearChrFlags(0x101, 0x40)

    ChrTalk(    #7
        0x101,
        (
            "#1335F#6P(Okay, gotta calm down.\x01",
            "That was probably just Schera or Kloe.)\x02\x03",

            "(Best to double-check the beds\x01",
            "and locks, though.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1817)
    OP_28(0x90, 0x1, 0x400)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    EventEnd(0x0)
    Return()

    # Function_2_49F end

    def Function_3_9CD(): pass

    label("Function_3_9CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C23")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(72560, 0, 72180, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 72610, 0, 71390, 360)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x9,
        "#1240F#40WZzz...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#457FWell, she's out like a broken light.\x02\x03",

            "#1336FHaha. She really freaked out when\x01",
            "I told her she'd be sleeping in\x01",
            "Joshua's room.\x02\x03",

            "Really kind of adorable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        "#1241F#40WNnn...\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x0, 0x5, 0x5DC)
    Sleep(300)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #11
        0x9,
        (
            "#1241F#40WDean... Ev'rone...\x02\x03",

            "#40WWha shoul' I...\x02\x03",

            "#40W...\x02\x03",

            "#1240F#40WZzz...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0x101,
        "#1339FKloe...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x11BC0, 0x0, 0x1179C, 0x1F4, 0x0)
    Sleep(500)
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 15)
    OP_70(0x6, 0xA)
    OP_99(0x9, 0x5, 0x7, 0x3E8)
    OP_73(0x6)
    Sleep(1000)
    OP_8F(0x101, 0x11BA2, 0x0, 0x116DE, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        "#1337FWe'll both do our best, okay?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1819)
    EventEnd(0x0)
    Jump("loc_C81")

    label("loc_C23")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05Kloe's expression is peaceful as she sleeps.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_C81")

    Return()

    # Function_3_9CD end

    def Function_4_C82(): pass

    label("Function_4_C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05Tita looks like an angel as she sleeps.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_F22")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC9")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(147270, 0, 145070, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 146350, 0, 144680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x8,
        (
            "#1253F#8P#40WNnn...\x02\x03",

            "#40WPapa... Mama...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #17
        0x8,
        (
            "#1253F#8P#40WI'm...a good girl...\x02\x03",

            "#40WI've got...'Stelle 'n...'vryone...\x02\x03",

            "#40WSo...'m okay...\x02\x03",

            "#40W...\x02\x03",

            "#1251F#40WHeehee... Bwabwaha...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #18
        0x101,
        "#1339F#6PTita...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrFlags(0x101, 0x4)
    OP_8F(0x101, 0x23CF8, 0x0, 0x235AA, 0x1F4, 0x0)
    Sleep(500)
    OP_6F(0x0, 50)
    OP_70(0x0, 0xC)
    OP_73(0x0)
    Sleep(1000)
    OP_8F(0x101, 0x23BAE, 0x0, 0x23528, 0x1F4, 0x0)
    ClearChrFlags(0x101, 0x4)
    Sleep(500)

    ChrTalk(    #19
        0x101,
        (
            "#1342F#6PDon't you worry.\x01",
            "We're here for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x181A)
    EventEnd(0x0)
    Jump("loc_F22")

    label("loc_EC9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Tita looks like an angel as she sleeps.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_F22")

    Return()

    # Function_4_C82 end

    def Function_5_F23(): pass

    label("Function_5_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC7")
    OP_8C(0x101, 180, 0)

    ChrTalk(    #21
        0x101,
        "#453FHuh?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05The bed is still warm.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #23
        0x101,
        (
            "#1335FWhere on earth would Schera go\x01",
            "at this hour?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x181B)
    TalkEnd(0xFF)
    Jump("loc_100F")

    label("loc_FC7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05The bed is still warm.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_100F")

    Return()

    # Function_5_F23 end

    def Function_6_1010(): pass

    label("Function_6_1010")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_1010 end

    def Function_7_1061(): pass

    label("Function_7_1061")

    EventBegin(0x0)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, -8070, 200, 2290, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x11, -7800, 700, 1240, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xC, -8140, 730, 1400, 0)
    SetChrPos(0xD, -8640, 730, 1400, 0)
    SetChrPos(0xF, -8140, 730, 940, 0)
    SetChrPos(0x10, -8640, 730, 940, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    TurnDirection(0x101, 0x103, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_6D(-8070, 0, 2290, 3000)

    ChrTalk(    #26
        0xA,
        "#026F...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, 820, 0, -2480, 300)

    ChrTalk(    #27
        0x101,
        "#3PSchera?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_116C():
        OP_8E(0xFE, 0xFFFFEC50, 0x0, 0xFFFFFEE8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_116C)

    def lambda_1187():
        OP_6D(-6710, 0, 880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1187)
    SetChrSubChip(0xA, 1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #28
        0xA,
        "#023FOh... Estelle. Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#454FI, uh, heard a sound and got up\x01",
            "to check it out.\x02\x03",

            "I thought it might be you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "#020FIt was, I'm sorry.\x02\x03",

            "#021FBeing able to wake when you sense the\x01",
            "slightest change in your environment?\x01",
            "NOW you're acting like a proper bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1331FHeheh... Well, I dunno about that.\x01",
            "I think I'm just nervous.\x02\x03",

            "#1336FI've got a lot on my mind and\x01",
            "I feel kinda confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        "#524FI see...\x02",
    )

    CloseMessageWindow()

    def lambda_135B():
        OP_8E(0xFE, 0xFFFFE2D2, 0x0, 0xFFFFFE52, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_135B)

    def lambda_1376():
        OP_6D(-7650, 0, 970, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1376)
    Sleep(500)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x101, 0x4)

    def lambda_13A2():
        OP_96(0xFE, 0xFFFFDFEE, 0xC8, 0xFFFFFDBC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13A2)
    OP_8C(0x101, 0, 1000)
    WaitChrThread(0x101, 0x1)
    SetChrChipByIndex(0x101, 5)
    Sleep(1000)

    ChrTalk(    #33
        0x101,
        (
            "#1333F#4PSo, hey!\x01",
            "Are the cards showing you anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        "#027F#6PLet's take a look.\x02",
    )

    CloseMessageWindow()

    def lambda_1431():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1431)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    OP_99(0xA, 0x8, 0xA, 0x190)
    Sleep(500)

    ChrTalk(    #35
        0xA,
        (
            "#026F#6PThe inverted Emperor.\x02\x03",

            "Mercy. Empathy. Trust. Difficulty. Inexperience.\x01",
            "And...uncertainty regarding your enemies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1335F#4PUm... Wow. I don't really get how one card\x01",
            "can have THAT much meaning.\x02\x03",

            "#455FAnd what do you mean by 'uncertainty regarding my\x01",
            "enemies'?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 10)
    SetChrSubChip(0xC, 12)

    def lambda_157B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_157B)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 3)
    Sleep(500)

    ChrTalk(    #37
        0xA,
        (
            "#026F#6PMmm...\x02\x03",

            "#524FI didn't draw that card for you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#453F#4PEr.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#020F#6PIt sounds like you think some\x01",
            "of that does apply to you, though.\x02\x03",

            "This wouldn't have anything to do with\x01",
            "what you spoke with Mr. Burns about,\x01",
            "would it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1340F#4POh, um...\x02\x03",

            "#452F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#524F#6PI'm sorry, Estelle.\x01",
            "I'm really not trying to rush you.\x02\x03",

            "I do think getting it off your chest would help,\x01",
            "though, once you're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#452F#4P...\x02\x03",

            "#1340FSchera...do you have a few minutes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#027F#6PHoney, you're practically my little sister.\x02\x03",

            "You have all my minutes.\x01",
            "That's what older sisters are for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1339F#4PAww, Schera...\x02\x03",

            "#452FUm... Could you take a look at this?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05Estelle handed Dorothy's photograph to Schera.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #46
        0xA,
        "#023F#6PHmm? A photo?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    SetChrSubChip(0xA, 9)
    Sleep(1000)

    ChrTalk(    #47
        0xA,
        (
            "#023F#6P...\x01",
            "What...in...\x02\x03",

            "#026FWell, this...answers one question,\x01",
            "at least.\x02\x03",

            "#524FI can see why you've been\x01",
            "so distracted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#455F#4PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#027F#6PI bet he's with them as a front, of sorts,\x01",
            "for whatever clandestine work he's doing.\x02\x03",

            "Yes, I see. With them he can do the sorts\x01",
            "of things he couldn't easily do if he\x01",
            "was having to maintain a bracer's face.\x02\x03",

            "Hmm... I wonder what his goals are,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1335F#4PUh. Schera?\x01",
            "Aren't you just a little bit surprised?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0xA,
        (
            "#026F#6PTo be completely honest?\x01",
            "I was expecting far worse.\x02\x03",

            "#524FI remember hearing that the soldiers attacked\x01",
            "during the bandit raid were simply knocked\x01",
            "unconscious. Not killed.\x02\x03",

            "I'm certain Joshua's skill had a lot to\x01",
            "do with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1339F#4PYeah, that's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#025F#6PGetting caught on film was a bit\x01",
            "careless of him, though.\x02\x03",

            "I should demand better of a student of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1336F#4PWell, to be fair, it was Dorothy who\x01",
            "took it.\x02\x03",

            "Sometimes I swear it's like the hand of\x01",
            "the Goddess is guiding her pictures\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "#027F#6PShe DOES seem possessed of\x01",
            "the camera of miracles, yes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#452F#4PSo...Schera?\x02\x03",

            "Should I...hand this photo over to Aina?\x01",
            "Or Elnan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        (
            "#026F#6PMm. As a rule, bracers have only one obligation.\x02\x03",

            "#020FThat is, to come to the aid of civilians\x01",
            "who are unjustly harmed, and to prevent\x01",
            "such acts whenever possible.\x02\x03",

            "So, let me ask you: is Joshua a danger\x01",
            "to the citizenry? Will he work with the\x01",
            "Capuas to bring terror to Liberl's skies?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1330F#4PWh- NO! He'd NEVER do something like that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#027F#6PThen you have exactly zero obligation\x01",
            "to report anything.\x02\x03",

            "And I see no reason to say anything, either,\x01",
            "as I, too, am confident Joshua presents\x01",
            "no danger.\x02\x03",

            "Ultimately, it comes down to whether you\x01",
            "believe in Joshua or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#452F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#524F#6POr...is that actually an on-going question?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#452F#4PI do believe in him... I DO trust him.\x02\x03",

            "#455FI'm just so worried.\x02\x03",

            "He's out there, somewhere, and I don't\x01",
            "know where, and he's got those cold,\x01",
            "unfeeling eyes...\x02\x03",

            "He looks like he doesn't care what\x01",
            "happens to himself.\x02\x03",

            "#1341FI almost want to talk to Dad, and try to\x01",
            "get Joshua put into protective custody\x01",
            "or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "#023F#6PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1340F#4PBut then...what did I do all of this for?\x02\x03",

            "Wasn't this all because I wanted to bring\x01",
            "Joshua back myself? But, then...then,\x01",
            "maybe I'm just being a selfish little girl?\x02\x03",

            "#455FAnd...ow, yeah, once I get this far in,\x01",
            "the headache sets in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        (
            "#026F#6PI see.\x02\x03",

            "#524FI wouldn't worry, Estelle.\x02\x03",

            "You're coming to an answer in your own way.\x01",
            "I wouldn't fret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1340F#4PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "#020F#6PFrom the sound of it, you have a fairly\x01",
            "good grasp of your feelings on this.\x02\x03",

            "All you've lost sight of is what you want\x01",
            "to actually DO.\x02\x03",

            "You'll find the answer you need if you\x01",
            "take it one step at a time. I know you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1339F#4PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#027F#6PYou already seem a lot calmer now than\x01",
            "when you got off the airship.\x02\x03",

            "You certainly seem to know what you need\x01",
            "to do right now, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1336F#4PYeah, that's true.\x02\x03",

            "#454FWhen I heard that Elissa's mom and Luke\x01",
            "had both collapsed...\x02\x03",

            "I actually felt kinda motivated, you know?\x01",
            "Like, 'I can't sit around in my own little\x01",
            "rain cloud!'\x02\x03",

            "My own problems seemed to fade into\x01",
            "the distance a little after that.\x02\x03",

            "#1335F...Oh, great, now I think I sound like\x01",
            "a vapid, flighty pom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#027F#6PI don't know about that, though you're\x01",
            "definitely cute enough to be a pom.\x02\x03",

            "I do think you should keep moving forward.\x02\x03",

            "You've always solved your problems best\x01",
            "by putting one foot in front of the other,\x01",
            "without stopping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#455F#4PThanks, Schera, NOW I sound like\x01",
            "a charging rhinocider, not a pom.\x02\x03",

            "#1337FStill...really, thanks.\x02\x03",

            "I think...I kinda see the answer in the\x01",
            "distance, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#027F#6PI hardly did anything special.\x02\x03",

            "#021FAnyway... Joshua's doing pretty well for\x01",
            "himself, now isn't he?\x02\x03",

            "I never thought he and that bandit girl\x01",
            "would be a match, but they are cute\x01",
            "together! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#455F#4POh, great, now YOU'RE getting in on that...\x02\x03",

            "#459FWe don't know if there's anything going\x01",
            "on there, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#027F#6POoooooh? You think not?\x02\x03",

            "She IS a very strong-willed, boyish sort\x01",
            "of girl.\x02\x03",

            "And yet, beneath that, there is a sort of\x01",
            "deeply-buried sense of refinement to\x01",
            "her...\x02\x03",

            "#021FThat sounds like just the kind of girl\x01",
            "Joshua would snuggle tenderly with. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#459F#4PSchera. Did you become a perverted old man\x01",
            "while I wasn't looking or something? The fog\x01",
            "seeped into your brain, didn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "#027F#6PAs they overcome perils together,\x01",
            "the soil will become fertile with affection...\x02\x03",

            "#023FOh, but, Estelle! Why are you worried?\x02\x03",

            "#021FIf someone steals Joshua from you,\x01",
            "all you have to do is take back your man!\x01",
            "Bright versus Capua! A struggle to the death!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1338F#4P...Note to self, never talk to Schera about\x01",
            "anything in the future. At all. Ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "#021F#6PHaha! I'm joking, Estelle. Really.\x02\x03",

            "#526FStill, though, if you want to worry about\x01",
            "Joshua, that would be the thing I'd worry\x01",
            "about more, in your shoes.\x02\x03",

            "You two ARE at that age, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#455F#4POh, believe me, I'm plenty worried\x01",
            "on that front, too.\x02\x03",

            "#1334F(Like...there's Kloe, for starters.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        "#023F#6PHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1336F#4PEr, nothing. I totally said nothing!\x02\x03",

            "#1331FAnyway, even despite all that, I'm actually...\x01",
            "a lot calmer now. I think I'm going to get\x01",
            "back to bed.\x02\x03",

            "Are you going to stay up, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "#524F#6PNo, I won't be too long in getting back\x01",
            "to bed myself.\x02\x03",

            "Agate and the others had a point about\x01",
            "getting some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#453F#4PThat's true...\x02\x03",

            "#1340F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        "#020F#6PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1335F#4PSchera...is there something YOU'RE\x01",
            "worried about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "#026F#6PAh... Well, a little, perhaps.\x02\x03",

            "#020FGive me a day or two, Estelle.\x01",
            "We can talk about it then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#455F#4PWell, okay.\x02\x03",

            "#454FI promise I won't worry about it\x01",
            "too much, then.\x02\x03",

            "Just...keep your own advice in\x01",
            "mind, okay? Don't drive yourself\x01",
            "crazy or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "#021F#6PDon't worry.\x02\x03",

            "#027FI've got a bothersome little sister to\x01",
            "handle all the crazy in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#455F#4PAck...\x02\x03",

            "#1337FWell...goodnight, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "#021F#6PGood night, Estelle.\x02",
    )

    CloseMessageWindow()

    def lambda_30B1():
        OP_96(0xFE, 0xFFFFE2BE, 0x0, 0xFFFFFD94, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B1)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 90, 1000)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    SetChrSubChip(0xA, 1)

    def lambda_30EF():
        OP_8E(0x101, 0xBAE, 0x0, 0xFFFFF5E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30EF)

    def lambda_310A():
        OP_6D(-5170, 0, -30, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_310A)
    WaitChrThread(0x101, 0x1)

    def lambda_3127():
        OP_6D(-7600, 0, 2870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3127)

    def lambda_313F():
        OP_6E(245, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_313F)
    Sleep(1000)
    SetChrSubChip(0xA, 0)
    WaitChrThread(0x101, 0x3)

    def lambda_315E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_315E)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 4)
    OP_99(0xA, 0x8, 0xA, 0x190)
    Sleep(500)

    ChrTalk(    #92
        0xA,
        (
            "#522F#6PThe inverted Emperor.\x02\x03",

            "Mercy. Empathy. Trust. Difficulty. Inexperience.\x01",
            "And...uncertainty regarding your enemies.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 11)
    Sleep(1000)

    ChrTalk(    #93
        0xA,
        (
            "#026F#6PLosing sight of what you want to do...\x02\x03",

            "#524FHeheh... I wonder who I was really\x01",
            "talking about.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0x1770)
    OP_0D()
    Sleep(3000)
    OP_22(0x118, 0x0, 0x28)
    Sleep(3000)
    OP_21()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1061 end

    def Function_8_32A4(): pass

    label("Function_8_32A4")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 147700, 350, 145310, 320)
    SetChrChipByIndex(0x101, 7)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x2)
    SetChrPos(0x13, 147960, 100, 145220, 320)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 8)
    ClearChrFlags(0x13, 0x80)
    OP_6D(145670, 400, 145530, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_71(0x7, 0x0)
    OP_71(0x7, 0x4)
    OP_72(0x0, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x7, 0x20)
    OP_6F(0x0, 15)
    OP_70(0x0, 0xF)
    FadeToBright(1000, 0)
    OP_6D(148490, 400, 145420, 4000)
    OP_62(0x101, 0xFFFFFED4, 1300, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(1000)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(1000)
    OP_DC()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x07\x05And at night, falling asleep embraced by a mother's\x01",
            "warmth...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 65535)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "\x07\x05Days of happiness, with no sight or knowledge of\x01",
            "sadness or loneliness...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #96
        "\x07\x05It was the closest one could come to bliss.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0300   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_8_32A4 end

    SaveToFile()

Try(main)
