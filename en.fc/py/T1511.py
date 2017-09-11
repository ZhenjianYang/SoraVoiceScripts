from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1511   ._SN',
        MapName             = 'Bose',
        Location            = 'T1511.x',
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
        'Lenard',                               # 9
        'Sophina',                              # 10
        'Lloyd',                                # 11
        'Elke',                                 # 12
        'Anette',                               # 13
        'Olivier',                              # 14
        'Olivier',                              # 15
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
        Unknown_30              = 225,
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH01690 ._CH',             # 01
        'ED6_DT07/CH01023 ._CH',             # 02
        'ED6_DT07/CH01180 ._CH',             # 03
        'ED6_DT07/CH01210 ._CH',             # 04
        'ED6_DT06/CH20050 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH01690P._CP',             # 01
        'ED6_DT07/CH01023P._CP',             # 02
        'ED6_DT07/CH01180P._CP',             # 03
        'ED6_DT07/CH01210P._CP',             # 04
        'ED6_DT06/CH20050P._CP',             # 05
    )

    DeclNpc(
        X                   = 24400,
        Z                   = 0,
        Y                   = 9200,
        Direction           = 0,
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
        X                   = 14000,
        Z                   = 0,
        Y                   = 3600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 49500,
        Z                   = 200,
        Y                   = 26230,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 54500,
        Z                   = 0,
        Y                   = 3400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 49900,
        Z                   = 0,
        Y                   = 5800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 109100,
        Z                   = 600,
        Y                   = 5100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x156,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 110010,
        Z                   = -500,
        Y                   = 5150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x156,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 80610,
        TriggerZ            = 0,
        TriggerY            = 9100,
        TriggerRange        = 1400,
        ActorX              = 80610,
        ActorZ              = 1500,
        ActorY              = 9100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_1EE",          # 02, 2
        "Function_3_204",          # 03, 3
        "Function_4_228",          # 04, 4
        "Function_5_2B1",          # 05, 5
        "Function_6_341",          # 06, 6
        "Function_7_3D9",          # 07, 7
        "Function_8_48E",          # 08, 8
        "Function_9_67B",          # 09, 9
        "Function_10_6B9",         # 0A, 10
        "Function_11_EA8",         # 0B, 11
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_1EC")

    Return()

    # Function_0_1DE end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    Return()

    # Function_1_1ED end

    def Function_2_1EE(): pass

    label("Function_2_1EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_203")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1EE")

    label("loc_203")

    Return()

    # Function_2_1EE end

    def Function_3_204(): pass

    label("Function_3_204")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_8D(0xFE, 50200, 5000, 54800, 6300, 2000)
    Jump("Function_3_204")

    label("loc_227")

    Return()

    # Function_3_204 end

    def Function_4_228(): pass

    label("Function_4_228")

    TalkBegin(0x8)

    ChrTalk(    #0
        0xFE,
        "Are you going out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If you're going to fish at night,\x01",
            "you're going to need an orbment\x01",
            "light or you won't be able to see.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_4_228 end

    def Function_5_2B1(): pass

    label("Function_5_2B1")

    TalkBegin(0x9)

    ChrTalk(    #2
        0xFE,
        (
            "That gentleman with you seems\x01",
            "to have drunk a lot. Is he going\x01",
            "to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "If you would like, I can bring\x01",
            "you some water.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_5_2B1 end

    def Function_6_341(): pass

    label("Function_6_341")

    TalkBegin(0xB)

    ChrTalk(    #4
        0xFE,
        "Good evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Seeing another group of lodgers\x01",
            "is something I enjoy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I'd love to keep company with\x01",
            "you if that would be all right.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_6_341 end

    def Function_7_3D9(): pass

    label("Function_7_3D9")

    TalkBegin(0xC)

    ChrTalk(    #7
        0xFE,
        (
            "My mother seems to be\x01",
            "enjoying the atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I was the first person to recommend\x01",
            "this inn to my mother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Now she invites me to come\x01",
            "here with her every year.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_7_3D9 end

    def Function_8_48E(): pass

    label("Function_8_48E")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63C")
    OP_A2(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #10
        "\x07\x05Lloyd is staring at an open map. It appears to be a map of Valleria Lake.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #11
        0xFE,
        (
            "There are hardly any structures\x01",
            "on the west side, and I didn't get\x01",
            "many bites either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "And all I'm getting on the east\x01",
            "side are small sized fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "The Guardian probably won't appear\x01",
            "in either of these two places...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I guess the best thing I can\x01",
            "do is to continue fishing\x01",
            "from the shore.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677")

    label("loc_63C")


    ChrTalk(    #15
        0xFE,
        (
            "I'm going to catch the Guardian this\x01",
            "time for sure...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677")

    TalkEnd(0xA)
    Return()

    # Function_8_48E end

    def Function_9_67B(): pass

    label("Function_9_67B")

    TalkBegin(0xD)

    ChrTalk(    #16
        0xFE,
        (
            "Ugh... Schera...please...\x01",
            "I can't take another...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_9_67B end

    def Function_10_6B9(): pass

    label("Function_10_6B9")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    AddParty(0x2, 0xFF)
    SetChrPos(0x101, 107680, 0, 5310, 90)
    SetChrPos(0x103, 109180, 0, 6400, 180)
    SetChrPos(0x102, 107620, 0, 6630, 135)
    OP_6D(107890, 0, 13120, 0)
    OP_A2(0x34E)
    OP_28(0x38, 0x1, 0x80)
    FadeToBright(2000, 0)
    OP_6D(109120, 0, 5740, 3000)

    ChrTalk(    #17
        0xE,
        (
            "#038F#6POhhh... Uggghhh...\x02\x03",

            "Uhhh... Gehhh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#007F#6POh, he's totally plastered.\x02\x03",

            "It looks like even a guy who takes his\x01",
            "sweet time for everything couldn't stand\x01",
            "up to a drunken Schera.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(    #19
        0x103,
        (
            "#021F#6POh, wow. What a night of drinking.\x02\x03",

            "I've been so busy lately I haven't\x01",
            "been able to enjoy myself like\x01",
            "this for a while.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 200)

    ChrTalk(    #20
        0x102,
        (
            "#017FAnd you're not even red in the\x01",
            "face either from all that alcohol...\x02\x03",

            "#018FAre you sure you haven't had\x01",
            "some special kind of training,\x01",
            "Schera?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #21
        0x103,
        (
            "#020F#6PUm, it could have been all the\x01",
            "bizarre liquors I drank while\x01",
            "I was in the troupe.\x02\x03",

            "You know, like the ones with\x01",
            "scorpions and asps in them.\x02\x03",

            "#021FI might have built up my resistance\x01",
            "that way, but who knows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#017FSomehow...I don't think that that's\x01",
            "the case.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #23
        0x101,
        (
            "#009F#6PBy the way, what do you plan on\x01",
            "doing with him? He's pretty much\x01",
            "useless as he is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #24
        0x103,
        (
            "#026F#6PLet's just let him sleep. He looks\x01",
            "so peaceful now, and we wouldn't\x01",
            "want to disturb him.\x02\x03",

            "#022FThere's a very high possibility\x01",
            "that we'll have a direct encounter\x01",
            "with the sky bandits tonight.\x02\x03",

            "And getting a civilian wrapped up\x01",
            "in the middle of it all wouldn't\x01",
            "be a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#004F#6PDon't tell me you...\x02\x03",

            "You got Olivier drunk so he wouldn't\x01",
            "be able to come along, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#023F#6PWell...\x02\x03",

            "...\x02\x03",

            "#021FOf course I did. And he'll thank\x01",
            "me in the long run, too. After\x01",
            "his raging hangover, anyway...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#509F#6PAnd so that whole time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#018FYou were just toying with him,\x01",
            "weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#026F#6PLet's see... It's getting late.\x02\x03",

            "Let's hurry and begin our stakeout\x01",
            "around the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#507F#6PDon't skirt around the issue,\x01",
            "Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x103,
        (
            "#022F#6PQuiet, you!\x02\x03",

            "For the time being, we're going\x01",
            "to circle up to the far pier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#006F#6PAll right then, let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 107480, 0, 9560, 0)
    SetChrPos(0x103, 107480, 0, 9560, 0)
    SetChrPos(0x102, 107480, 0, 9560, 0)
    OP_6D(107480, 0, 9560, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    ClearMapFlags(0x10000000)
    Return()

    # Function_10_6B9 end

    def Function_11_EA8(): pass

    label("Function_11_EA8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05There are some fishing rods propped against the rack.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_EA8 end

    SaveToFile()

Try(main)
