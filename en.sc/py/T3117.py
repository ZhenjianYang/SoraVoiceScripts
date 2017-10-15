from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3117_1 ._SN',
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
        'Ray',                                  # 9
        'Terry',                                # 10
        'Muriel',                               # 11
        'Antoine',                              # 12
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
    )

    DeclNpc(
        X                   = 1070,
        Z                   = 0,
        Y                   = 9970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -3500,
        Z                   = 0,
        Y                   = 14150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -2590,
        Z                   = 0,
        Y                   = 8420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 3650,
        Z                   = 0,
        Y                   = 2680,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -5350,
        TriggerZ            = 0,
        TriggerY            = 4760,
        TriggerRange        = 1000,
        ActorX              = -5350,
        ActorZ              = 500,
        ActorY              = 4760,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5500,
        TriggerZ            = 0,
        TriggerY            = 5390,
        TriggerRange        = 1000,
        ActorX              = 5500,
        ActorZ              = 500,
        ActorY              = 5390,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4470,
        TriggerZ            = 1000,
        TriggerY            = 14290,
        TriggerRange        = 1000,
        ActorX              = 4470,
        ActorZ              = 1500,
        ActorY              = 14290,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1750,
        TriggerZ            = 0,
        TriggerY            = 12760,
        TriggerRange        = 1000,
        ActorX              = 1750,
        ActorZ              = 0,
        ActorY              = 12760,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_287",          # 01, 1
        "Function_2_2B7",          # 02, 2
        "Function_3_2DB",          # 03, 3
        "Function_4_9AB",          # 04, 4
        "Function_5_1B44",         # 05, 5
        "Function_6_1C46",         # 06, 6
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1EB")
    Jump("loc_201")

    label("loc_1EB")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 4490, 1000, 8220, 0)

    label("loc_201")

    Jump("loc_286")

    label("loc_204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_224")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -2590, 0, 9570, 270)
    Jump("loc_286")

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_24E")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -2590, 0, 9570, 180)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_286")

    label("loc_24E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_27A")
    SetChrPos(0x8, 5290, 1000, 8740, 0)
    SetChrPos(0x9, -2590, 0, 9570, 270)
    Jump("loc_286")

    label("loc_27A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_286")
    ClearChrFlags(0xB, 0x80)

    label("loc_286")

    Return()

    # Function_0_1DA end

    def Function_1_287(): pass

    label("Function_1_287")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6")
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_7B()
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x4)

    label("loc_2A6")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Return()

    # Function_1_287 end

    def Function_2_2B7(): pass

    label("Function_2_2B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DA")
    OP_8D(0xFE, 4670, 5810, -4590, 550, 1000)
    Jump("Function_2_2B7")

    label("loc_2DA")

    Return()

    # Function_2_2B7 end

    def Function_3_2DB(): pass

    label("Function_3_2DB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")

    ChrTalk(    #0
        0xFE,
        "Phew! Finally managed to get back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Orbments may not be working,\x01",
            "but the greenhouse is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Terry's done at least a basic level\x01",
            "of work...I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Phew! I pray things go well with the Arseille.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_422")

    label("loc_3D0")


    ChrTalk(    #4
        0xFE,
        "The greenhouse is safe, so that's a relief.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Time to resume experiments!\x02",
    )

    CloseMessageWindow()

    label("loc_422")

    Jump("loc_9A7")

    label("loc_425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_697")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F2")

    ChrTalk(    #6
        0xFE,
        "I wish I had an adorable assistant like Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Maybe once I'm done with the greenhouse\x01",
            "experiments, I'll set to developing an Orbal Doll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I'd model it after Tita, of course!\x02",
    )

    CloseMessageWindow()
    Jump("loc_694")

    label("loc_4F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52F")

    ChrTalk(    #9
        0xFE,
        "Hey, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Busy again today, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_590")

    label("loc_52F")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)
    Sleep(400)

    ChrTalk(    #11
        0xFE,
        "Oh, is that Tita over there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "You look as busy as always.\x02",
    )

    CloseMessageWindow()

    label("loc_590")


    ChrTalk(    #13
        0x107,
        (
            "#560FYup.\x02\x03",

            "I'm helping Grandpa out again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Man, Professor Russell sure is blessed\x01",
            "to have an assistant like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Unlike my assistant...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #16
        0xFE,
        "Ah, enough complaining.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Tita, pardon me. You can go back to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#060FOkay. Bye, Ray!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_694")

    Jump("loc_9A7")

    label("loc_697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_83F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_731")

    ChrTalk(    #19
        0xFE,
        (
            "The world is covered in things\x01",
            "that could be researched.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "However, only a small handful of them\x01",
            "are actually worth researching.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83C")

    label("loc_731")


    ChrTalk(    #21
        0xFE,
        (
            "I just had success improving farm\x01",
            "crops during my last bit of testing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "But raising boring, old, normal plants\x01",
            "isn't exactly interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Argh, no brilliant ideas are coming to\x01",
            "me just moping around here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Maybe it's about time to go for a walk.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_83C")

    Jump("loc_9A7")

    label("loc_83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_9A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8C4")

    ChrTalk(    #25
        0xFE,
        (
            "Terry hasn't decided on a theme for\x01",
            "this period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Since I basically had to, I'm using him\x01",
            "as my assistant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A7")

    label("loc_8C4")


    ChrTalk(    #27
        0xFE,
        (
            "I guess I'll be continuing research with\x01",
            "the greenhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Though, to be honest, I'll be leaving\x01",
            "most of it to Terry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I wonder if there isn't some more\x01",
            "interesting direction I could take using\x01",
            "the greenhouse...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9A7")

    TalkEnd(0x8)
    Return()

    # Function_3_2DB end

    def Function_4_9AB(): pass

    label("Function_4_9AB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BB")
    OP_A2(0x3)

    label("loc_9BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A53")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Finished QST042 in the previous game\x01",            # 0
            "Did not finish QST042 in the previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A47"),
        (1, "loc_A4D"),
        (SWITCH_DEFAULT, "loc_A53"),
    )


    label("loc_A47")

    OP_A2(0x3)
    Jump("loc_A53")

    label("loc_A4D")

    OP_A3(0x3)
    Jump("loc_A53")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B80")

    ChrTalk(    #30
        0xFE,
        "Ray's finally back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "He was doing some cooperative research\x01",
            "with Russell on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Wh-While I was managing the greenhouse,\x01",
            "Ray was researching leading-edge tech...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Damn it!! I've gotta step up my game!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "I'll get results with my research next period!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C1B")

    label("loc_B80")


    ChrTalk(    #35
        0xFE,
        (
            "I feel like the gap between me and Ray\x01",
            "is only increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I've got to come up with some\x01",
            "groundbreaking results! Kick some\x01",
            "ass, take some names!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1B")

    Jump("loc_1B40")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 2)), scpexpr(EXPR_END)), "loc_CD2")

    ChrTalk(    #37
        0xFE,
        "A-Anyway, I hope Ray comes back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Since orbments aren't working, the\x01",
            "temperature in the greenhouse isn't\x01",
            "holding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Man, Ray! Please come back...\x02",
    )

    CloseMessageWindow()
    Jump("loc_10F0")

    label("loc_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1010")

    ChrTalk(    #40
        0xFE,
        (
            "Ray was dragged off into some\x01",
            "other research...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "So I'm stuck managing the greenhouse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "But, with the orbments not working, the\x01",
            "temperature in the greenhouse just keeps\x01",
            "dropping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "A-Anyway, I hope Ray comes back soon.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 7)), scpexpr(EXPR_END)), "loc_100A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBD")

    ChrTalk(    #44
        0x107,
        (
            "#064FSpeaking of Ray...\x02\x03",

            "We saw him over at the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #45
        0xFE,
        "The K-Krone Pass?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1002FYeah...\x02\x03",

            "I'm sure he'll be back eventually.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #47
        0xFE,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "Well, I just want him to get back safe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1007")

    label("loc_EBD")


    ChrTalk(    #49
        0x101,
        (
            "#1015FI guess we might as well tell you...\x02\x03",

            "We saw Ray at the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #50
        0xFE,
        "The K-Krone Pass?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1040FYeah. With the airliners grounded, there's\x01",
            "no way to get around except to walk, really.\x02\x03",

            "It might take some time, but I'm sure he'll\x01",
            "be back.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #52
        0xFE,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "Well, I just want him to get back safe.\x02",
    )

    CloseMessageWindow()

    label("loc_1007")

    OP_A2(0x20D2)

    label("loc_100A")

    OP_A2(0x1)
    Jump("loc_10F0")

    label("loc_1010")


    ChrTalk(    #54
        0xFE,
        (
            "Since Ray was dragged off on other research,\x01",
            "I'm stuck managing the greenhouse alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "But, with the orbments not working, the\x01",
            "temperature in the greenhouse just keeps\x01",
            "dropping...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "Man, Ray! Please come back...\x02",
    )

    CloseMessageWindow()

    label("loc_10F0")

    Jump("loc_1B40")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_159C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_128A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1191")

    ChrTalk(    #57
        0xFE,
        "Hmm... What would be a good theme?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Ahh, Muriel...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #60
        0xFE,
        "...Gah, what am I even thinking?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1287")

    label("loc_1191")


    ChrTalk(    #61
        0xFE,
        "This new girl came by a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "She was so eager and c-c-cute. She really\x01",
            "felt like a super honest, bright girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "...Gah, I don't have time to think about that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "I... I need to decide on a research theme\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    OP_A2(0x2)

    label("loc_1287")

    Jump("loc_152E")

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1353")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1315")

    ChrTalk(    #65
        0xFE,
        "Right now, I'm still searching for a theme.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Until I can come up with one, I'm helping\x01",
            "Ray with his experiments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1350")

    label("loc_1315")


    ChrTalk(    #67
        0xFE,
        "S-So you're new, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "You s-sure are young...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1350")

    Jump("loc_152E")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13E3")

    ChrTalk(    #69
        0xFE,
        "*sigh* I really need to pick a theme soon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "At this rate, I'm going to end up playing\x01",
            "second fiddle to Ray forever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1490")

    label("loc_13E3")


    ChrTalk(    #71
        0xFE,
        (
            "Hmm, what should I have as my\x01",
            "next theme...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I can't just stay helping Ray forever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "If I waste too much time, I'll just end up\x01",
            "turning into his assistant.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1490")

    Jump("loc_152E")

    label("loc_1493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_152E")

    ChrTalk(    #74
        0xFE,
        (
            "This is the fourth floor, so the tremors\x01",
            "felt pretty strong up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I'm just glad there wasn't any damage\x01",
            "to the facilities, personally.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_152E")

    Jump("loc_1599")

    label("loc_1531")


    ChrTalk(    #76
        0xFE,
        (
            "I'm searching for a theme for my next\x01",
            "research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "If anything comes up, I'll contact the guild.\x02",
    )

    CloseMessageWindow()

    label("loc_1599")

    Jump("loc_1B40")

    label("loc_159C")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #78
        0xFE,
        "Hey, it's been a while. Remember me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "I'm Terry! I was doing research on sneakers.\x01",
            "Please say you remember me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1016FAhaha, don't worry. I remember you.\x02\x03",

            "It was a job for Stregas! No way I'd\x01",
            "forget a dream job like that.\x02\x03",

            "#1000FSo, still researching shoes, Terry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Not anymore. Thanks to your help getting\x01",
            "that data before, I was able to achieve my\x01",
            "research goals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "After handing the findings over to the\x01",
            "Strega Corporation, the job was finished.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #83
        0xFE,
        (
            "Oh, yeah. I gave them your message\x01",
            "like I said I would.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I told them a bracer fan said she couldn't\x01",
            "'wait to see the next new product.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #85
        0x101,
        "#1004FR-Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Yeah, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "The Strega developers were really touched.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "They were making jokes about making a\x01",
            "bracer model next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1008FAww, it was just a joke...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Haha, who knows? I thought it was\x01",
            "a joke, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "One way or another, I got more\x01",
            "research funding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "So right now, I'm looking for a new\x01",
            "research theme.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "I might ask the guild for help again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I hope I can count on you like before\x01",
            "if anything comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1006FYeah, don't hesitate to contact us.\x02\x03",

            "#1015FAlso, I'm sure you know, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1005F#3SBe sure to prioritize requests from the\x01",
            "Strega Corporation, okay?! And if you\x01",
            "need a bracer, I'm your woman!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #97
        0xFE,
        "Hahaha, understood.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x142D)
    OP_A2(0x1)

    label("loc_1B40")

    TalkEnd(0x9)
    Return()

    # Function_4_9AB end

    def Function_5_1B44(): pass

    label("Function_5_1B44")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1C42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BAC")

    ChrTalk(    #98
        0xFE,
        "So what kind of research do you doooo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "Teehee, that's sooooo interesting.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C42")

    label("loc_1BAC")


    ChrTalk(    #100
        0xFE,
        "Heehee, nice to meet you. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "I'm Muriel, an apprentice here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'm searching for some documents.\x01",
            "Can I have a moment of your time? ☆\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1C42")

    TalkEnd(0xA)
    Return()

    # Function_5_1B44 end

    def Function_6_1C46(): pass

    label("Function_6_1C46")

    TalkBegin(0xB)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #103
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_1C46 end

    SaveToFile()

Try(main)
