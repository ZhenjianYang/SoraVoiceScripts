from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1311   ._SN',
        MapName             = 'Bose',
        Location            = 'T1311.x',
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
        'Warrant Officer Serose',               # 9
        'Private Usher',                        # 10
        'CWO Zelste',                           # 11
        'Anelace',                              # 12
        'Private Egel',                         # 13
        'Private Mikey',                        # 14
        'Private Cutinger',                     # 15
        'Dish',                                 # 16
        'Dish',                                 # 17
        'Coffee',                               # 18
        'Coffee',                               # 19
    )

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
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

    DeclEntryPoint(
        Unknown_00              = 48000,
        Unknown_04              = -3000,
        Unknown_08              = 27000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 6000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 280,
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
        'ED6_DT07/CH01300 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT06/CH20021 ._CH',             # 06
        'ED6_DT06/CH20053 ._CH',             # 07
        'ED6_DT06/CH20053 ._CH',             # 08
        'ED6_DT06/CH20062 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01300P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT06/CH20021P._CP',             # 06
        'ED6_DT06/CH20053P._CP',             # 07
        'ED6_DT06/CH20053P._CP',             # 08
        'ED6_DT06/CH20062P._CP',             # 09
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 22490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 22000,
        Z                   = 0,
        Y                   = 9500,
        Direction           = 27,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 81840,
        Z                   = 0,
        Y                   = 13080,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 21900,
        Z                   = 0,
        Y                   = 22100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 19990,
        Z                   = 0,
        Y                   = 7950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 76700,
        Z                   = 0,
        Y                   = 7590,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 25000,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65541,
        ChipIndex           = 0x5,
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
        Unknown3            = 65541,
        ChipIndex           = 0x5,
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
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
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
        Unknown3            = 1572869,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 21950,
        TriggerZ            = 0,
        TriggerY            = 22540,
        TriggerRange        = 400,
        ActorX              = 19990,
        ActorZ              = 1500,
        ActorY              = 22490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_442",          # 01, 1
        "Function_2_4B9",          # 02, 2
        "Function_3_4CF",          # 03, 3
        "Function_4_4D4",          # 04, 4
        "Function_5_15A1",         # 05, 5
        "Function_6_1CD2",         # 06, 6
        "Function_7_279F",         # 07, 7
        "Function_8_2BCC",         # 08, 8
        "Function_9_2C2C",         # 09, 9
        "Function_10_2E92",        # 0A, 10
        "Function_11_36C2",        # 0B, 11
        "Function_12_4F91",        # 0C, 12
        "Function_13_52F3",        # 0D, 13
        "Function_14_56C9",        # 0E, 14
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_352")
    OP_71(0x2, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_37A")
    OP_71(0x2, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_393")
    OP_71(0x2, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3AC")
    OP_71(0x2, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_3C0")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    Jump("loc_3EF")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3D9")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3EF")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_3FD")
    OP_A3(0x3FC)
    Event(0, 11)

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_414")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_422")
    OP_A3(0x3FB)
    Event(0, 13)

    label("loc_422")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_42E"),
        (SWITCH_DEFAULT, "loc_441"),
    )


    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E")
    Event(0, 11)

    label("loc_43E")

    Jump("loc_441")

    label("loc_441")

    Return()

    # Function_0_32A end

    def Function_1_442(): pass

    label("Function_1_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_END)), "loc_46F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_64(0x0, 0x1)

    label("loc_46F")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_442 end

    def Function_2_4B9(): pass

    label("Function_2_4B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4CE")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_4B9")

    label("loc_4CE")

    Return()

    # Function_2_4B9 end

    def Function_3_4CF(): pass

    label("Function_3_4CF")

    Call(0, 4)
    Return()

    # Function_3_4CF end

    def Function_4_4D4(): pass

    label("Function_4_4D4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_580")

    ChrTalk(    #0
        0x8,
        (
            "It looks like we had some fish\x01",
            "delivered from Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I think I'll cook something a bit lavish\x01",
            "this evening to help everyone\x01",
            "recharge their batteries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_62A")

    ChrTalk(    #2
        0x8,
        (
            "We haven't seen any of those\x01",
            "monsters after they attacked\x01",
            "us the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Any way I look at it, it just seems\x01",
            "like they weren't from around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_62A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_6B4")

    ChrTalk(    #4
        0x8,
        (
            "Oh, if it isn't the bracers from\x01",
            "the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "What can we help you with today?\x01",
            "Do you have some business up here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_10A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C")
    ClearMapFlags(0x1)
    OP_69(0x8, 0x3E8)

    ChrTalk(    #6
        0x101,
        "#000FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#010FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "Good morning to yourselves as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "Thanks for helping us out the way\x01",
            "you did last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#000FTee hee. We didn't do much.\x02\x03",

            "How about you guys? Did you\x01",
            "run into any trouble patrolling\x01",
            "the area after that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Nope. Everything was fine, like\x01",
            "on any normal night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "I tell you what though,\x01",
            "that was rather strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#000FStrange? What was?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "You know how the lights along the roads\x01",
            "and at the checkpoints have the ability\x01",
            "to ward off monsters, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Well, even if there were monsters that\x01",
            "approached the checkpoint, they wouldn't\x01",
            "be any more than two or three in number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "So yesterday was the first time\x01",
            "I've ever seen them come in a\x01",
            "large pack like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#010FYeah, that is rather strange, now\x01",
            "that you mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "Then again, these monsters were\x01",
            "small change when compared with\x01",
            "the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "We should probably just consider\x01",
            "it good training in protecting our\x01",
            "base of operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#000FI-Is that really the issue here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "For us, that's all we're really\x01",
            "concerned about. Protecting\x01",
            "the checkpoint is paramount.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "We'll leave figuring out what the\x01",
            "monsters were thinking up to\x01",
            "you bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "Now, getting back on topic...\x01",
            "You guys are heading over to\x01",
            "Ruan, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "Are you ready to fill out the\x01",
            "paperwork for your gate pass?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#010FYes, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05Filled out the paperwork to enter the\x01",
            "Ruan region.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #27
        0x8,
        (
            "Well, that's that. It looks like\x01",
            "you're done here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "Enjoy your travels in Ruan.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    OP_70(0x2, 0x64)
    OP_6D(23765, 0, 25450, 2000)

    ChrTalk(    #29
        0x8,
        (
            "Welcome to the Ruan region!\x01",
            "Blue oceans and white magnolias\x01",
            "await you!\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x8, 0x3E8)
    TurnDirection(0x8, 0x0, 400)

    ChrTalk(    #30
        0x8,
        (
            "That reminds me, you'll be\x01",
            "heading to Ruan City, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Well, just make sure to report to\x01",
            "the guild concerning the incident\x01",
            "that happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "There will be a payment there\x01",
            "from the army for helping us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#000FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "Yeah, but you're going to have\x01",
            "to divvy your spoils with Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "All right, enjoy yourselves and\x01",
            "good luck in your endeavor to\x01",
            "become senior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#000FThanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#010FWe really appreciate everything\x01",
            "you've done for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x407)
    OP_28(0x11, 0x4, 0x40)
    OP_28(0x13, 0x4, 0x40)
    NewScene("ED6_DT01/T1300   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_109E")

    label("loc_F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1011")
    OP_A2(0x0)

    ChrTalk(    #38
        0x8,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "Make sure you report to the guild\x01",
            "concerning the incident that\x01",
            "happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "Take care and enjoy your trip\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109E")

    label("loc_1011")


    ChrTalk(    #41
        0x8,
        (
            "Make sure you report to the guild\x01",
            "concerning the incident that\x01",
            "happened up here last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "Take care and enjoy your trip\x01",
            "to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109E")

    Jump("loc_159D")

    label("loc_10A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_110F")

    ChrTalk(    #43
        0x8,
        (
            "Huh? What are you kids doing\x01",
            "hiking at a time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "It's pretty cold out there, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_110F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1312")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
    OP_A2(0x0)

    ChrTalk(    #45
        0x8,
        (
            "No matter how experienced of a traveler\x01",
            "you are, you shouldn't be hiking around\x01",
            "in a place like this at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "The trail is steep and there are\x01",
            "a lot of monsters out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "That reminds me, as strange as it sounds,\x01",
            "we've seen a lot of organized packs of\x01",
            "monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "I've never seen anything like it\x01",
            "until now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_130F")

    label("loc_1275")


    ChrTalk(    #49
        0x8,
        (
            "That reminds me, as strange as it sounds,\x01",
            "we've seen a lot of organized packs of\x01",
            "monsters recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "I've never seen anything like it\x01",
            "until now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130F")

    Jump("loc_159D")

    label("loc_1312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_13B3")

    ChrTalk(    #51
        0x8,
        (
            "All soldiers are allotted at least\x01",
            "six hours of sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "That's because they can't fight\x01",
            "to their full ability if they have\x01",
            "insufficient rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_14CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1461")
    OP_A2(0x0)

    ChrTalk(    #53
        0x8,
        (
            "Despite my appearance as a soldier\x01",
            "in the Royal Army, I love to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "I often get the chief's permission\x01",
            "so I can cook here at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CB")

    label("loc_1461")


    ChrTalk(    #55
        0x8,
        (
            "Just so you know, the traveler's\x01",
            "quarters are over there so feel free\x01",
            "to use them whenever you need.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14CB")

    Jump("loc_159D")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_159D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157C")
    OP_A2(0x0)

    ChrTalk(    #56
        0x8,
        (
            "Despite my appearance as a soldier\x01",
            "in the Royal Army, I love to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "I often get the chief's permission\x01",
            "so I can cook here at the checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159D")

    label("loc_157C")


    ChrTalk(    #58
        0x8,
        "So are you heading to Ruan?\x02",
    )

    CloseMessageWindow()

    label("loc_159D")

    TalkEnd(0x8)
    Return()

    # Function_4_4D4 end

    def Function_5_15A1(): pass

    label("Function_5_15A1")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_16E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165E")
    OP_A2(0x2)

    ChrTalk(    #59
        0xFE,
        "It was my day to cook today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Then the warrant officer came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DF")

    label("loc_165E")


    ChrTalk(    #62
        0xFE,
        (
            "The warrant officer just came and told\x01",
            "me to let him cook in my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "That guy really likes cooking,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DF")

    Jump("loc_1CCE")

    label("loc_16E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_17E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178B")
    OP_A2(0x2)

    ChrTalk(    #64
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the sky bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Well, I guess it's better than\x01",
            "an endless string of events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17DE")

    label("loc_178B")


    ChrTalk(    #66
        0xFE,
        (
            "The Bose region has been rather\x01",
            "quiet since the sky bandits were\x01",
            "apprehended.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DE")

    Jump("loc_1CCE")

    label("loc_17E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1875")

    ChrTalk(    #67
        0xFE,
        (
            "Those monsters the other day were\x01",
            "a lot stronger than I imagined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Which means I'll have to train a\x01",
            "lot harder than I have been.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_1911")

    ChrTalk(    #69
        0xFE,
        (
            "The attack on the checkpoint\x01",
            "last night was good practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "I guess I should be better prepared\x01",
            "for an emergency--both in body and\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(    #71
        0xFE,
        (
            "With the border garrison's investigation\x01",
            "carrying on this long, I'm sure they're\x01",
            "tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I hope they'll find some new leads\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_19A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(    #73
        0xFE,
        (
            "This area is covered with mountains\x01",
            "and filled with monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Not to mention there are big,\x01",
            "vicious ones roaming around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Training is essential to being a\x01",
            "soldier here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")
    OP_A2(0x2)

    ChrTalk(    #76
        0xFE,
        (
            "This is due to the rugged terrain\x01",
            "which covers the Krone Range.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "The sky bandits may just be\x01",
            "hiding around here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1B02")


    ChrTalk(    #78
        0xFE,
        (
            "Which is why the border garrison\x01",
            "has already investigated this area\x01",
            "on multiple occasions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B62")

    Jump("loc_1CCE")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1CCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C42")
    OP_A2(0x2)

    ChrTalk(    #79
        0xFE,
        (
            "On a normal day, we almost get\x01",
            "no travelers coming through the\x01",
            "steep pass here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "But now, with the airliners being stopped,\x01",
            "those in a hurry to get to Ruan or Bose\x01",
            "have been making the trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CCE")

    label("loc_1C42")


    ChrTalk(    #81
        0xFE,
        (
            "That said, I would tell anybody\x01",
            "to avoid trying to come through\x01",
            "this pass at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "It's way too dangerous for a\x01",
            "normal traveler.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCE")

    TalkEnd(0x9)
    Return()

    # Function_5_15A1 end

    def Function_6_1CD2(): pass

    label("Function_6_1CD2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1E")
    OP_A2(0x0)

    ChrTalk(    #83
        0xFE,
        (
            "These checkpoints around Liberl were useful in\x01",
            "the war 10 years ago to separate the various\x01",
            "troops of the Imperial Army from each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "And even today they're still used\x01",
            "as strategic points by the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "That is why we, as garrisons who\x01",
            "oversee these places, can never\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F06")

    label("loc_1E1E")


    ChrTalk(    #86
        0xFE,
        (
            "These checkpoints around Liberl were useful in\x01",
            "the war 10 years ago to separate the various\x01",
            "troops of the Imperial Army from each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "That is why we, as garrisons who\x01",
            "oversee these places, can never\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F06")

    Jump("loc_279B")

    label("loc_1F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_20A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2013")
    OP_A2(0x0)

    ChrTalk(    #88
        0xFE,
        (
            "Soldiers have been stationed at\x01",
            "each checkpoint to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "But occasionally we have to rescue\x01",
            "hikers here in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "That's because we have a lot of hikers\x01",
            "who find themselves in trouble here\x01",
            "along the Krone Range.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20A1")

    label("loc_2013")


    ChrTalk(    #91
        0xFE,
        (
            "Soldiers have been stationed at\x01",
            "each checkpoint to protect them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "But occasionally we have to rescue\x01",
            "hikers here in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A1")

    Jump("loc_279B")

    label("loc_20A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_212A")

    ChrTalk(    #93
        0xFE,
        (
            "How should we protect against\x01",
            "an enemy if we are attacked on\x01",
            "both sides...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "That's the topic of today's training.\x02",
    )

    CloseMessageWindow()
    Jump("loc_279B")

    label("loc_212A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_218A")

    ChrTalk(    #95
        0xFE,
        "Oh, so you're leaving, are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "It's a wild world out there, so\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279B")

    label("loc_218A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_21FF")

    ChrTalk(    #97
        0xFE,
        (
            "Good morning. Were you able\x01",
            "to sleep well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Thanks for lending us a hand\x01",
            "like you did last night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279B")

    label("loc_21FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2426")
    OP_A2(0x404)
    ClearMapFlags(0x1)
    OP_69(0xFE, 0x3E8)

    ChrTalk(    #99
        0xFE,
        "Huh? And you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#010FWe apologize for intruding at\x01",
            "this hour.\x02\x03",

            "But we were actually wondering...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x05Joshua explained the situation and asked if they could stay the night.\x01",
            "Estelle tried to make her eyes as large and yearning as she could in the\x01",
            "hopes of scoring some free food, as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #102
        0xFE,
        (
            "I see. Well, that's no problem.\x01",
            "I can see from the emblem\x01",
            "that you're bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "Feel free to use the room next\x01",
            "to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#000FWe really appreciate this,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)
    Jump("loc_247F")

    label("loc_2426")


    ChrTalk(    #105
        0xFE,
        (
            "Feel free to use the room next\x01",
            "to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "How about warming yourselves\x01",
            "up first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247F")

    Jump("loc_279B")

    label("loc_2482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_2541")

    ChrTalk(    #107
        0xFE,
        (
            "It appears that the border garrison\x01",
            "has requested reinforcements for\x01",
            "the headquarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "It looks like the general is planning\x01",
            "to make his move sometime in the\x01",
            "near future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279B")

    label("loc_2541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_25F2")

    ChrTalk(    #109
        0xFE,
        (
            "It appears that General Morgan\x01",
            "has narrowed his search area to the\x01",
            "northern mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "So the sky bandits have been\x01",
            "lurking somewhere along the\x01",
            "border, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_279B")

    label("loc_25F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_2735")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A6")
    OP_A2(0x1)

    ChrTalk(    #111
        0xFE,
        (
            "General Morgan has issued an\x01",
            "order to bolster security in the\x01",
            "surrounding area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "That's because we still don't know\x01",
            "where the sky bandits are hiding.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2732")

    label("loc_26A6")


    ChrTalk(    #113
        0xFE,
        (
            "The mountainous areas are an\x01",
            "especially good place for them\x01",
            "to make a hideout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I need to tell my men to get\x01",
            "squared away as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2732")

    Jump("loc_279B")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_279B")

    ChrTalk(    #115
        0xFE,
        (
            "If you need a gate pass I can\x01",
            "issue one for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Just let me know when you need\x01",
            "one.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279B")

    TalkEnd(0xA)
    Return()

    # Function_6_1CD2 end

    def Function_7_279F(): pass

    label("Function_7_279F")

    TalkBegin(0xB)
    TurnDirection(0xFE, 0x103, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA9")
    OP_A2(0x360)
    OP_A2(0x3)

    ChrTalk(    #117
        0xFE,
        "Isn't that you, Scherazard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "It's nice to see you again. I haven't\x01",
            "seen you since the last time you\x01",
            "were here during your training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#020FIf it isn't Anelace. What\x01",
            "are you doing here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Well, we had a request to\x01",
            "exterminate a monster in\x01",
            "this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        (
            "#020FOh really...?\x02\x03",

            "So how has your swordsmanship been\x01",
            "coming along? Have you started\x01",
            "mastering the use of that weapon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Ah ha ha... Uh...let's avoid that subject\x01",
            "right now. I'm still working on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "By the way Scherazard, are you\x01",
            "here on a job for the guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#020FYeah, something like that. Although\x01",
            "the job is a little different from the\x01",
            "one you're handling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Well, this region has become\x01",
            "more dangerous recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "Make sure to be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BC8")

    label("loc_2AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B58")
    OP_A2(0x3)

    ChrTalk(    #128
        0x103,
        "#020FWell, if it isn't Anelace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Scherazard!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "So how is your investigation\x01",
            "coming along? Have you\x01",
            "made any progress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        "#020FIn a sense, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BC8")

    label("loc_2B58")


    ChrTalk(    #132
        0xFE,
        (
            "One more thing, Scherazard.\x01",
            "The region has become really\x01",
            "dangerous recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "Make sure to be careful.\x02",
    )

    CloseMessageWindow()

    label("loc_2BC8")

    TalkEnd(0xB)
    Return()

    # Function_7_279F end

    def Function_8_2BCC(): pass

    label("Function_8_2BCC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_2C28")

    ChrTalk(    #134
        0xC,
        (
            "Since this place is at such a high\x01",
            "altitude, it gets really cold after dark.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C28")

    TalkEnd(0xC)
    Return()

    # Function_8_2BCC end

    def Function_9_2C2C(): pass

    label("Function_9_2C2C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2CCA")

    ChrTalk(    #135
        0xFE,
        (
            "The wound I got from that\x01",
            "monster has finally healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "I guess I'm going to need to\x01",
            "train harder to make sure\x01",
            "that never happens again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8E")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(    #137
        0xFE,
        "The warrant officer loves to cook.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Even when it's not his turn to cook,\x01",
            "there are times he still makes\x01",
            "things in the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8E")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2DFC")

    ChrTalk(    #139
        0xFE,
        "We're almost out of firewood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "After I finish my training today and\x01",
            "report back to the chief, I think I'll\x01",
            "go out and gather some more wood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E8E")

    label("loc_2DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_2E34")

    ChrTalk(    #141
        0xFE,
        "Owowow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "That monster got me good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E8E")

    label("loc_2E34")


    ChrTalk(    #143
        0xFE,
        (
            "It's almost time for me to go\x01",
            "on duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "I'd better hurry up and eat while\x01",
            "I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E8E")

    TalkEnd(0xD)
    Return()

    # Function_9_2C2C end

    def Function_10_2E92(): pass

    label("Function_10_2E92")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_2EF5")

    ChrTalk(    #145
        0xFE,
        (
            "I've still got time until I go\x01",
            "on duty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Maybe I should catch a\x01",
            "few winks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BE")

    label("loc_2EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_307D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301A")
    OP_A2(0x5)

    ChrTalk(    #147
        0xFE,
        (
            "Since this is the middle of the\x01",
            "mountains, it's really inconvenient\x01",
            "to get food brought up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "We usually get our stuff delivered\x01",
            "from Bose or Ruan along the trail\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "And along with the deliverer's\x01",
            "own escort we have to go and\x01",
            "meet them along the way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_307A")

    label("loc_301A")


    ChrTalk(    #150
        0xFE,
        (
            "It gets really bad when it's the\x01",
            "middle of the winter and we've\x01",
            "got snow piled up to here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_307A")

    Jump("loc_36BE")

    label("loc_307D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3111")

    ChrTalk(    #151
        0xFE,
        "It's almost time for training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "In light of the monsters attacking\x01",
            "the checkpoint, I need to get\x01",
            "myself ready for anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BE")

    label("loc_3111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 6)), scpexpr(EXPR_END)), "loc_3266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31DF")
    OP_A2(0x5)

    ChrTalk(    #153
        0xFE,
        (
            "Hi again. Thanks for your help\x01",
            "the other night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "You may be young, but I shouldn't\x01",
            "expect anything less from a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_31DF")


    ChrTalk(    #156
        0xFE,
        (
            "You may be young, but I shouldn't\x01",
            "expect anything less from a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "That was excellent work you\x01",
            "made of those monsters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3263")

    Jump("loc_36BE")

    label("loc_3266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_3334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32EC")
    OP_A2(0x5)

    ChrTalk(    #158
        0xFE,
        (
            "What's wrong? You're welcome to\x01",
            "go in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "mention it to the chief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3331")

    label("loc_32EC")


    ChrTalk(    #160
        0xFE,
        (
            "If you feel like taking a rest, please\x01",
            "mention it to the chief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3331")

    Jump("loc_36BE")

    label("loc_3334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_34D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345B")
    OP_A2(0x5)

    ChrTalk(    #161
        0xFE,
        (
            "It seems like nobody's been able\x01",
            "to figure out exactly where the\x01",
            "sky bandits really are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "The border garrison often comes\x01",
            "here to investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D5")

    label("loc_345B")


    ChrTalk(    #165
        0xFE,
        (
            "That's because the Bose region\x01",
            "is covered with mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "This area is the perfect place for\x01",
            "criminals to hide.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D5")

    Jump("loc_36BE")

    label("loc_34D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_358A")

    ChrTalk(    #167
        0xFE,
        (
            "It seems as though the missing\x01",
            "airliner was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "However, since the criminals weren't\x01",
            "apprehended, these security checks\x01",
            "are going to continue for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BE")

    label("loc_358A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_3640")

    ChrTalk(    #169
        0xFE,
        "Sky bandits, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "General Morgan is spearheading\x01",
            "the investigation this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "It's only a matter of time until\x01",
            "he's got this bunch locked up\x01",
            "behind bars.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36BE")

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_36BE")

    ChrTalk(    #172
        0xFE,
        (
            "We are on high alert at the\x01",
            "moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "If you're heading anywhere,\x01",
            "then you'll need to fill out\x01",
            "some paperwork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36BE")

    TalkEnd(0xE)
    Return()

    # Function_10_2E92 end

    def Function_11_36C2(): pass

    label("Function_11_36C2")

    EventBegin(0x0)
    OP_6D(80990, 200, 53320, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, 81090, 200, 51050, 270)
    SetChrPos(0x102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrPos(0xF, 79980, 750, 50430, 0)
    SetChrPos(0x10, 79200, 750, 51110, 0)
    SetChrPos(0x11, 80060, 700, 51150, 0)
    SetChrPos(0x12, 79240, 700, 50480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(    #174
        0x101,
        (
            "#001F#2POh, man, I'm so stuffed!\x02\x03",

            "They said not to expect much,\x01",
            "but the food was pretty good,\x01",
            "didn't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x102,
        (
            "#010FY-Yeah. It was, uh, certainly like\x01",
            "nothing I've ever had before.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 72320, 0, 52990, 90)

    ChrTalk(    #176
        0x8,
        "#2PExcuse me for disturbing you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x4)

    def lambda_3909():
        OP_6D(79690, 0, 53470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3909)
    SetChrSubChip(0x102, 1)
    OP_8C(0x8, 90, 0)
    ClearChrFlags(0x8, 0x80)

    def lambda_3932():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_3932)
    OP_8E(0x8, 0x1372C, 0x0, 0xCE86, 0xBB8, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #177
        0x101,
        (
            "#001F#4POh, sir! The meal was delicious!\x01",
            "Thanks so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#010F#2P...Yes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#3PR-Really? You must have taste buds\x01",
            "of iron, too... I mean, I'm glad to hear\x01",
            "that you enjoyed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        (
            "#3PAnyway...we've had another guest arrive,\x01",
            "so if it's not too much trouble, could\x01",
            "you two share the same room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x102,
        (
            "#014F#2PAnother guest...in the middle of\x01",
            "the night like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#000F#4PThey must have some serious guts\x01",
            "to be hiking around in the mountains\x01",
            "at this hour.\x02\x03",

            "But no, we don't mind. It's not like\x01",
            "we're paying to stay here either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "#3PI really appreciate that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#3PHe's actually in the same line of\x01",
            "work as the both of you, so I'm sure\x01",
            "you'll get along just fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#004F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x102,
        "#014F#2PThe same line of work?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x106, 0x80)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x106, 7)
    SetChrPos(0x106, 72320, 0, 52990, 90)

    NpcTalk(    #187
        0x106,
        "Man's Voice",
        (
            "#2PHmph...I knew I'd seen you two\x01",
            "somewhere before.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x4)

    def lambda_3CBA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3CBA)

    def lambda_3CCC():
        OP_8E(0xFE, 0x13330, 0x0, 0xD160, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3CCC)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x106, 0x1)
    OP_8C(0x106, 180, 400)
    ClearChrFlags(0x106, 0x4)

    ChrTalk(    #188
        0x101,
        "#004F#4PY-You're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        "#014F#2PThe 'Heavy Blade' Agate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x8,
        (
            "#3POh, so you know each other\x01",
            "already, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(    #191
        0x8,
        (
            "#4PBy the way, Agate, what do you\x01",
            "plan to do about dinner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x106,
        (
            "#050FI appreciate the invitation, but\x01",
            "I had something before coming\x01",
            "up here.\x02\x03",

            "All I need is somewhere to crash\x01",
            "for the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x8,
        "#4PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "#4PGo ahead and divide up the beds\x01",
            "amongst yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(300)

    ChrTalk(    #195
        0x8,
        "#3PAll right, good night.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    OP_44(0x106, 0xFF)
    OP_8E(0x8, 0x13240, 0x0, 0xCDDC, 0xBB8, 0x0)

    def lambda_3F06():

        label("loc_3F06")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3F06")

    QueueWorkItem2(0x106, 3, lambda_3F06)
    OP_8E(0x8, 0x1234A, 0x0, 0xCEAE, 0xBB8, 0x0)

    def lambda_3F2B():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3F2B)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    def lambda_3F65():
        OP_6D(80990, 200, 53320, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F65)
    OP_44(0x106, 0xFF)
    OP_8C(0x106, 135, 400)
    OP_8E(0x106, 0x1372C, 0x0, 0xCE86, 0x7D0, 0x0)
    OP_8C(0x106, 180, 400)

    ChrTalk(    #196
        0x106,
        (
            "#050F#1PNow, if I remember right...weren't\x01",
            "you Cassius' kids?\x02\x03",

            "What are you doing sleeping in\x01",
            "a place like this?\x02\x03",

            "And what happened to Scherazard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#010F#2PSchera returned to Rolent.\x02\x03",

            "Now it's just the two of us\x01",
            "traveling together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#006F#2PWe're thinking of making our way\x01",
            "around the kingdom in order to\x01",
            "become senior bracers.\x02\x03",

            "We're going to see the places we\x01",
            "want to protect and train so that\x01",
            "we can do just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x106,
        (
            "#052F#1PSenior bracers? Traveling the entire\x01",
            "kingdom on foot?\x02\x03",

            "You two are really a bunch of\x01",
            "carefree brats, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #200
        0x101,
        "#009F#2PWhat did you just call us?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x106,
        (
            "#053F#1PThere's no way the two of you are\x01",
            "going to simply become senior\x01",
            "bracers.\x02\x03",

            "Use your brains and think about\x01",
            "it for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#005F#2PSay what you want, but we helped\x01",
            "in the arrest of the sky bandits!\x02\x03",

            "And we've even got some recommendations,\x01",
            "so quit treating us like we're a bunch\x01",
            "of kids!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#050F#1POh, that? I heard all about it from\x01",
            "old man Lugran.\x02\x03",

            "#050FAll right, let me put it to you this way:\x01",
            "Suppose you had been the only ones there.\x01",
            "Do you think you could've solved the incident?\x02\x03",

            "Just you two alone, without Scherazard's help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#003F#2PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#015F#2PI think it would have been\x01",
            "very difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x106,
        (
            "#050F#1PThat's pretty obvious when you think\x01",
            "about it, huh?\x02\x03",

            "You two are newbies and little brats,\x01",
            "to say the least.\x02\x03",

            "Not to mention, you're lacking in strength\x01",
            "and experience. You don't have the ability\x01",
            "to make quick, sound judgments.\x02\x03",

            "If you get all caught up in yourselves and\x01",
            "forget that, one of these days you're going\x01",
            "to get the rug pulled out from under you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#009F#2PWe-we're not all caught up in\x01",
            "ourselves!\x02\x03",

            "How about yourself, Mr. Macho Man? What\x01",
            "were you thinking trying to hike through\x01",
            "the pass at this hour of the night?\x02\x03",

            "You're either plain careless...\x01",
            "or maybe that bandanna's just a\x01",
            "little too tight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x106,
        (
            "#054F#1PWatch your mouth, brat.\x01",
            "I'm trying to hone my skills,\x01",
            "unlike you amateurs.\x02\x03",

            "And besides, I'm here for work.\x01",
            "Don't try and compare my actions\x01",
            "with your tourist-training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x102,
        "#012F#2PWork...for the guild?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x106,
        (
            "#050F#1PYeah, that's right. The work your\x01",
            "old man forced on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        "#004F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x102,
        "#014F#2PDad pushed his work onto you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x106,
        "#050F#1P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(    #214
        0x106,
        (
            "#053FForget about it. I've got an early\x01",
            "day ahead of me, so I need to\x01",
            "get some rest.\x02\x03",

            "You two quit talking and get some\x01",
            "sleep, too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4902():
        OP_6D(79640, 0, 54740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4902)
    OP_8E(0x106, 0x12F52, 0x0, 0xDCA0, 0x9C4, 0x0)
    OP_8C(0x106, 180, 400)
    SetChrFlags(0x106, 0x4)
    OP_96(0x106, 0x12818, 0x3E8, 0xD994, 0x4B0, 0x1388)
    OP_22(0xD1, 0x0, 0x64)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 9)
    OP_7C(0x0, 0x64, 0x7D0, 0x64)

    ChrTalk(    #215
        0x101,
        (
            "#005F#2PAh! He just avoided finishing\x01",
            "the conversation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x102,
        (
            "#018F#2PWell, he did drop a tidbit about Dad.\x01",
            "That's something, at least...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)
    OP_99(0x106, 0x0, 0x2, 0x3E8)
    Sleep(300)
    SetChrSubChip(0x106, 3)

    ChrTalk(    #217
        0x106,
        (
            "#054F#1PEnough already, you two! Just shut\x01",
            "the hell up, and let me sleep!\x02\x03",

            "And you better stop poking around\x01",
            "where you shouldn't or you're gonna\x01",
            "get burned.\x02\x03",

            "Instead, why don't you get your\x01",
            "behinds over to Ruan, and do some\x01",
            "jobs listed on the bulletin board.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x106, 0x3, 0x5, 0x3E8)
    Sleep(400)

    ChrTalk(    #218
        0x106,
        (
            "#053F#1PThat's...*yawn*...far better suited\x01",
            "for the likes of you...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #219
        0x101,
        "#004F#2PH-Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x102,
        (
            "#014F#2PIt looks like he's asleep...and just\x01",
            "as quickly as someone I know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#005F#2PDon't you even dare suggest that\x01",
            "I'm anything like this jerk!\x02\x03",

            "#007FWhat's his deal, anyway?!\x02\x03",

            "It seems to me like all he's trying\x01",
            "to do is pick a fight...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0)
    Sleep(300)

    ChrTalk(    #222
        0x102,
        (
            "#010F#5PRelax, Estelle. It's true we're still\x01",
            "just novices at this.\x02\x03",

            "It could be that he just said that\x01",
            "to us because he was worried\x01",
            "about us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#009F#2P...\x02\x03",

            "Do you really think so, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#015F#5PI wish I could say for sure,\x01",
            "but I don't know.\x02\x03",

            "#010FBut he definitely did get one thing\x01",
            "right: we SHOULD turn in for the\x01",
            "night.\x02\x03",

            "We've still got to hike down through\x01",
            "the pass tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#007F#2PI'm all riled up now, but I guess\x01",
            "there's nothing to be done about\x01",
            "it...\x02\x03",

            "#006FUnless...we doodle on this jerk's\x01",
            "face and then go to sleep.\x02\x03",

            "I'm pretty sure he wouldn't wake up\x01",
            "with the way he's snoring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        "#018F#5PDon't even think about it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT01/T1301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_36C2 end

    def Function_12_4F91(): pass

    label("Function_12_4F91")

    EventBegin(0x0)
    OP_6D(79640, 0, 54740, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x101, 81090, 200, 51050, 270)
    SetChrPos(0x102, 78250, 200, 51000, 90)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0x102, 1)
    SetChrPos(0xF, 79980, 750, 50430, 0)
    SetChrPos(0x10, 79200, 750, 51110, 0)
    SetChrPos(0x11, 80060, 700, 51150, 0)
    SetChrPos(0x12, 79240, 700, 50480, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x106, 0x2)
    SetChrPos(0x106, 75800, 1000, 55700, 0)
    SetChrChipByIndex(0x106, 9)
    SetChrSubChip(0x106, 2)
    OP_0D()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x106, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #227
        0x101,
        "#004F#2PWh-What was that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        "#012F#5PSounds like something's going on.\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x106)
    Sleep(300)
    SetChrChipByIndex(0x106, 7)
    ClearChrFlags(0x106, 0x2)
    OP_8C(0x106, 90, 0)
    SetChrSubChip(0x106, 0)
    OP_96(0x106, 0x12FA2, 0x0, 0xDB06, 0x258, 0x1770)
    OP_8E(0x106, 0x12ED0, 0x0, 0xD052, 0xFA0, 0x0)

    ChrTalk(    #229
        0x106,
        (
            "#050F#1PI'm going to go check it out.\x01",
            "You two stay here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x12412, 0x0, 0xCEA4, 0x1770, 0x0)
    OP_22(0x6, 0x0, 0x64)

    def lambda_51B3():
        OP_8E(0xFE, 0x11A80, 0x0, 0xCEFE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_51B3)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrFlags(0x106, 0x80)

    ChrTalk(    #230
        0x101,
        "#004F#2PAh! Now just you wait a min...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#012F#5PI think we'd better go see for\x01",
            "ourselves, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#002F#2POf course that's what we\x01",
            "should do!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x102, 77820, 0, 53250, 270)
    SetChrPos(0x101, 77820, 0, 53250, 270)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_6D(77820, 0, 53250, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x405)
    Return()

    # Function_12_4F91 end

    def Function_13_52F3(): pass

    label("Function_13_52F3")

    RemoveParty(0x5, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(83887, 0, 57065, 0)
    SetChrPos(0x101, 84150, 0, 57128, 270)
    SetChrPos(0x102, 82890, 0, 56215, 90)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)

    ChrTalk(    #233
        0x102,
        "#010FEstelle. Estelle, wake up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#000F*yawn*...Come on, can't a woman\x01",
            "have her beauty sleep...?\x02",
        )
    )

    CloseMessageWindow()
    OP_77(0xFF, 0xFF, 0xFF, 0x3E800, 0x0)
    Sleep(1300)

    ChrTalk(    #235
        0x101,
        (
            "#000FHuh? Joshua...?\x02\x03",

            "Is it already time to go to the\x01",
            "guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x102,
        (
            "#010FWhat are you talking about?\x01",
            "This is the Krone Pass Checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #237
        0x101,
        (
            "#000FOh right...we had that monster\x01",
            "scare last night and...\x02\x03",

            "Huh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)
    Sleep(300)
    OP_8C(0x101, 315, 400)
    Sleep(300)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #238
        0x101,
        "#000FWhere'd the redheaded jerk go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x102,
        (
            "#010FIt looks like he took off early this\x01",
            "morning. Apparently, he had an\x01",
            "urgent job to attend to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#000FOh...\x02\x03",

            "And after we helped him fend off\x01",
            "those monsters last night, too.\x02\x03",

            "How rude of him not to say\x01",
            "anything before leaving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#010FIt's not that big of a deal,\x01",
            "Estelle.\x02\x03",

            "How about we get ready ourselves?\x01",
            "I'd like to make it through the pass\x01",
            "by noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x101,
        (
            "#000FAll right.\x02\x03",

            "It's off to Ruan we go!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x406)
    OP_28(0x3A, 0x4, 0x2)
    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x1, 0x1)
    OP_28(0x3A, 0x1, 0x2)
    Fade(1000)
    SetChrPos(0x101, 82076, 0, 53560, 270)
    SetChrPos(0x102, 82076, 0, 53560, 270)
    EventEnd(0x0)
    Return()

    # Function_13_52F3 end

    def Function_14_56C9(): pass

    label("Function_14_56C9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #243
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58E4")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x32)
    OP_73(0x33)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 19740, 0, 13090, 217)
    SetChrPos(0x1, 19740, 0, 13090, 217)
    SetChrPos(0x2, 19740, 0, 13090, 217)
    SetChrPos(0x3, 19740, 0, 13090, 217)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0xA, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_58E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58FE")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_58FE")

    Return()

    # Function_14_56C9 end

    SaveToFile()

Try(main)
