from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2300.x',
        MapIndex            = 86,
        MapDefaultBGM       = "ed60015",
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
        'Manoria Byroad',                       # 9
        'Gull Seaside Way',                     # 10
        'Target Camera',                        # 11
        'Lucia',                                # 12
        'Grant',                                # 13
        'Sadie',                                # 14
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01260 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01260P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
    )

    DeclNpc(
        X                   = -2940,
        Z                   = 7990,
        Y                   = 68620,
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
        X                   = 75410,
        Z                   = -40,
        Y                   = 20810,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 37840,
        Z                   = -50,
        Y                   = 17810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 38170,
        Z                   = -20,
        Y                   = 18890,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 0,
        Y                   = 23500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclEvent(
        X                   = 27540,
        Y                   = 0,
        Z                   = 18980,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 53410,
        Y                   = 0,
        Z                   = 22710,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4000,
        Z                   = 20210,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 11,
    )


    DeclActor(
        TriggerX            = 37770,
        TriggerZ            = -10,
        TriggerY            = 19530,
        TriggerRange        = 1000,
        ActorX              = 37770,
        ActorZ              = 1800,
        ActorY              = 19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_206",          # 00, 0
        "Function_1_293",          # 01, 1
        "Function_2_2AB",          # 02, 2
        "Function_3_F65",          # 03, 3
        "Function_4_2519",         # 04, 4
        "Function_5_28C0",         # 05, 5
        "Function_6_3116",         # 06, 6
        "Function_7_3157",         # 07, 7
        "Function_8_319D",         # 08, 8
        "Function_9_3348",         # 09, 9
        "Function_10_334C",        # 0A, 10
        "Function_11_3350",        # 0B, 11
    )


    def Function_0_206(): pass

    label("Function_0_206")

    OP_72(0x402, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x1002, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_255")
    SetChrFlags(0x15, 0x80)
    SetChrPos(0x13, 4510, 6000, -1100, 90)
    SetChrPos(0x14, 4510, 6000, -100, 90)
    Jump("loc_270")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_25F")
    Jump("loc_270")

    label("loc_25F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_269")
    Jump("loc_270")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_270")

    label("loc_270")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_292")
    OP_A3(0x2504)
    Event(0, 5)

    label("loc_292")

    Return()

    # Function_0_206 end

    def Function_1_293(): pass

    label("Function_1_293")

    OP_16(0x2, 0xFA0, 0xFFFE5A20, 0xFFFE13D0, 0x23004B)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_293 end

    def Function_2_2AB(): pass

    label("Function_2_2AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_7AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 5)), scpexpr(EXPR_END)), "loc_527")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A9")
    OP_4A(0x14, 255)

    ChrTalk(    #0
        0xFE,
        (
            "It's something you get when scary monsters\x01",
            "come after you and you almost fall off cliffs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "This riddle is really hard!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_37C")

    ChrTalk(    #2
        0x14,
        "#823F...Kindly do some work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A2")

    label("loc_37C")


    NpcTalk(    #3
        0x14,
        "Man",
        "#823F...Kindly do some work.\x02",
    )

    CloseMessageWindow()

    label("loc_3A2")

    OP_4B(0x14, 255)
    Jump("loc_405")

    label("loc_3A9")


    ChrTalk(    #4
        0xFE,
        (
            "Why do you have to almost fall off a cliff\x01",
            "to get happiness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "It's a mystery...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_405")

    Jump("loc_524")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_494")

    ChrTalk(    #6
        0xFE,
        (
            "It'd be really nice if we got as many customers\x01",
            "as the department store in Grancel does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "They'd all be very welcome! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_524")

    label("loc_494")


    ChrTalk(    #8
        0xFE,
        "I hope lots of people come to the bazaar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It'd be really nice if we got as many customers\x01",
            "as the department store in Grancel does.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_524")

    Jump("loc_7A7")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_6A6")

    ChrTalk(    #10
        0xFE,
        "Huh? Mary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "What happened to Polly? Isn't she with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x14E,
        (
            "#1713FU-Umm...\x02\x03",

            "#1712FShe's playing with Clem and Daniel now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Aww? Really? I wanted her to tell me more\x01",
            "about those happiness stone thingies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Can you tell me about them instead, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14E,
        (
            "#1714FU-Umm...\x02\x03",

            "#1713F(...I can't even remember.)\x02\x03",

            "(I don't even want to think about them\x01",
            "right now...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A4")

    label("loc_6A6")


    ChrTalk(    #16
        0xFE,
        "Huh? Mary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "What happened to Polly? Isn't she with you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14E,
        (
            "#1713FU-Umm...\x02\x03",

            "#1712FShe's playing with Clem and Daniel now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Aww? Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I hope she comes back to the bazaar later...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14E,
        "#1710FW-Well, I'll let her know you'd like that.\x02",
    )

    CloseMessageWindow()

    label("loc_7A4")

    OP_A2(0x2F3D)

    label("loc_7A7")

    Jump("loc_F61")

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_C27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_909")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_840")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #22
        0xFE,
        (
            "It's something you get when scary monsters\x01",
            "come after you and you almost fall off cliffs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "...I don't know!\x02",
    )

    CloseMessageWindow()
    Jump("loc_906")

    label("loc_840")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #24
        0xFE,
        (
            "A name like happiness stone made it sound\x01",
            "so nice...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x14F, 400)
    Sleep(500)

    ChrTalk(    #25
        0xFE,
        (
            "Scary monsters and dangerous cliffs, not so\x01",
            "much... Maybe this is some kind of riddle?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_906")

    Jump("loc_C24")

    label("loc_909")


    ChrTalk(    #26
        0x14E,
        (
            "#1710FHey, Lucia? Have you ever heard of a happiness\x01",
            "stone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "...A what?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0xFE)

    ChrTalk(    #28
        0xFE,
        "Tell me more! Tell me more!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14E,
        "#1714F(W-Wow... That's some smile.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "I want to know everything you know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Tell me! Tell meeeeee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x14E,
        (
            "#1719FI can't. It's a secret!\x02\x03",

            "#1711FAlthough, I suppose I could tell you\x01",
            "a liiiiiittle bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Tell meee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x14F,
        (
            "#1731FUmm... It's something you get when scary\x01",
            "monsters come after you and you almost\x01",
            "fall off cliffs!\x02\x03",

            "#1732FBig, scary cliffs!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(1500)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x10, 0x13, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    TurnDirection(0x14E, 0x14F, 500)
    Sleep(500)

    ChrTalk(    #35
        0x14E,
        (
            "#1714F(Umm... She's trying to retell O'Neil's story,\x01",
            "isn't she?)\x02\x03",

            "#1712F(It's somehow got a lot less impact when Polly\x01",
            "tells it...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_63(0xFE)
    Sleep(500)

    ChrTalk(    #36
        0xFE,
        "Scary monsters?\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x20)

    ChrTalk(    #37
        0xFE,
        "#4SEeeeeek!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x1F4)
    CloseMessageWindow()
    ClearMapFlags(0x20)
    Sleep(200)
    OP_A2(0x2F3C)
    OP_A3(0x1)

    label("loc_C24")

    Jump("loc_F61")

    label("loc_C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 3)), scpexpr(EXPR_END)), "loc_E49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB2")
    OP_8C(0xFE, 0, 0)
    OP_4A(0x14, 255)

    ChrTalk(    #38
        0xFE,
        "Wait! A bit more to the right!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14, 45, 400)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_CA1")

    ChrTalk(    #39
        0x14,
        "#822FHmm? What, like here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC5")

    label("loc_CA1")


    NpcTalk(    #40
        0x14,
        "Man",
        "#822FHmm? What, like here?\x02",
    )

    CloseMessageWindow()

    label("loc_CC5")


    ChrTalk(    #41
        0xFE,
        "No, that's too far to the right!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_D06")

    ChrTalk(    #42
        0x14,
        "#822FUmm...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1B")

    label("loc_D06")


    NpcTalk(    #43
        0x14,
        "Man",
        "#822FUmm...\x02",
    )

    CloseMessageWindow()

    label("loc_D1B")

    OP_8C(0x14, 0, 400)
    Sleep(400)

    ChrTalk(    #44
        0xFE,
        "That's too far to the left now.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_D81")

    ChrTalk(    #45
        0x14,
        "#823FI can't win here, can I...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_D81")


    NpcTalk(    #46
        0x14,
        "Man",
        "#823FI can't win here, can I...?\x02",
    )

    CloseMessageWindow()

    label("loc_DAB")

    OP_4B(0x14, 255)
    Jump("loc_E46")

    label("loc_DB2")


    ChrTalk(    #47
        0xFE,
        (
            "I can't reach high enough on my own,\x01",
            "so I had to get Mr. Bracer here to help\x01",
            "put the posters up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "...I can't remember his name, though.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E46")

    Jump("loc_F57")

    label("loc_E49")


    ChrTalk(    #49
        0xFE,
        "Oh, you came after all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14F,
        "#1732FWell, it sounds like fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Oh, it is! You'll have loooads of fun.\x01",
            "I guarantee it! ★\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x14E,
        "#1710FWhere in town is it being held, Lucia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "It's in the cabin attached to the windmill!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Go and buy tooons of stuff, okay?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3B)

    label("loc_F57")

    Jump("loc_F61")

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_F61")

    label("loc_F61")

    TalkEnd(0xFE)
    Return()

    # Function_2_2AB end

    def Function_3_F65(): pass

    label("Function_3_F65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1197")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 0)), scpexpr(EXPR_END)), "loc_107C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(    #55
        0x14,
        (
            "#820FIf you need help with anything, don't hesitate\x01",
            "to ask. Helping people is my job, after all!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1079")

    label("loc_FED")


    ChrTalk(    #56
        0x14,
        (
            "#820FIf you need help with anything, don't hesitate\x01",
            "to ask, all right?\x02\x03",

            "I mean, I'm a bracer, after all. Helping people\x01",
            "is our job.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1079")

    Jump("loc_1194")

    label("loc_107C")


    ChrTalk(    #57
        0x14,
        (
            "#821FWelcome, welcome! ...Oh, wait. You're that girl\x01",
            "from earlier.\x02\x03",

            "#820FSomething wrong? Can I help you with anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x14E,
        (
            "#1713FN-No, it's nothing...\x02\x03",

            "#1712F(It's not like this is the first time Polly has\x01",
            "done something weird...)\x02\x03",

            "(I'll be able to find her on my own!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F40)

    label("loc_1194")

    Jump("loc_1312")

    label("loc_1197")

    OP_8C(0x14, 90, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #59
        0x14,
        "Man",
        "Umm... Can I help you?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #60
        0x14E,
        (
            "#1714FWait, I remember now!\x02\x03",

            "Your name was Black! ...Wasn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    NpcTalk(    #61
        0x14,
        "Man",
        "That's not even close...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x14,
        (
            "#823F...The name's Grant, actually. I'd appreciate it\x01",
            "if you tried to remember it this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_1312")

    Jump("loc_2515")

    label("loc_1315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_20DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_1BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 7)), scpexpr(EXPR_END)), "loc_1639")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_1504")
    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13BB")

    ChrTalk(    #63
        0x13,
        (
            "But you've got to almost fall of a cliff to get\x01",
            "one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x14,
        (
            "#823F(This story makes less sense to me by the\x01",
            "minute...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1501")

    label("loc_13BB")


    ChrTalk(    #65
        0x13,
        (
            "So Mary and Polly were telling me about this\x01",
            "happiness stone thingy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x14,
        (
            "#825FYeah... You've told me a thousand times now...\x02\x03",

            "So is this spot okay for the poster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x13,
        (
            "It's supposed to be really shiny, though!\x01",
            "Doesn't that sound so nice? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x14,
        (
            "#825F(Girls really do love these kinds of stories,\x01",
            "don't they?)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1501")

    Jump("loc_1636")

    label("loc_1504")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_158A")

    ChrTalk(    #69
        0x14,
        (
            "#820FI won't fault someone for being serious about\x01",
            "their work, but she's not exactly a very\x01",
            "considerate boss...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1636")

    label("loc_158A")


    ChrTalk(    #70
        0x14,
        "#820FIf you ask me, this spot's just fine for it, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x13,
        "No! There'll be no corner cutting on my watch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        "#825F*sigh* She really is a demanding mistress...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1636")

    Jump("loc_1BDF")

    label("loc_1639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x140, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17C6")

    ChrTalk(    #73
        0x14,
        "#821FOh...\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #74
        (
            "\x07\x05Grant looks at the Emergency Puppet that Mary is\x01",
            "holding.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #75
        0x14,
        (
            "#823FN-No, it's nothing...\x02\x03",

            "(That was one of the items I donated to the\x01",
            "bazaar myself...)\x02\x03",

            "#825F(I'm not sure she's the best person for it to\x01",
            "go to, but oh well...)\x02\x03",

            "#821FTake good care of that, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x14E,
        "#1714FO...kay...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_1BDF")

    label("loc_17C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x139, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_18C3")

    ChrTalk(    #77
        0x14,
        "#821FOh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    OP_63(0x14F)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #78
        (
            "\x07\x05Grant looks at the Woolly Knit-Hat that Polly is\x01",
            "wearing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #79
        0x14,
        (
            "#823FN-No, it's nothing...\x02\x03",

            "#825F(I was the one who donated that...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_1BDF")

    label("loc_18C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 4)), scpexpr(EXPR_END)), "loc_1AA5")
    OP_8C(0x14, 0, 0)
    OP_4A(0x13, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1958")

    ChrTalk(    #80
        0x13,
        (
            "But you've got to almost fall of a cliff to get\x01",
            "one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x14,
        (
            "#823F(This story makes less sense to me by the\x01",
            "minute...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA2")

    label("loc_1958")


    ChrTalk(    #82
        0x13,
        (
            "So Mary and Polly were telling me about this\x01",
            "happiness stone thingy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        (
            "#825FYeah... You've told me a thousand times now...\x02\x03",

            "So is this spot okay for the poster?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x13,
        (
            "It's supposed to be really shiny, though!\x01",
            "Doesn't that sound so nice? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x14,
        (
            "#823F(Girls really do love these kinds of stories,\x01",
            "don't they?)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_A2(0x1)

    label("loc_1AA2")

    Jump("loc_1BDF")

    label("loc_1AA5")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B2B")

    ChrTalk(    #86
        0x14,
        (
            "#825FI won't fault someone for being serious about\x01",
            "their work, but she's not exactly a very\x01",
            "considerate boss...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDF")

    label("loc_1B2B")

    OP_4A(0x13, 255)

    ChrTalk(    #87
        0x14,
        (
            "#820FIf you ask me, this spot's just fine for it,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x13,
        "No! There'll be no corner cutting on my watch!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x14,
        "#825F*sigh* She really is a demanding mistress...\x02",
    )

    CloseMessageWindow()
    OP_4B(0x13, 255)
    OP_A2(0x1)

    label("loc_1BDF")

    Jump("loc_20DC")

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 7)), scpexpr(EXPR_END)), "loc_1D19")
    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #90
        0x14,
        "Man",
        "Umm... Can I help you?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #91
        0x14E,
        (
            "#1714FOh, I remember your name now!\x02\x03",

            "#1711FIt's Black!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #92
        0x14,
        (
            "#823F...It's Grant. Please try and remember it this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)
    Jump("loc_20DC")

    label("loc_1D19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x140, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EB2")

    NpcTalk(    #93
        0x14,
        "Man",
        "Oh...\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x07\x05Grant looks at the Emergency Puppet that Mary is\x01",
            "holding.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #95
        0x14,
        "Man",
        "N-No, it's nothing...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #96
        0x14,
        "Man",
        (
            "(That was one of the items I donated to the\x01",
            "bazaar myself...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #97
        0x14,
        "Man",
        (
            "(I'm not sure she's the best person for it to\x01",
            "go to, but oh well...)\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #98
        0x14,
        "Man",
        "Take good care of that, all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x14E,
        "#1714FO...kay...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_20DC")

    label("loc_1EB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x139, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FB5")

    NpcTalk(    #100
        0x14,
        "Man",
        "Oh...\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)
    OP_63(0x14E)
    OP_63(0x14F)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #101
        (
            "\x07\x05Grant looks at the Woolly Knit-Hat that Polly is\x01",
            "wearing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    NpcTalk(    #102
        0x14,
        "Man",
        "N-No, it's nothing...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #103
        0x14,
        "Man",
        "(I was the one who donated that...)\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F3F)
    Jump("loc_20DC")

    label("loc_1FB5")

    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #104
        0x14,
        "Man",
        "Umm... Can I help you?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #105
        0x14E,
        (
            "#1711FOh, I remember your name now!\x02\x03",

            "It's Black!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #106
        0x14,
        (
            "#823F...It's Grant. Please try and remember it this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_20DC")

    Jump("loc_2515")

    label("loc_20DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_250E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 6)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E7, 3)), scpexpr(EXPR_END)), "loc_2227")
    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2135")

    ChrTalk(    #107
        0x14,
        "#820FThis seems like it'll be a good spot.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2224")

    label("loc_2135")


    ChrTalk(    #108
        0x14,
        (
            "#822FHmm... I don't want to put it too high up, or no\x01",
            "one will be able to read it.\x02\x03",

            "#821FWell, I doubt most adults will have too much\x01",
            "trouble, but children and the elderly will want\x01",
            "to go, too. A little on the low side seems best.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2224")

    Jump("loc_23D1")

    label("loc_2227")

    OP_8C(0x14, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22DC")

    ChrTalk(    #109
        0x14,
        (
            "#823FI'm supposed to be affiliated with the Bose\x01",
            "branch, but I haven't been back there in a\x01",
            "month...\x02\x03",

            "*sigh* I seem to be spending all my time in\x01",
            "Ruan lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23D1")

    label("loc_22DC")


    ChrTalk(    #110
        0x14,
        (
            "#823FJean sure knows how to work people to the\x01",
            "bone...\x02\x03",

            "Do I really look like the kind of person who's\x01",
            "suited to help out at a bazaar? Really?\x02\x03",

            "#824FThis was supposed to be Carna's job! I hope\x01",
            "she doesn't think I'm going to forget this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_23D1")

    Jump("loc_250B")

    label("loc_23D4")

    OP_8C(0x14, 0, 0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    TurnDirection(0x14, 0x14E, 400)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x14)

    NpcTalk(    #111
        0x14,
        "Man",
        "Umm... Can I help you?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_63(0x14E)
    Sleep(500)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #112
        0x14E,
        (
            "#1714FOh, I remember your name now!\x02\x03",

            "#1711FIt's Black!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_63(0x14)

    ChrTalk(    #113
        0x14,
        (
            "#823F...It's Grant. Do me a favor and try remembering\x01",
            "it next time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F3E)

    label("loc_250B")

    Jump("loc_2515")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_2515")

    label("loc_2515")

    TalkEnd(0xFE)
    Return()

    # Function_3_F65 end

    def Function_4_2519(): pass

    label("Function_4_2519")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_2526")
    Jump("loc_28BC")

    label("loc_2526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 3)), scpexpr(EXPR_END)), "loc_2679")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25E8")

    ChrTalk(    #114
        0xFE,
        (
            "...I'm guessing he must live here, come to think\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I doubt he'd look like he was having as much fun\x01",
            "helping with the bazaar as he does if he wasn't\x01",
            "from Manoria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2676")

    label("loc_25E8")


    ChrTalk(    #116
        0xFE,
        "I wonder who that man with Lucia is, anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I do see him around from time to time, but I've\x01",
            "never asked... Maybe he lives here?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2676")

    Jump("loc_28BC")

    label("loc_2679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_2780")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2720")

    ChrTalk(    #118
        0xFE,
        (
            "I'm sure at least a few people would want to buy\x01",
            "flowers if I sold them over there.\x02\x03",

            "I mean, who doesn't feel relaxed looking at pretty\x01",
            "flowers?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_277D")

    label("loc_2720")


    ChrTalk(    #119
        0xFE,
        "I think it's about noon now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "Time to close up shop and head over to the bazaar!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_277D")

    Jump("loc_28BC")

    label("loc_2780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_28B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27FA")

    ChrTalk(    #121
        0xFE,
        "I wish the morning would end already.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I just can't seem to relax and focus on my work\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B2")

    label("loc_27FA")


    ChrTalk(    #123
        0xFE,
        "There's a bazaar starting here in town today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I'm planning to head over there to help out this\x01",
            "afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Heehee. Maybe I should sell a few potted plants\x01",
            "there, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_28B2")

    Jump("loc_28BC")

    label("loc_28B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_28BC")

    label("loc_28BC")

    TalkEnd(0xFE)
    Return()

    # Function_4_2519 end

    def Function_5_28C0(): pass

    label("Function_5_28C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-1560, 6000, -3200, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(328000, 0)
    OP_6E(340, 0)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    SetChrPos(0x14E, 3300, 6500, -2840, 90)
    SetChrPos(0x14F, 3300, 6500, -2840, 90)

    def lambda_293B():
        OP_6D(5100, 6000, 960, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_293B)

    def lambda_2953():
        OP_67(0, 6360, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2953)

    def lambda_296B():
        OP_6B(2440, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_296B)

    def lambda_297B():
        OP_6C(318000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_297B)

    def lambda_298B():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_298B)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x1C2, 0x0, 0x64)
    OP_0D()
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    Sleep(200)
    OP_43(0x14E, 0x2, 0x0, 0x6)
    OP_43(0x14F, 0x2, 0x0, 0x7)
    Sleep(2500)
    OP_72(0x2, 0x8)
    ExitThread()
    OP_6F(0x2, 29)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x2, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_23(0x1C2)
    WaitChrThread(0x14E, 0x2)
    WaitChrThread(0x14F, 0x2)

    ChrTalk(    #126
        0x14E,
        "#1719FWhew...\x02",
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    OP_8C(0x14E, 180, 500)
    Sleep(400)

    ChrTalk(    #127
        0x14E,
        (
            "#1718FWh-What should we do, Polly?! \x02\x03",

            "This actually sounds like it might be true\x01",
            "after all!\x02\x03",

            "#1903FMaybe there really IS something up in the \x01",
            "mountains!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14F,
        "#1730FUmm... Mary?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(400)

    ChrTalk(    #129
        0x14E,
        (
            "#1719F(The golden glow, tall mountains... It all fits.)\x02\x03",

            "#1711F(Maybe there really is a happiness stone to\x01",
            "be found there!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x14F,
        "#1733FShe's not listening...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x14E,
        (
            "#1719F...\x02\x03",

            "I-I suppose it wouldn't hurt to go and take\x01",
            "a quick peek up there, would it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14E, 180, 400)
    Sleep(400)

    ChrTalk(    #132
        0x14E,
        "#1718FSay, Polly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x14F,
        (
            "#1731FYou know Clem and Daniel came to the\x01",
            "bazaar earlier, Mary?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)
    Sleep(200)

    ChrTalk(    #134
        0x14E,
        "#1714F#3S...What?!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #135
        0x14F,
        (
            "#1730FThey came to do some shopping and said they\x01",
            "were going into the Krone mountains.\x02\x03",

            "They said they're all ready, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x14E,
        "#1714FSeriously?! I didn't even notice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x14F,
        "#1731FWell, you are spacing out a lot lately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x14E,
        (
            "#1715FI can't believe they're thinking of heading into\x01",
            "the mountains!\x02\x03",

            "Matron Theresa is always telling us not to go\x01",
            "any farther from the orphanage than Manoria!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x14F,
        "#1733FBut you wanna go into the mountains, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x14E,
        (
            "#1900FThat's... Uhh...\x02\x03",

            "#1903FI-I'm planning on doing it to get her a birthday\x01",
            "present! That's very different! And it'll only be\x01",
            "for a minute or two!\x02\x03",

            "Besides, we've got to go and bring those two home\x01",
            "now. That's important enough on its own! Then we\x01",
            "can just search for the present while we're there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x14F,
        (
            "#1731F...\x02\x03",

            "#1730FWe can't tell the matron about this, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x14E,
        (
            "#1710FAbsolutely not. She can't know about the birthday\x01",
            "present, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_302C():
        OP_8E(0xFE, 0x15CC, 0x1770, 0x104, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_302C)
    WaitChrThread(0x14E, 0x1)

    ChrTalk(    #143
        0x14E,
        "#1718F#11PLet's go! Stick close to me, Polly!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 400)
    Sleep(600)

    def lambda_308B():
        OP_8E(0xFE, 0x15CC, 0x1770, 0x2044, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_308B)

    def lambda_30A6():
        OP_8E(0xFE, 0x1644, 0x1770, 0x1D9C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_30A6)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x14E, 0x1)
    OP_44(0x14F, 0x2)
    SetChrPos(0x14E, 4120, 4000, 15700, 0)
    SetChrPos(0x14F, 4120, 4000, 15700, 0)
    ClearChrFlags(0x14E, 0x40)
    OP_71(0x2, 0x8)
    ExitThread()
    OP_6F(0x2, 0)
    OP_A2(0x2F21)
    EventEnd(0x0)
    FadeToBright(1000, 0)
    Return()

    # Function_5_28C0 end

    def Function_6_3116(): pass

    label("Function_6_3116")


    def lambda_311C():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFF5D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_311C)
    WaitChrThread(0x14E, 0x1)

    def lambda_313C():
        OP_8E(0xFE, 0x1644, 0x1770, 0x49C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_313C)
    WaitChrThread(0x14E, 0x1)
    Return()

    # Function_6_3116 end

    def Function_7_3157(): pass

    label("Function_7_3157")

    Sleep(1200)

    def lambda_3162():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFF5D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_3162)
    WaitChrThread(0x14F, 0x1)

    def lambda_3182():
        OP_8E(0xFE, 0x1644, 0x1770, 0xFFFFFE5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_3182)
    WaitChrThread(0x14F, 0x1)
    Return()

    # Function_7_3157 end

    def Function_8_319D(): pass

    label("Function_8_319D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #144
        (
            "\x07\x05     ●3rd Manoria Village Bazaar Now Open!●\x01\x01",
            "Everyone's favorite time of year is finally upon us!\x01",
            "Manoria's famous bazaar will be held in the windmill\x01",
            "cabin for the next three days, and all are welcome!\x01",
            "If you have any unwanted items you would be willing\x01",
            "to donate, please do!\x01",
            "Come join us--you never know what you'll find!\x01\x01",
            "            Manoria Bazaar Organization Committee\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_319D end

    def Function_9_3348(): pass

    label("Function_9_3348")

    SetPlaceName(0x58)
    Return()

    # Function_9_3348 end

    def Function_10_334C(): pass

    label("Function_10_334C")

    SetPlaceName(0x57)
    Return()

    # Function_10_334C end

    def Function_11_3350(): pass

    label("Function_11_3350")

    SetPlaceName(0x59)
    Return()

    # Function_11_3350 end

    SaveToFile()

Try(main)
