from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0312_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0312   ._SN',
            'ED6_DT21/E0312_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #0
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C) Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W........#20WOK!\x01",
            "#200W　#20W\x01",
            "#1SDatabase accessed.\x01",
            "Please input search term.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_75AA")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x37, 0x50, 0x1)
    OP_CC(0x1, 0x0, "[Central Factory]")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_END)), "loc_1F6")
    OP_CC(0x1, 0x0, "[Data Crystals]")

    label("loc_1F6")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20D"),
        (1, "loc_1DAF"),
        (SWITCH_DEFAULT, "loc_759A"),
    )


    label("loc_20D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DAF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "[Establishment]\x01",       # 0
            "[Universal Tech]\x01",      # 1
            "[Related Topics]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_277"),
        (1, "loc_B5F"),
        (2, "loc_19B0"),
        (SWITCH_DEFAULT, "loc_1D9F"),
    )


    label("loc_277")


    AnonymousTalk(    #1
        (
            "\x07\x02#1S[S1154] (S: Septian Calendar) - Death of Prof.\x01",
            "C. Epstein in the sovereign state of Leman.\x01",
            "[S1155] Professor A. Russell returns to the Liberl\x01",
            "Kingdom. He proposes the spread of orbment\x01",
            "technology, to a chilly reception.\x01",
            "[S1157] Prof. Russell forms a partnership with\x01",
            "the Zeiss Clockmaker's Union. Together, they\x01",
            "establish the Zeiss Engineering Factory (later\x01",
            "renamed the Central Factory).\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x02#1S[S1160] Edgar III, after an inspection of the\x01",
            "factory, donates a large amount of money to\x01",
            "further its research. Prof. Russell becomes the\x01",
            "first Factory Chief.\x01",
            "[S1162] Edgar III dies, and Alicia II assumes the\x01",
            "throne.\x01",
            "[S1164] Construction is completed on the\x01",
            "Langland Bridge.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x02#1S[S1168] The first orbal-powered airship, the\x01",
            "Calatrava, is completed. (39 failed test flights\x01",
            "before success was achieved.)\x01",
            "[S1173] The Zeiss Engineering Factory is renamed\x01",
            "Zeiss Central Factory and begins sharing\x01",
            "technology with the Verne Company and Reinford\x01",
            "Company.\x01",
            "[S1175] The Liberl Orbalship Corporation is\x01",
            "established, and the transit commuter airship,\x01",
            "the Linde, is commissioned.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x07\x02#1S[S1177] Transit commuter airship, the Cecilia,\x01",
            "is commissioned.\x01",
            "[S1178] Factory airship, the Leibnitz, is\x01",
            "completed.\x01",
            "[S1180] The Zeiss Central Factory is dismantled\x01",
            "and reconstructed at its current site. The\x01",
            "partially-underground factory in the Kaldia\x01",
            "Hills is completed.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x07\x02#1S[S1182] Professor Russell resigns from his\x01",
            "position as Factory Chief and is succeeded by\x01",
            "Murdock.\x01",
            "[S1185] Natural Science and Medical Research\x01",
            "divisions are founded.\x01",
            "[S1187] The passenger ship, Eterna, sinks in\x01",
            "Calvard waters. Crown prince Judis dies.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #6
        (
            "\x07\x02#1S[S1190] The Orbal Network, a joint venture with\x01",
            "the Epstein Foundation, is publicly announced.\x01",
            "[S1192] Outbreak of the Hundred Days War. The\x01",
            "Central Factory is taken by the Erebonian Army.\x01",
            "Prof. Russell develops patrol airships at Leiston\x01",
            "Fortress, which are used to mount a highly\x01",
            "effective counteroffensive, and soon become\x01",
            "central to the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #7
        (
            "\x07\x02#1S[S1193] Liberl and Erebonia sign a peace accord.\x01",
            "Orbment exports to the Erebonian Empire resume.\x01",
            "[S1197] Version 1.0 of the Capel orbal computer\x01",
            "is completed.\x01",
            "[S1199] Development commences on the high-speed\x01",
            "cruiser, the Arseille.\x01",
            "[S1202] The Arseille is completed and flight\x01",
            "tests commence.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAC")

    label("loc_B5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19A0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)

    Menu(
        2,
        55,
        259,
        1,
        (
            "[Orbments]\x01",                # 0
            "[Crystal Circuits]\x01",        # 1
            "[Septium]\x01",                 # 2
            "[Airships]\x01",                # 3
            "[Orbal Weaponry]\x01",          # 4
            "[Tactical Orbments]\x01",       # 5
            "[New Model Orbments]\x01",      # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C17"),
        (1, "loc_DF4"),
        (2, "loc_EFE"),
        (3, "loc_1088"),
        (4, "loc_1286"),
        (5, "loc_14FA"),
        (6, "loc_1789"),
        (SWITCH_DEFAULT, "loc_1990"),
    )


    label("loc_C17")


    AnonymousTalk(    #8
        (
            "\x07\x02#1SEntry: Orbment\x01",
            "General term for devices that draw orbal energy\x01",
            "from septium, invented 50 years ago by Prof. C.\x01",
            "Epstein. The clockwork mechanism inside causes a\x01",
            "reaction between quartz, which in turn produces\x01",
            "a variety of different phenomena. Their greatest\x01",
            "advantages over combustion engines is that the\x01",
            "orbal energy within them is gradually restored\x01",
            "over time and the variety of different phenomena\x01",
            "they can produce. They are also much more\x01",
            "economically efficient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_DF4")


    AnonymousTalk(    #9
        (
            "\x07\x02#1SEntry: Crystal Circuit (Quartz)\x01",
            "An electrical circuit with a crystalline structure\x01",
            "made from processed septium fragments (sepith).\x01",
            "They serve as an energy source but also cause\x01",
            "varied phenomena, which are only seen when they\x01",
            "are placed inside an orbment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_EFE")


    AnonymousTalk(    #10
        (
            "\x07\x02#1SEntry: Septium\x01",
            "A grouping of seven gemstones found throughout\x01",
            "the continent. Prized as jewels for eons, it was\x01",
            "also regarded as a symbol of mystery. The invention\x01",
            "of technology to refine and process septium\x01",
            "fragments too small to use as jewels, called\x01",
            "sepith, and make them into quartz, resulted in a\x01",
            "massive increase in the importance of septium as\x01",
            "a resource across the continent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_1088")


    AnonymousTalk(    #11
        (
            "\x07\x02#1SEntry: Orbal Airships/'Orbalships'\x01",
            "Commonly regarded as the crowning achievement\x01",
            "of orbment technology. Enables the power of\x01",
            "flight by combining a flight engine to control\x01",
            "gravity and an orbal engine to provide vast\x01",
            "amounts of energy. Because of the need for\x01",
            "high-efficiency orbal energy transfer and the\x01",
            "complexity of controlling the airship, many\x01",
            "modern orbalships are equipped with highly capable\x01",
            "orbal arithmetic logic units. Orbalships less than\x01",
            "20 arge in length are simply called 'airships.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_1286")


    AnonymousTalk(    #12
        (
            "\x07\x02#1SEntry: Orbal Weaponry\x01",
            "Any firearm or cannon powered with orbment tech-\x01",
            "nology. Currently the most common form of military\x01",
            "weaponry among many nations. With orbal firearms,\x01",
            "energy is focused in a helical path along the\x01",
            "barrel, down to a tiny point, which then forces a\x01",
            "large metal projectile outward at high velocity.\x01",
            "These guns can fire more rounds than traditional\x01",
            "gunpowder arms, and at adjustable levels of force.\x01",
            "Orbal Cannons, meanwhile, fire shells containing\x01",
            "energy which explode on impact. Similar to orbal\x01",
            "guns, these have less recoil than gunpowder-using\x01",
            "cannons, and their power can be similarly adjusted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_14FA")


    AnonymousTalk(    #13
        (
            "\x07\x02#1SEntry: Tactical Orbments\x01",
            "Orbments used to manipulate orbal magics.\x01",
            "Usually no larger than a pocket watch, so its\x01",
            "internal workings are extremely minute and\x01",
            "elegantly constructed. When quartz designed\x01",
            "for tactical orbment use is installed, it improves\x01",
            "the abilities of its bearer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #14
        (
            "\x07\x02#1SWhen this quartz synchronizes with the bearer\x01",
            "(a.k.a. the 'Resonance Phenomenon'), the\x01",
            "internal mechanisms take over the otherwise\x01",
            "complex process that would be required to use\x01",
            "magic, allowing just about anyone to use it in\x01",
            "the form of orbal arts. Furthermore, the arts\x01",
            "the user is able to use can be changed depending\x01",
            "on the combination of quartz inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_1789")


    AnonymousTalk(    #15
        (
            "\x07\x02#1SEntry: New Model Orbments\x01",
            "A new class of tactical orbments massively\x01",
            "upgraded from the preceding models developed by\x01",
            "the Epstein Foundation. In comparison to the old\x01",
            "model's six quartz slots, the new model has seven\x01",
            "slots.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #16
        (
            "\x07\x02#1SThis new model allows for more flexible quartz\x01",
            "arrangements, new combinations of usable orbal\x01",
            "magic, and even drastic increases in power.\x01",
            "However, as the architecture is drastically\x01",
            "different from the predecessor model, there is\x01",
            "no interchangeability in quartz between models.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199D")

    label("loc_1990")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_199D")

    label("loc_199D")

    Jump("loc_B5F")

    label("loc_19A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_1DAC")

    label("loc_19B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "[Combustion Engine]\x01",      # 0
            "[Gasoline]\x01",               # 1
            "[Haulage Vehicle]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A19"),
        (1, "loc_1B26"),
        (2, "loc_1C68"),
        (SWITCH_DEFAULT, "loc_1D7F"),
    )


    label("loc_1A19")


    AnonymousTalk(    #17
        (
            "\x07\x02#1SEntry: Combustion Engine\x01",
            "A machine which generates usable energy by\x01",
            "burning fuel within. Less efficient than its\x01",
            "orbal counterpart, due to issues with gaseous\x01",
            "exhaust and noise pollution.\x01\x01",
            "[Combustion Engine] \x01",
            "Number Owned: 1\x01",
            "Owner: Maintenance Chief Gustav\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8C")

    label("loc_1B26")


    AnonymousTalk(    #18
        (
            "\x07\x02#1SEntry: Gasoline\x01",
            "A liquid derived from the purification of the\x01",
            "naturally-occurring hydrocarbon compound known as\x01",
            "petroleum. Used primarily as fuel for combustion\x01",
            "engines and as an industrial solvent.\x01",
            "[Republic-Manufactured Gasoline]\x01",
            "Emergency Stores: 20 mid-sized tanks\x01",
            "Repository: Orbment Manufacturing Factory\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8C")

    label("loc_1C68")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #19
        (
            "\x07\x02#1SEntry: Orbal Haulage Vehicle\x01",
            "Any wheeled vehicle powered by orbal energy.\x01",
            "Widely considered uncomfortable to ride and\x01",
            "very limited in speed. Primarily used for\x01",
            "transporting cargo.\x01",
            "[Orbment-Powered Vehicle]\x01",
            "Owner: No Data\x01",
            "Repository: Underground Factory Entrance\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8C")

    label("loc_1D7F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D8C")

    label("loc_1D8C")

    Jump("loc_19B0")

    label("loc_1D8F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_1DAC")

    label("loc_1D9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DAC")

    label("loc_1DAC")

    Jump("loc_20D")

    label("loc_1DAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_758A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x1, 0x37, 0x99, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 0)), scpexpr(EXPR_END)), "loc_1DEF")
    OP_CC(0x1, 0x1, "#0 Viewed")
    Jump("loc_1E27")

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1E12")
    OP_CC(0x1, 0x1, "#0 Analysis Complete!")
    Jump("loc_1E27")

    label("loc_1E12")

    OP_CC(0x1, 0x1, "#0 Under Analysis")

    label("loc_1E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E93")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 1)), scpexpr(EXPR_END)), "loc_1E5B")
    OP_CC(0x1, 0x1, "#1 Viewed")
    Jump("loc_1E93")

    label("loc_1E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1E7E")
    OP_CC(0x1, 0x1, "#1 Analysis Complete!")
    Jump("loc_1E93")

    label("loc_1E7E")

    OP_CC(0x1, 0x1, "#1 Under Analysis")

    label("loc_1E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EFF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 2)), scpexpr(EXPR_END)), "loc_1EC7")
    OP_CC(0x1, 0x1, "#2 Viewed")
    Jump("loc_1EFF")

    label("loc_1EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1EEA")
    OP_CC(0x1, 0x1, "#2 Analysis Complete!")
    Jump("loc_1EFF")

    label("loc_1EEA")

    OP_CC(0x1, 0x1, "#2 Under Analysis")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_EXEC_OP, "OP_40(0x400, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F6B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 3)), scpexpr(EXPR_END)), "loc_1F33")
    OP_CC(0x1, 0x1, "#3 Viewed")
    Jump("loc_1F6B")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1F56")
    OP_CC(0x1, 0x1, "#3 Analysis Complete!")
    Jump("loc_1F6B")

    label("loc_1F56")

    OP_CC(0x1, 0x1, "#3 Under Analysis")

    label("loc_1F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_EXEC_OP, "OP_40(0x401, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 4)), scpexpr(EXPR_END)), "loc_1F9F")
    OP_CC(0x1, 0x1, "#4 Viewed")
    Jump("loc_1FD7")

    label("loc_1F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_1FC2")
    OP_CC(0x1, 0x1, "#4 Analysis Complete!")
    Jump("loc_1FD7")

    label("loc_1FC2")

    OP_CC(0x1, 0x1, "#4 Under Analysis")

    label("loc_1FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_EXEC_OP, "OP_40(0x402, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2043")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 5)), scpexpr(EXPR_END)), "loc_200B")
    OP_CC(0x1, 0x1, "#5 Viewed")
    Jump("loc_2043")

    label("loc_200B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_202E")
    OP_CC(0x1, 0x1, "#5 Analysis Complete!")
    Jump("loc_2043")

    label("loc_202E")

    OP_CC(0x1, 0x1, "#5 Under Analysis")

    label("loc_2043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x403, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 6)), scpexpr(EXPR_END)), "loc_2077")
    OP_CC(0x1, 0x1, "#6 Viewed")
    Jump("loc_20AF")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_209A")
    OP_CC(0x1, 0x1, "#6 Analysis Complete!")
    Jump("loc_20AF")

    label("loc_209A")

    OP_CC(0x1, 0x1, "#6 Under Analysis")

    label("loc_20AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x404, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_211B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 7)), scpexpr(EXPR_END)), "loc_20E3")
    OP_CC(0x1, 0x1, "#7 Viewed")
    Jump("loc_211B")

    label("loc_20E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_2106")
    OP_CC(0x1, 0x1, "#7 Analysis Complete!")
    Jump("loc_211B")

    label("loc_2106")

    OP_CC(0x1, 0x1, "#7 Under Analysis")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x405, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2187")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 0)), scpexpr(EXPR_END)), "loc_214F")
    OP_CC(0x1, 0x1, "#8 Viewed")
    Jump("loc_2187")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_2172")
    OP_CC(0x1, 0x1, "#8 Analysis Complete!")
    Jump("loc_2187")

    label("loc_2172")

    OP_CC(0x1, 0x1, "#8 Under Analysis")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_EXEC_OP, "OP_40(0x406, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 1)), scpexpr(EXPR_END)), "loc_21BB")
    OP_CC(0x1, 0x1, "#9 Viewed")
    Jump("loc_21F3")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_21DE")
    OP_CC(0x1, 0x1, "#9 Analysis Complete!")
    Jump("loc_21F3")

    label("loc_21DE")

    OP_CC(0x1, 0x1, "#9 Under Analysis")

    label("loc_21F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 1)), scpexpr(EXPR_EXEC_OP, "OP_40(0x407, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2262")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 2)), scpexpr(EXPR_END)), "loc_2228")
    OP_CC(0x1, 0x1, "#10 Viewed")
    Jump("loc_2262")

    label("loc_2228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_224C")
    OP_CC(0x1, 0x1, "#10 Analysis Complete!")
    Jump("loc_2262")

    label("loc_224C")

    OP_CC(0x1, 0x1, "#10 Under Analysis")

    label("loc_2262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 3)), scpexpr(EXPR_END)), "loc_2297")
    OP_CC(0x1, 0x1, "#11 Viewed")
    Jump("loc_22D1")

    label("loc_2297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_22BB")
    OP_CC(0x1, 0x1, "#11 Analysis Complete!")
    Jump("loc_22D1")

    label("loc_22BB")

    OP_CC(0x1, 0x1, "#11 Under Analysis")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x409, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2340")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x800), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 6)), scpexpr(EXPR_END)), "loc_2306")
    OP_CC(0x1, 0x1, "#12 Viewed")
    Jump("loc_2340")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_232A")
    OP_CC(0x1, 0x1, "#12 Analysis Complete!")
    Jump("loc_2340")

    label("loc_232A")

    OP_CC(0x1, 0x1, "#12 Under Analysis")

    label("loc_2340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x412, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 7)), scpexpr(EXPR_END)), "loc_2375")
    OP_CC(0x1, 0x1, "#13 Viewed")
    Jump("loc_23AF")

    label("loc_2375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2399")
    OP_CC(0x1, 0x1, "#13 Analysis Complete!")
    Jump("loc_23AF")

    label("loc_2399")

    OP_CC(0x1, 0x1, "#13 Under Analysis")

    label("loc_23AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x413, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_241E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 0)), scpexpr(EXPR_END)), "loc_23E4")
    OP_CC(0x1, 0x1, "#14 Viewed")
    Jump("loc_241E")

    label("loc_23E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2408")
    OP_CC(0x1, 0x1, "#14 Analysis Complete!")
    Jump("loc_241E")

    label("loc_2408")

    OP_CC(0x1, 0x1, "#14 Under Analysis")

    label("loc_241E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 4)), scpexpr(EXPR_EXEC_OP, "OP_40(0x414, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 1)), scpexpr(EXPR_END)), "loc_2453")
    OP_CC(0x1, 0x1, "#15 Viewed")
    Jump("loc_248D")

    label("loc_2453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_2477")
    OP_CC(0x1, 0x1, "#15 Analysis Complete!")
    Jump("loc_248D")

    label("loc_2477")

    OP_CC(0x1, 0x1, "#15 Under Analysis")

    label("loc_248D")

    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24AD")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2517")

    label("loc_24AD")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2517")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D0")
    Jump("loc_2517")

    label("loc_24D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_250A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_24FD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jump("loc_250A")

    label("loc_24FD")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jump("loc_24D0")

    label("loc_250A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_24B7")

    label("loc_2517")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2560"),
        (1, "loc_2B6B"),
        (2, "loc_2F42"),
        (3, "loc_33FF"),
        (4, "loc_3A6A"),
        (5, "loc_3FC1"),
        (6, "loc_4574"),
        (7, "loc_4A5C"),
        (8, "loc_4E5A"),
        (9, "loc_53B3"),
        (10, "loc_58BA"),
        (11, "loc_5DC7"),
        (12, "loc_649D"),
        (13, "loc_6800"),
        (14, "loc_6BE8"),
        (15, "loc_6FD2"),
        (SWITCH_DEFAULT, "loc_757A"),
    )


    label("loc_2560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2820")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #20
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 1/4]\x01",
            "My name is Celeste D. Auslese. I am the designer\x01",
            "of the Seal Mechanism, and the woman ultimately\x01",
            "responsible for the sealing of the Aureole. I\x01",
            "have decided to leave behind a series of records\x01",
            "for the world to come in case the second seal is\x01",
            "activated and the Aureole, which we sealed in\x01",
            "another dimension, should threaten to return.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #21
        (
            "\x07\x02#1SIf you who read this message seek to prevent the\x01",
            "Aureole's return, I pray this information will\x01",
            "aid you. However, if you seek to restore the\x01",
            "Aureole, I beg you, reconsider. The Aureole's\x01",
            "power is too great for we Children of Man to\x01",
            "wield. When we used it, it connected us to the\x01",
            "darkest Gehenna.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2280)
    Jump("loc_2B67")

    label("loc_2820")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 1/4]\x01",
            "My name is Celeste D. Auslese.\x01",
            "I am t■ de■■■er of ■ Seal M■■sm, and ■■\x01",
            "man ulti■■■■■y re■■■■e ■ th■ ■■■ing of\x01",
            "the A■■■■. I h■■ de■■■ed to ■■■■ b■■■ a\x01",
            "■■■■ of ■■■■ds for ■■■ ■■■■ to come ■ c■■\x01",
            "the S■■■■ ■■al is a■■■■ed and ■■ ■■■ole,\x01",
            "■■■■h we ■■■■■ in ■■■er d■■■■n, s■■■■ld\x01",
            "■■■■■■■ to re■■■.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #23
        (
            "\x07\x02#1SIf y■u wh■ r■■d th■ me■■ge ■■■ to\x01",
            "pr■■■■t the ■■■■■■■'s ■■■■rn, I ■■■■ th■■\x01",
            "in■■■■■ion will ■■■ y■u. Ho■■■■r, if y■u ■■■■\x01",
            "to r■■■ore the Au■■■■, I beg y■u, ■■■■■■■er.\x01",
            "The ■■■■■■■'s p■w■r is t■■ gr■■t f■r we Children\x01",
            "of Man t■ w■■■d. When we ■■■■ it, it l■■ ■■ ■■■o\x01",
            "the ■■■■■st Gehenna.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B67")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2D2C")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 2/4]\x01",
            "The purpose of the seals is to prevent any contact\x01",
            "between the Aureole and humanity, thus ensuring\x01",
            "humanity's survival. I feel the need to clarify:\x01",
            "the Aureole, itself, does not wish to control or\x01",
            "harm humanity. The disaster that visited us was\x01",
            "our fault alone.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #25
        (
            "\x07\x02#1SDo not doubt the mercy of our great Goddess in\x01",
            "giving this gift to us. It is we who are unequal\x01",
            "to such a gift.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2281)
    Jump("loc_2F3E")

    label("loc_2D2C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 2/4]\x01",
            "The purp■se ■f the s■■■s is to pr■■■ent any\x01",
            "c■ntact betw■■n the A■■■■e and hu■■■■y, thus\x01",
            "ens■ring ■■■■ity's ■■■■■■. I fe■l the n■ed t■\x01",
            "clari■■: the A■■■■■, its■lf, d■es n■t ■■■■ t■\x01",
            "c■■■■■l or ha■m huma■■■■. The di■■■■■ that\x01",
            "■■■■■ed us was ■ur f■■lt al■ne.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #27
        (
            "\x07\x02#1SDo n■t ■■■■ the merc■ of ■ur great\x01",
            "G■ddess in g■■■■ng t■■s gift t■ ■■.\x01",
            "It ■■ we wh■ ■re ■■equal t■ s■ch a g■■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3E")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_2F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_315D")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 3/4]\x01",
            "In truth, the construction and implementation of\x01",
            "the seal goes directly against the will of the\x01",
            "people and our democratic ideals. Even among our\x01",
            "group, some believed we should try to find a way\x01",
            "to use the Aureole's power effectively.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #29
        (
            "\x07\x02#1SHowever, once it obtained autonomy, the Aureole\x01",
            "began to change our society and our lives\x01",
            "drastically. It did not just concern itself with\x01",
            "our physical well-being; it considered our mental\x01",
            "well-being to be a top priority as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2282)
    Jump("loc_33FB")

    label("loc_315D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #30
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 3/4]\x01",
            "In tr■th, the c■■stru■■■ion and imp■■■ntati■■ of\x01",
            "the s■■■ goes dir■■■ly ■■■■nst th■ wi■■ ■f the\x01",
            "p■■■le and ■ur de■■■atic ide■■s. Ev■n am■■■ ■ur\x01",
            "g■■■p, s■me be■■■ed we sh■■■ try t■ ■■■ a w■■\x01",
            "t■ use th■ ■■■■■■'s p■w■r e■■■■■ly.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #31
        (
            "\x07\x02#1SH■wev■■, ■nce it ■bt■■■■d auto■■my, the\x01",
            "■■■■■■e be■■n to c■■■■■ ■ur s■■■■ty and ■■r ■■■■es\x01",
            "dras■■cally. It d■■ n■t just ■■■■ern its■■f w■th\x01",
            "■■r ph■■■■al w■ll-■■■ng; it ■■■■idered our ■■■tal\x01",
            "■■■■■■■■■ t■ be ■ t■p ■■■■■ity as w■ll.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33FB")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_33FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_36E8")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #32
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 4/4]\x01",
            "To provide an example: the Aureole facilitated the\x01",
            "creation of virtual realities intended to induce\x01",
            "euphoria in participants. It even altered brain\x01",
            "chemistry to achieve this. It was no different\x01",
            "than taking a powerful euphoric stimulant and\x01",
            "hallucinogen at the same time. Worse still, there\x01",
            "were no side effects. No physical ones, at least.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #33
        (
            "\x07\x02#1SSuch 'boons' have brought humanity's very\x01",
            "continued existence into question. The effects\x01",
            "already begin to tell upon our citizenry, and we\x01",
            "have precious little time left to us. As a result,\x01",
            "we few have overcome our differences to undertake\x01",
            "the sealing, all too aware of the many difficulties\x01",
            "we are likely to face in the process.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2283)
    Jump("loc_3A66")

    label("loc_36E8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #34
        (
            "\x07\x02#1S[Concerning the Seal Mechanism 4/4]\x01",
            "To pr■vide an ■■■■ple: the A■■■■■ faci■■■■■■d\x01",
            "the cre■■■■n ■f vi■■■■al rea■■■ies int■■ded t■\x01",
            "■■■uce eu■■■■a in pa■■■■ip■■ts. It ■ven a■t■■ed\x01",
            "b■■■n che■■stry to ■■■■eve th■s. It was n■\x01",
            "di■■er■nt than t■■■■g a p■■■■ful ■■■■■ric\x01",
            "st■■ulant and ■■■■■■inog■n at the ■■■■ time.\x01",
            "W■rse ■■ill, th■■■ ■■re n■ side ef■■■■s.\x01",
            "No phy■■■■■ o■■s, at le■st.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #35
        (
            "\x07\x02#1SSuch 'b■■ns' have br■■■ght hum■■ity's very\x01",
            "co■■■■■d exi■■■nce int■ que■■■■on. The eff■■■ts\x01",
            "already begin t■ tell up■■ ■ur citi■■■ry, and we\x01",
            "have preci■■s littl■ time l■ft t■ us.\x01",
            "As a res■lt, we fe■ have ove■■■me our di■■■■■■■■\x01",
            "t■ unde■■■■■e th■ sealing, all too■■■of ■■■■ ties\x01",
            "are are like■■■■to face in■■ process.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A66")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_3A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_3CD3")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #36
        (
            "\x07\x02#1S[Lakeside Underground Facility 1/4]\x01",
            "In order to make the Seal Mechanism into a\x01",
            "reality, we needed both enormous amounts of energy\x01",
            "and massive facilities. We, to source the energy,\x01",
            "first thought of using the Aureole itself.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #37
        (
            "\x07\x02#1SThe Aureole responds to people's wishes and gives\x01",
            "its boon--in other words, by 'wishing' we thought\x01",
            "that perhaps we could pull the needed amount of\x01",
            "energy from the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #38
        (
            "\x07\x02#1S...However, that did not come to pass. Shortly\x01",
            "after the Aureole gained autonomy, it turned to\x01",
            "simply one-sidedly bestowing its gifts regardless\x01",
            "of the wishes of the people.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2284)
    Jump("loc_3FBD")

    label("loc_3CD3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        (
            "\x07\x02#1S[Lakeside Underground Facility 1/4]\x01",
            "In or■■■ to m■ke the Seal Mec■■■■■m into a\x01",
            "■eal■■y, w■ needed b■■h ■■■■ous am■■nts ■■ energy\x01",
            "and mas■■■■ facil■■■■s. We, to ■■■■■■ the ■■■■,\x01",
            "■irs■ th■■■■ of using ■■e Aureole ■■lf.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #40
        (
            "\x07\x02#1SThe Aur■■le ■■spond■ to ■■■■■■ 's wishes ■■d gives\x01",
            "its boon--in ■■■er words, ■■ 'w■sh■■g' w■ thought\x01",
            "that ■■■■■ps we could ■ull the n■■■ed ■mo■■t of\x01",
            "e■■■gy ■■■■ ■■■ Aureole.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #41
        (
            "\x07\x02#1S... However, ■■■■ ■■■ not c■■e to ■■■■. Shortly\x01",
            "■fter ■h■ Aureole ■■■■ed auto■■■, it ■ur■■d to\x01",
            "simply ■■■■■■■■ b■st■■ing its ■■fts ■■■■dless\x01",
            "of ■■■ w■■h■s o■ the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBD")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_3FC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_4254")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        (
            "\x07\x02#1S[Lakeside Underground Facility 2/4]\x01",
            "We could not use the power of the Aureole. Casting\x01",
            "our eyes beyond the city, we began to consider using\x01",
            "the energy sleeping in the septium veins that rest\x01",
            "deep beneath the earth, and eventually resolved to\x01",
            "build atop those. However, we were already under\x01",
            "the watch of the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #43
        (
            "\x07\x02#1SIt seems the Aureole had come to the conclusion\x01",
            "that its first priority was the continuation of\x01",
            "the city, and therefore the elimination of all\x01",
            "potential obstacles to that. So, to deceive the\x01",
            "Aureole, we proceeded with the construction of\x01",
            "these buildings under the guise of monitoring\x01",
            "the septium veins.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2285)
    Jump("loc_4570")

    label("loc_4254")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #44
        (
            "\x07\x02#1S[Lakeside Underground Facility 2/4]\x01",
            "We could ■ot ■■■ the ■■■er of th■ ■■■eo■■. Casting\x01",
            "our eyes ■■■■ the ci■■, we began to con■■■■■\x01",
            "the ■■ergy s■e■■■ng in the s■■■v■■■s that rest\x01",
            "d■■■ ■ea■■ the ■■■■■, and eventually ■■■■ved ■■\x01",
            "b■■ld atop ■■■se. Ho■■■■■ we ■■■e ■■■■■ un■■r\x01",
            "■■ w■■■h of the ■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #45
        (
            "\x07\x02#1S■■ seems ■■■■■u■■■■■ had come ■o the ■on■■■sion\x01",
            "that its ■■■■■ prior■■■ was the con■■■■■■ ■■\x01",
            "the city, ■■d theref■re the elimination of ■■■\x01",
            "■■■■■■■ ob■■ac■es to ■■■at. So, to d■■■■■ the\x01",
            "Aureole, ■■ proc■■■ed with the ■■■st■■■tion of\x01",
            "these ■■■l■ings under the ■■■■■ o■ mo■■tor■■■\x01",
            "the s■■■■■■ veins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4570")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_4574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_479F")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #46
        (
            "\x07\x02#1S[Lakeside Underground Facility 3/4]\x01",
            "The facility was built roughly 500 arge beneath\x01",
            "the earth on the eastern side of Valleria Lake.\x01",
            "According to our investigations, this was the\x01",
            "location where the septium veins gathered most\x01",
            "efficiently. The land beneath the city was a\x01",
            "sprawling primal forest. As it was untouched by\x01",
            "human activity, building on top of it proved\x01",
            "remarkably easy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #47
        (
            "\x07\x02#1SWe, while avoiding the attention of the Aureole,\x01",
            "collected all the technology we had, and hurried\x01",
            "to complete the underground facility.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2286)
    Jump("loc_4A58")

    label("loc_479F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #48
        (
            "\x07\x02#1S[Lakeside Underground Facility 3/4]\x01",
            "The ■■■■ty was ■■■■ roughly ■00 arge b■■■a■■\x01",
            "■he ■■■th on the ea■■■r■ side of ■■■■■■ ■■ke.\x01",
            "A■■■■ing ■■ our ■■■■ti■■tions, this ■as ■■e\x01",
            "loc■■ion wher■ the ■■■■■■■ ■■■■s g■th■■ed mo■■\x01",
            "■ffi■■■■ly. ■■■ l■nd beneath the ■■■■ was a\x01",
            "sp■■■■■ing pri■■■ f■■■■t. As i■ was ■■to■■■ed by\x01",
            "human ■■■■■■, buil■■■■ ■■ top ■■ it pr■■■d\x01",
            "remarkably ■■■■.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #49
        (
            "\x07\x02#1S■■, while av■■■ing the ■■■■■■ion ■f the ■■■■■■■e,\x01",
            "co■■ected a■■ the ■■■h■■logy we had, an■ ■■■ried\x01",
            "to com■■■■■ the u■■■■■■r■■nd facilit■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A58")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_4A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_4C22")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #50
        (
            "\x07\x02#1S[Lakeside Underground Facility 4/4]\x01",
            "While the construction of the underground facility\x01",
            "was underway, we built additional structures\x01",
            "on the fringes of the surface. The Ahnenburg,\x01",
            "whose inner wall points ever towards the Aureole,\x01",
            "and the four device towers that surround the\x01",
            "Aureole.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "\x07\x02#1SEach system of structures possessed a critical\x01",
            "role in the plan and were as vital to the Seal\x01",
            "Mechanism as the underground facility.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2287)
    Jump("loc_4E56")

    label("loc_4C22")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #52
        (
            "\x07\x02#1S[Lakeside Underground Facility 4/4]\x01",
            "Wh■■■ the c■■■■r■■tion of ■he under■■■■■ ■■■ility\x01",
            "was ■■der■■y, ■■ ■■■■■ ad■■■io■■l ■■ruc■ur■■\x01",
            "■■ ■■■ fr■■ges of the surface. The A■■■■■ur■,\x01",
            "whose ■■■er wa■■ points eve■ toward■ ■■■ Aureole,\x01",
            "■nd the four ■■vi■■ ■■■■■ that ■■rround the\x01",
            "Aur■■■e.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #53
        (
            "\x07\x02#1S■■■■ syste■ of str■■■■■es po■■e■■ed a ■■■t■cal\x01",
            "ro■e ■■ the pla■ and ■■re a■ vital ■■ ■■■ S■■l\x01",
            "■■chan■■■ as the ■■■■■ground ■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E56")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_4E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_50BD")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #54
        (
            "\x07\x02#1S[About the Aureole's Seal 1/4]\x01",
            "When we were closing in on completing the\x01",
            "underground facility, unbeknownst to us, our seal\x01",
            "plan was discovered by the Aureole. One of our\x01",
            "comrades fell victim to the sweet seduction of the\x01",
            "Aureole's euphoric simulations, and he was lost to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "\x07\x02#1SHowever, the silver lining in this disaster was\x01",
            "that this comrade was not aware of the full scale\x01",
            "of the plan. With the information it gleaned from\x01",
            "his mind, the Aureole focused entirely on the\x01",
            "underground facility by the lakeside, and it paid\x01",
            "no attention to the Ahnenburg or the device\x01",
            "towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2288)
    Jump("loc_53AF")

    label("loc_50BD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #56
        (
            "\x07\x02#1S[About the Aureole's Seal 1/4]\x01",
            "When w■ were ■■■■ing in on ■■■■■■ing the\x01",
            "underground ■■■■■■, un■■■■■■st ■■ us, our ■eal\x01",
            "■■an w■s ■■■cover■■ by t■■ Aur■ol■. ■■■ of our\x01",
            "co■rades ■■ll v■■ti■ to ■■e s■■■t ■■■duction of ■he\x01",
            "A■■■ol■'s e■■■■■ic sim■■■■ions, ■nd he w■s lost to\x01",
            "■■.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #57
        (
            "\x07\x02#1SHowe■er, the s■■■er ■■■in■ in this ■isast■■ was\x01",
            "t■■t ■■■■ co■■ade was not ■■ar■ of the ■■■■ scale\x01",
            "of the p■■■. ■ith the ■■forma■■on it g■■■■■ed from\x01",
            "his ■■■d, the ■ureole ■■■■■■■ ■■■■■■ on ■■■\x01",
            "un■■■gro■■■ ■acilit■ by the ■■■■side, and i■ p■■d\x01",
            "no a■■entio■ to the ■■■enb■■g or the ■evice\x01",
            "Tow■■■. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_53AF")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_53B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_55E5")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #58
        (
            "\x07\x02#1S[About the Aureole's Seal 2/4]\x01",
            "The Aureole, having learned of our plan, took to\x01",
            "force. The Aureole manifested Reveries as its\x01",
            "defenders, and set them upon us in the facility.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #59
        (
            "\x07\x02#1SHowever, we were saved by our decision to build\x01",
            "the facility underground. Just one single channel\x01",
            "connected the facility to the surface. The\x01",
            "Reveries' attacks could not reach down 500 arge\x01",
            "beneath the surface.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #60
        (
            "\x07\x02#1SThe attacks by the Reveries went on and on, day\x01",
            "and night without pause. Eventually our defensive\x01",
            "line began to reach its limits.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2289)
    Jump("loc_58B6")

    label("loc_55E5")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #61
        (
            "\x07\x02#1S[About the Aureole's Seal 2/4]\x01",
            "The ■■■■ol ■, ha ■■ng ■ea■■■d ■■ ■■■ ■lan, too■ to\x01",
            "fo■■e. The Aureole m■n■■es■■d ■■■■■ies as i■■\x01",
            "defend■■■, and ■et t■■m ■■■■ ■■ in ■h■ ■ac■■■ty.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #62
        (
            "\x07\x02#1S■■■eve■, we w■■e saved ■y our ■■■i■■■n to ■■■■■\x01",
            "the f■■■l■■■ ■n■■■gro■■d. Jus■ on■ si■■le ■h■■nel\x01",
            "co■■ecte■ the ■■■■■■ to the sur■■c■. The\x01",
            "Rev■■■es' ■■■ack■ cou■d not ■■■ch ■o■n ■■0 ar■e\x01",
            "■en■■■h the surface.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #63
        (
            "\x07\x02#1STh■ ■■■ac■s by the ■■■■■■■ ■■■■ on ■■■ o■, day\x01",
            "and ■■■h■ w■■■out ■■us■. Ev■■■ua■■■ our d■■■n■ive\x01",
            "■■■■ bega■ ■■ r■■■h it■ l■mi■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58B6")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_58BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_5AF3")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #64
        (
            "\x07\x02#1S[About the Aureole's Seal 3/4]\x01",
            "While under attack by the Reveries we were able\x01",
            "to finish the facility, but it took time to\x01",
            "secure the necessary energy. During the process,\x01",
            "it seems we got careless, and a single Reverie\x01",
            "broke into the facility proper.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #65
        (
            "\x07\x02#1SOnce inside, stopping it was difficult. The\x01",
            "Reverie reached the deepest sections in an\x01",
            "instant. We were just a hair's breadth from total\x01",
            "disaster when the full power for the sealing\x01",
            "operation was finally gathered. Just as the\x01",
            "Reverie set upon us, we activated the first\x01",
            "barrier.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x228A)
    Jump("loc_5DC3")

    label("loc_5AF3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        (
            "\x07\x02#1S[About the Aureole's Seal 3/4]\x01",
            "Wh■■■ un■er ■■■ac■ by ■■■ Re■■ri■■ we ■■■■ ■■■e\x01",
            "to ■■ni■h the ■■■■■■, b■■ it t■■k ■■m■ to\x01",
            "secure t■■ ne■e■■ar■ ■■■rgy. ■■■ing the pr■cess\x01",
            "■■ s■■■s we ■■■ c■■el■■■, and a ■■■gle ■■■■■■\x01",
            "bro■■ into ■he ■■■il■■y pr■■er.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        (
            "\x07\x02#1S■■ce ■■side, sto■■■ng it was ■i■■■■ult. The\x01",
            "R■■■■■ie r■■ched the ■■■■■■■ se■■i■ns in ■■\x01",
            "in■■■nt. We we■■ ■■st a ■ai■'s bread■■ f■■m total\x01",
            "■■■aster ■■■n the f■■l powe■ for the s■■■ing\x01",
            "■■■■ation wa■ fina■■y ■athered. Just ■■ the\x01",
            "Re■■■ie set ■pon ■■, we act■■■■ed the ■irst\x01",
            "■■■■■■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC3")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_5DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_60AD")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #68
        (
            "\x07\x02#1S[About the Aureole's Seal (4/4)]\x01",
            "The light fired from the facility, reflected off\x01",
            "the inner wall of the Ahnenburg, caught the\x01",
            "Aureole floating in the sky. In that moment, the\x01",
            "Aureole disappeared from us, and the Reveries\x01",
            "stopped entirely. Through this, we knew that the\x01",
            "first barrier was successful.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #69
        (
            "\x07\x02#1SThe Aureole is, of the Sept-Terrions, the treasure\x01",
            "governing the power of space. What was needed to\x01",
            "nullify the Aureole, which held absolute dominion\x01",
            "over space itself, was to utterly sever its\x01",
            "connections to space, and indeed even to time\x01",
            "itself. The Seal Mechanism, born of our hard work,\x01",
            "had sent the Aureole, along with the entire city,\x01",
            "into another dimension, and successfully\x01",
            "temporally froze it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x228B)
    Jump("loc_6499")

    label("loc_60AD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #70
        (
            "\x07\x02#1S[About the Aureole's Seal (4/4)]\x01",
            "■ light ■■■■■ fr■m ■■■ facility, ■■■■ected off\x01",
            "■■■ ■■■■■ wall of the ■■ne■b■■g, ca■■ht the\x01",
            "■■■■■■■ ■■oat■■g ■■ ■■■ sky. In ■■■■ mo■■■■, ■■■\x01",
            "Aureole ■■■■■■■■■■■ ■■■■ us, ■■■ ■■■ ■■■eries\x01",
            "stopped ■nt■■ely. Through ■■■s, we k■■w that the\x01",
            "■■■■■ ■■■■■■■ was successful.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #71
        (
            "\x07\x02#1S■■■ Aureole ■■, of ■■■ ■■■■■■■■■■■, the tre■■■re\x01",
            "gov■■■■■■ the power ■■ space. ■■■■ was ■■eded to\x01",
            "nul■■■■ ■■■ Aureole, ■■■■ held abs■■■te dom■■■■■\x01",
            "■■■■ space itself, ■■■ to utterly sever ■■■\x01",
            "■■■■■ctions ■■ space, ■■■ ■■■■■■ ■■■■ ■■ ■■■■\x01",
            "■■■■■■. ■■■ Seal ■■■■■■■■■, ■■■■ ■■ ■■■ hard ■■■■,\x01",
            "had sent ■■■ ■■■■■■■, ■■■■■ ■■■■ ■■■ ■■■■■■ city,\x01",
            "into ■■■■■■■ ■■■■■■■■■ a■d ■■■■essfully te■■■■■■■■\x01",
            "froze ■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6499")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_649D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6621")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #72
        (
            "\x07\x02#1S[About the Device Towers 1/4]\x01",
            "The first barrier had activated successfully, and\x01",
            "we had succeeded in performing a temporal freeze\x01",
            "upon the Aureole in another dimension. However,\x01",
            "that was not the only barrier within the plan to\x01",
            "seal the Aureole.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #73
        (
            "\x07\x02#1SThe plan's final defense line, the second barrier.\x01",
            "--The key to that lies within the four device\x01",
            "towers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2276)
    Jump("loc_67FC")

    label("loc_6621")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #74
        (
            "\x07\x02#1S[About the Device Towers 1/4]\x01",
            "■■■ first ■■r■■■r ■■■ acti■a■ed ■■■■■ssfu■■■, and\x01",
            "w■ had s■■■ee■■d in p■■■orming a ■■mpo■■■ ■■ee■e\x01",
            "upon the Aur■ole in a■■■her ■■■■■■■■■. H■■ever,\x01",
            "■■at was ■■■ the ■■nly ba■■ie■ withi■ the ■■■■ to\x01",
            "seal th■ A■■■ol■.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #75
        (
            "\x07\x02#1SThe p■■■'s ■■nal de■en■e line, the ■■■ond ba■ri■■.\x01",
            "--The ■■■ to th■t lies ■■thin the fo■■ de■i■■\x01",
            "■o■ers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67FC")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_6800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_69BE")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #76
        (
            "\x07\x02#1S[About the Device Towers 2/4]\x01",
            "This mechanism is built to activate should the\x01",
            "first barrier fall and time once again tick in the\x01",
            "space of the Aureole. The second barrier's other\x01",
            "name is the Gravity Barrier, and it can manifest\x01",
            "gravity inside the other dimension.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #77
        (
            "\x07\x02#1SShould the Aureole resume activity, by tying this\x01",
            "other dimension down with lynchpins of gravity,\x01",
            "the goal was to prevent its return to reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2277)
    Jump("loc_6BE4")

    label("loc_69BE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #78
        (
            "\x07\x02#1S[About the Device Towers 2/4]\x01",
            "This ■■■hanis■ is ■■ilt to ■■■■■■e should ■he\x01",
            "F■■■t ■arr■■r ■■ll and tim■ once ■■■■■ tick ■n the\x01",
            "■■■ce of th■ Aure■■e. ■■■ ■■■■■■ B■rri■■'s ■ther\x01",
            "na■e is ■■e ■■a■ity ■■■■■■, and ■■ can ■ani■■■t\x01",
            "■■■■■■ ins■■e the ■■h■■ dimension.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #79
        (
            "\x07\x02#1SS■■■d the ■ur■■■e resume ■ct■■■ty, by ty■■■ th■s\x01",
            "other ■■■en■■■n do■■ wi■h ■■■chp■■s of g■■■ity,\x01",
            "the goal ■■s t■ prevent ■■■ ■■■■■■ to reality.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE4")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_6BE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_6DAA")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #80
        (
            "\x07\x02#1S[About the Device Towers 3/4]\x01",
            "If the second barrier activates, it signals that\x01",
            "the Aureole is once again active. As a result,\x01",
            "with its Gospels, anyone will be free to draw\x01",
            "out its power.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #81
        (
            "\x07\x02#1SThe Gospels remaining on Liber Ark were sealed\x01",
            "with the Aureole. However, should something that\x01",
            "could serve in place of the Gospels be born in the\x01",
            "world to come, the Aureole will be free to wield\x01",
            "its power in reality again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2278)
    Jump("loc_6FCE")

    label("loc_6DAA")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #82
        (
            "\x07\x02#1S[About the Device Towers 3/4]\x01",
            "I ■ the ■■con■ ba■■■■er act■■■■s, it ■■g■■ls that\x01",
            "the ■■reole is ■■■e again a■■i■e. As a ■■■■■■,\x01",
            "with its ■ospe■s, anyone ■■■l be fr■■ to ■ra■\x01",
            "out ■■■ power.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #83
        (
            "\x07\x02#1S■■■ ■■■■■■■ re■ain■■■ on L■■■r ■■■ were sealed\x01",
            "w■■h the Aur■■le. ■■■ev■r, should ■■methin■ that\x01",
            "could ■■■■■ in pl■■e ■■ ■■■ G■■■els be ■■■■ in the\x01",
            "world ■■ come, the ■ureole w■■l be f■ee to ■■eld\x01",
            "its ■■■■■ in ■■■■■■ again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FCE")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_6FD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_7256")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #84
        (
            "\x07\x02#1S[About the Device Towers 4/4]\x01",
            "We succeeded in sealing the Aureole, but its power\x01",
            "has not been destroyed. We will root ourselves to\x01",
            "this land and watch over the Aureole. I pray that\x01",
            "we will be successful in our vigil and that these\x01",
            "records are never seen by any eyes.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #85
        (
            "\x07\x02#1SHowever, while we are steadfast in our duty, we\x01",
            "predict that such will not be our future. When the\x01",
            "Aureole once again returns to reality, how will\x01",
            "our descendents choose to respond? Believing that\x01",
            "we will not make the same mistake again, and the\x01",
            "time will come when we are truly free of the\x01",
            "Aureole, I leave these records for the future.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2279)
    Jump("loc_7576")

    label("loc_7256")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #86
        (
            "\x07\x02#1S[About the Device Towers 4/4]\x01",
            "We ■■■■eeded in ■■■ling the ■■■eol■, but ■■■ power\x01",
            "has ■ot been d■■■roye■. ■■ will ■oot ■■■selves to\x01",
            "this la■d ■■■ ■■■■■ over ■he ■■■eole. I ■■■y t■■■\x01",
            "we ■ill be suc■■■ful in ■■■ ■■■■■ an■ ■■at t■■■e\x01",
            "records ■■■ never see■ by ■■y ■■■s.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #87
        (
            "\x07\x02#1S■■■■■■, wh■■e we are ■■■ad■■■t in our ■■■■, we\x01",
            "p■ed■■t that s■ch will ■■■ be our ■■tu■e. Wh■■ the\x01",
            "Aureole once ■ga■n ■■■■■■ to ■eal■■y, how w■ll\x01",
            "our des■■■de■■■ ch■■se to ■■■■■■? Be■■evin■ that\x01",
            "■■ wi■■ ■ot make ■■■ same ■■■■a■e again, ■■■ ■■■\x01",
            "tim■ will ■■me w■■■ we are tr■■y ■■ee of the\x01",
            "Au■■■le, I ■■■ve these reco■■s for the ■■■■■■.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7576")

    CloseMessageWindow()
    Jump("loc_7587")

    label("loc_757A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7587")

    label("loc_7587")

    Jump("loc_1DAF")

    label("loc_758A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_XOR_SAVE), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_75A7")

    label("loc_759A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75A7")

    label("loc_75A7")

    Jump("loc_1A9")

    label("loc_75AA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
