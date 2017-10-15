from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3132   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3132_1 ._SN',
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
        'Martina',                              # 9
        'Emma',                                 # 10
        'Noticia',                              # 11
        'Dodge',                                # 12
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
        'ED6_DT07/CH01210 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01210P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
    )

    DeclNpc(
        X                   = -1700,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 192,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 36440,
        Z                   = 0,
        Y                   = 50580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 68210,
        Z                   = 0,
        Y                   = 92140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 68100,
        Z                   = 0,
        Y                   = 56310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -1290,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = -1700,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4000,
        TriggerZ            = 0,
        TriggerY            = 4000,
        TriggerRange        = 800,
        ActorX              = -4000,
        ActorZ              = 1000,
        ActorY              = 4000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_204",          # 01, 1
        "Function_2_205",          # 02, 2
        "Function_3_229",          # 03, 3
        "Function_4_22E",          # 04, 4
        "Function_5_EBE",          # 05, 5
        "Function_6_15C4",         # 06, 6
        "Function_7_18E9",         # 07, 7
        "Function_8_1C4E",         # 08, 8
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C3")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1B9")
    SetChrPos(0x9, 33350, 0, 55500, 0)
    Jump("loc_1C0")

    label("loc_1B9")

    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_1C0")

    Jump("loc_203")

    label("loc_1C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1DE")
    SetChrPos(0x9, 5590, 0, 134800, 348)
    Jump("loc_203")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1ED")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_203")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1F7")
    Jump("loc_203")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_203")
    ClearChrFlags(0xA, 0x80)

    label("loc_203")

    Return()

    # Function_0_192 end

    def Function_1_204(): pass

    label("Function_1_204")

    Return()

    # Function_1_204 end

    def Function_2_205(): pass

    label("Function_2_205")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_228")
    OP_8D(0xFE, 33380, 54030, 36670, 49190, 2000)
    Jump("Function_2_205")

    label("loc_228")

    Return()

    # Function_2_205 end

    def Function_3_229(): pass

    label("Function_3_229")

    Call(0, 4)
    Return()

    # Function_3_229 end

    def Function_4_22E(): pass

    label("Function_4_22E")

    TalkBegin(0x8)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B")
    OP_A9(0x99)
    TalkEnd(0x8)
    Return()

    label("loc_24B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C")
    TalkEnd(0x8)
    Return()

    label("loc_25C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_288")
    Call(1, 1)
    Jump("loc_28C")

    label("loc_288")

    Call(1, 0)

    label("loc_28C")

    Jump("loc_EBA")

    label("loc_28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_335")

    ChrTalk(    #0
        0x8,
        (
            "Given the situation, there aren't\x01",
            "many guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Looks like my days of putting up with this will\x01",
            "continue until the scheduled liners resume.\x01",
            "*sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41A")

    ChrTalk(    #2
        0x8,
        "Oh, bracers. It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "The Zahnrad Hotel is open for business,\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "There will be some inconveniences during this\x01",
            "period, but feel free to stay with us if you\x01",
            "would like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C7")

    label("loc_41A")


    ChrTalk(    #5
        0x8,
        (
            "Welcome. The Zahnrad Hotel is open for business,\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "There will be some inconveniences during this\x01",
            "period, but feel free to stay with us if you\x01",
            "would like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C7")

    OP_A2(0x0)
    Jump("loc_571")

    label("loc_4CD")


    ChrTalk(    #7
        0x8,
        (
            "The Zahnrad Hotel is open for business,\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "There will be some inconveniences during this\x01",
            "period, but feel free to stay with us if you\x01",
            "would like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_571")

    Jump("loc_EBA")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_A79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_9D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_936")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 3)), scpexpr(EXPR_END)), "loc_8AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6D2")

    ChrTalk(    #9
        0x8,
        (
            "Once she heard there wouldn't be any more\x01",
            "earthquakes, Emma cheered right back up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Well, she's a little bit TOO cheerful, really.\x01",
            "I wish she would settle down and stop\x01",
            "being such a nuisance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "*sigh* Couldn't she find some middle ground\x01",
            "between being energetic or in the dumps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80E")

    label("loc_6D2")


    ChrTalk(    #12
        0x8,
        (
            "According to the announcement from the central\x01",
            "factory, there won't be any more earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "Thanks to that, Emma's cheered right back up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Well, she's a little bit TOO cheerful, really.\x01",
            "I wish she would settle down and stop\x01",
            "being such a nuisance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        "*sigh* I feel like I wasted my time worrying.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_80E")

    Jump("loc_8A8")

    label("loc_811")


    ChrTalk(    #16
        0x8,
        (
            "Everyone, good work. If you're looking\x01",
            "for Jimmy, he returned a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "He seemed to be in some hurry, though,\x01",
            "and checked out immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A8")

    Jump("loc_933")

    label("loc_8AB")


    ChrTalk(    #18
        0x8,
        "Ah, everyone. Good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Just a bit ago Jimmy returned safely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "Phew!\x01",
            "I feel as if a burden's lifted from my chest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1643)
    OP_A2(0x1)

    label("loc_933")

    Jump("loc_9CE")

    label("loc_936")


    ChrTalk(    #21
        0x8,
        (
            "It seem the missing guest has\x01",
            "headed to the Limestone Cave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "We tried very hard to stop him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "Well, then, please take care of our guest.\x02",
    )

    CloseMessageWindow()

    label("loc_9CE")

    Jump("loc_A76")

    label("loc_9D1")


    ChrTalk(    #24
        0x8,
        (
            "I'm overjoyed to hear the safety announcement\x01",
            "regarding the earthquakes, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "I have another concern now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "*sigh* It's just one thing after another.\x02",
    )

    CloseMessageWindow()

    label("loc_A76")

    Jump("loc_EBA")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AFC")

    ChrTalk(    #27
        0x8,
        (
            "One of our employees, Emma, is still\x01",
            "scared of the earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "The way she's depressed has me worried.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC1")

    label("loc_AFC")


    ChrTalk(    #29
        0x8,
        (
            "One of our employees, Emma, is still\x01",
            "scared of the earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "Normally she's far too energetic,\x01",
            "so it's almost nice for a change, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "The way she's depressed has me worried.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BC1")

    Jump("loc_EBA")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_D50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C76")

    ChrTalk(    #32
        0x8,
        (
            "Calm and quiet like today is far\x01",
            "better than the normal Emma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "After all, usually she's practically screaming\x01",
            "greetings at the guests and scaring them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4D")

    label("loc_C76")


    ChrTalk(    #34
        0x8,
        (
            "One of our employees, Emma, is so scared of the\x01",
            "earthquakes that she's completely lost her energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "Still, being a little scared might just be best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "She normally has far too much energy,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D4D")

    Jump("loc_EBA")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E14")

    ChrTalk(    #37
        0x8,
        (
            "Of course, our hotel is well equipped to\x01",
            "handle earthquakes. It's very resilient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "We've been certified as having the highest\x01",
            "of safety standards by the central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBA")

    label("loc_E14")


    ChrTalk(    #39
        0x8,
        "Welcome. Welcome to the Zahnrad Hotel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "I was surprised by the earthquake,\x01",
            "but it really has been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        "They're quite rare, so you needn't worry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EBA")

    TalkEnd(0x8)
    Return()

    # Function_4_22E end

    def Function_5_EBE(): pass

    label("Function_5_EBE")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_FEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7F")

    ChrTalk(    #42
        0xFE,
        "Soot collects on maps, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I've got to clean them every once in a while\x01",
            "or they might turn pitch black...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "*siiigh* Orbment lights are soooo much better.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_FE9")

    label("loc_F7F")


    ChrTalk(    #45
        0xFE,
        (
            "Lamps just leave soot everywhere.\x01",
            "It's annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Yeah, orbment lights are much more convenient.\x02",
    )

    CloseMessageWindow()

    label("loc_FE9")

    Jump("loc_15C0")

    label("loc_FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_112C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C5")

    ChrTalk(    #47
        0xFE,
        (
            "The orbment lights won't turn on,\x01",
            "so we're using lamps, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "It's so dark at night it's kind of scary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Every time I meet a guest in the dark\x01",
            "I feel like my heart's gonna explode.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1129")

    label("loc_10C5")


    ChrTalk(    #50
        0xFE,
        "Lamp light is really murky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Th-Thanks to that, the corridors sure are\x01",
            "scary at night...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1129")

    Jump("loc_15C0")

    label("loc_112C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_126A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_118B")

    ChrTalk(    #52
        0xFE,
        "Now, first we'll start with cleaning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I'm really gonna do it today!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1267")

    label("loc_118B")


    ChrTalk(    #54
        0xFE,
        "WELCOME TO THE ZAHNRAD HOTEL!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Heehee, did you hear?! The earthquakes are done!\x01",
            "The earthquakes are doooooone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "One of the guests told me there\x01",
            "was an announcement about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I feel 1000% better now!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1267")

    Jump("loc_15C0")

    label("loc_126A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12F2")

    ChrTalk(    #58
        0xFE,
        (
            "*siiigh* Just thinking about the earthquakes\x01",
            "kills my appetite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Probably, next I'll end up an insomniac...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1394")

    label("loc_12F2")


    ChrTalk(    #60
        0xFE,
        "Ah, welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "*siiigh* Just thinking about the earthquakes\x01",
            "kills my appetite...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Probably, next I'll end up an insomniac...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Ah...hahaha...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1394")

    Jump("loc_15C0")

    label("loc_1397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_14D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_142E")

    ChrTalk(    #64
        0xFE,
        (
            "Thinking that another earthquake might\x01",
            "come is totally distracting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "The manager seems pretty happy for some\x01",
            "reason, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14CF")

    label("loc_142E")


    ChrTalk(    #66
        0xFE,
        "W-Welcome...guest.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Thinking that another earthquake might\x01",
            "come is totally distracting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The manager seems pretty happy for some\x01",
            "reason, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14CF")

    Jump("loc_15C0")

    label("loc_14D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_15C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1550")

    ChrTalk(    #69
        0xFE,
        (
            "I-If it shakes again, what do I do?\x01",
            "What do I do?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "Ooooh, it's so scary I can't get anything done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_1550")


    ChrTalk(    #71
        0xFE,
        "W-Welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Oooh, the ground still feels like it's shaking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "I-It's so scary! I can't work!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_15C0")

    TalkEnd(0x9)
    Return()

    # Function_5_EBE end

    def Function_6_15C4(): pass

    label("Function_6_15C4")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_171E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_167A")

    ChrTalk(    #74
        0xFE,
        (
            "While I was looking into the scoop at the central\x01",
            "factory I heard some interesting stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Now, time to put together an article\x01",
            "on the next ship back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171B")

    label("loc_167A")


    ChrTalk(    #76
        0xFE,
        (
            "While I was looking into the scoop at the central\x01",
            "factory I heard some interesting stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "It isn't called the brain of the kingdom\x01",
            "for no reason!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_171B")

    Jump("loc_18E5")

    label("loc_171E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_18E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_17F6")

    ChrTalk(    #78
        0xFE,
        (
            "As a reporter from the Liberl News I can't\x01",
            "ignore talk about the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "While I'm here checking out the new model engine\x01",
            "I'll also collect opinions from the brains around\x01",
            "the factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E5")

    label("loc_17F6")


    ChrTalk(    #80
        0xFE,
        "Hmm, an earthquake, how rare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Of course, as a reporter with the Liberl\x01",
            "News, I'm going to follow up on this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "While I'm here checking out the new model engine\x01",
            "I'll also collect opinions from the brains around\x01",
            "the factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_18E5")

    TalkEnd(0xA)
    Return()

    # Function_6_15C4 end

    def Function_7_18E9(): pass

    label("Function_7_18E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F0")

    ChrTalk(    #83
        0xFE,
        (
            "Apparently they STILL don't know why orbments\x01",
            "aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "With the central factory in that state,\x01",
            "I suppose it's obvious research wouldn't\x01",
            "get anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Thinking about that, the severity\x01",
            "of the situation's pretty clear.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1A97")

    label("loc_19F0")


    ChrTalk(    #86
        0xFE,
        (
            "Apparently they STILL don't know why orbments\x01",
            "aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "With the central factory in that state,\x01",
            "I suppose it's obvious research wouldn't\x01",
            "get anywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A97")

    Jump("loc_1C4A")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC2")

    ChrTalk(    #88
        0xFE,
        (
            "I came from the Republic to buy\x01",
            "new model orbments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "It seems like orbments across the whole\x01",
            "city aren't working. It's crazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "The central factory looks like it's out of\x01",
            "commission right now, so it'd probably be\x01",
            "hard to get anywhere with a business deal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1C4A")

    label("loc_1BC2")


    ChrTalk(    #91
        0xFE,
        (
            "I came from the Republic to buy\x01",
            "new model orbments, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "At this rate, any chance I have at a business\x01",
            "deal is shot. *sigh*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4A")

    TalkEnd(0xFE)
    Return()

    # Function_7_18E9 end

    def Function_8_1C4E(): pass

    label("Function_8_1C4E")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #93
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1C4E end

    SaveToFile()

Try(main)
